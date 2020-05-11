from django import forms
from .models import Invoice, LineItems, Tracking

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('Type', 'Date', 'DueDate','LineAmountTypes', 'InvoiceNumber',
                 'Refrence', 'Url', 'CurrencyCode', 'CurrencyRate', 'Status',
                 'SentToContact', 'ExpectedPaymentDate', 'PlannedPaymentDate'
                 )



class LineItemsForm(forms.ModelForm):
    class Meta:
        model = LineItems
        fields = ('Description', 'Quantity', 'UnitAmount', 'ItemCode', 'AccountCode', 'TaxType',
                 'TaxAmount', 'LineAmount', 'DiscountRate'
                 )



class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = ('Name', 'Option')