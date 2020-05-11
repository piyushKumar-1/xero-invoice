from typing import Dict
from django.shortcuts import render, redirect
from django.http import JsonResponse
from xero.auth import OAuth2Credentials
from xero.constants import XeroScopes
from xero import Xero
from .forms import InvoiceForm, LineItemsForm, TrackingForm
from .clean_json import beautify


client_id = '7F540F8988B4465AB967C6BF5A5312FE'
client_secret = 'W6H3IIWWlC063yWtSsK4UjI9FSHpvkBYsNA79KD-vrYZUvIR'
callback_uri = "https://localhost:8000/auth/"





mycache: Dict[str, dict] = {'xero_creds':{}}
data = {}
my_scope = [XeroScopes.ACCOUNTING_TRANSACTIONS,
             XeroScopes.ACCOUNTING_CONTACTS]


def index(request):
    credentials = OAuth2Credentials(client_id, client_secret, scope=my_scope,
                                    callback_uri=callback_uri)
    authorisation_url = credentials.generate_url()
    mycache['xero_creds'] = credentials.state

    return redirect(authorisation_url)


def auth(request):

    global mycache
    cred_state = mycache['xero_creds']
    print(cred_state)
    credentials = OAuth2Credentials(**cred_state)
    credentials.verify(request.get_raw_uri())
    tenants = credentials.get_tenants()
    credentials.tenant_id = tenants[0]['tenantId']
    mycache['xero_creds'] = credentials.state
    return redirect('Oauth:add')


def add_invoice(request):
    url = "/add/"
    global data
    global mycache
    cred_state = mycache['xero_creds']
    if 'tenant_id' in cred_state:
        credentials = OAuth2Credentials(**cred_state)
        xero = Xero(credentials)
        contacts = xero.contacts.all()
        form = InvoiceForm()
        if request.method == 'POST':
            form = InvoiceForm(request.POST)
            if form.is_valid():
                data['invoice'] = form.cleaned_data
                data['invoice']['LineItems'] = list()
                context = {"contacts": contacts}
                return render(request, 'addcont.html', context)
        context = {"form": form, 'url': url}
        return render(request, 'invoice.html', context)
    else:
        return redirect('Oauth:index')


def add_conID(request, conID):
    global mycache
    cred_state = mycache['xero_creds']
    if 'tenant_id' in cred_state and 'Type' not in data['invoice']:
        return redirect('Oauth:add')
    if 'tenant_id' in cred_state:
        print(conID)
        data['invoice']['Contact'] = {'ContactID': conID}
        print(data)
        return redirect('Oauth:addl')
    else:
        return redirect('Oauth:index')




def add_line(request):
    global data
    global mycache
    cred_state = mycache['xero_creds']
    if 'tenant_id' in cred_state and 'Type' not in data['invoice']:
        return redirect('Oauth:add')
    if 'tenant_id' in cred_state:
        print("jaunga")
        form = LineItemsForm()
        if request.method == 'POST':
            form = LineItemsForm(request.POST)
            if form.is_valid():
                data['invoice']['LineItems'].append(form.cleaned_data)
                print(data)
                return render(request, 'ask.html')
        context = {"form": form, 'url': "/addline/"}
        return render(request, 'addmore.html', context)
    else:
        return redirect('Oauth:index')

def submit(request):
    global data
    global mycache
    cred_state = mycache['xero_creds']
    if 'invoice' not in data:
        return redirect('Oauth:add')
    if 'invoice' in data and 'Contact' not in data['invoice']:
        return redirect('Oauth:add')
    if 'tenant_id' in cred_state:
        credentials = OAuth2Credentials(**cred_state)
        xero = Xero(credentials)
        print(xero)

        print("karunga")
        print(data['invoice'])
        d = data['invoice']
        print(d)
        d = beautify(d)
        xero.invoices.put(d)
        data = {}
        return JsonResponse(d, safe=False)

    else:
        return redirect('Oauth:index')