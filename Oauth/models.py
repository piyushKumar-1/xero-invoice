from django.db import models
import datetime
from django.utils.timezone import now



class Invoice(models.Model):
    Type = models.CharField(max_length=100, default="ACCREC")
    Date = models.DateField(blank=True, default="")
    DueDate = models.DateField(blank=True, default="")
    LineAmountTypes = models.CharField(max_length=100, default="Exclusive", blank=True)
    InvoiceNumber = models.CharField(max_length=255, blank=True)
    Refrence = models.CharField(max_length=255, blank=True)
    Url = models.URLField(blank=True)
    CurrencyCode = models.CharField(blank=True, max_length=100, default='INR')
    CurrencyRate = models.CharField(blank=True, max_length=100)
    Status = models.CharField(blank=True, max_length=100)
    SentToContact = models.CharField(blank=True, max_length=100)
    ExpectedPaymentDate = models.DateField(blank=True, default="")
    PlannedPaymentDate = models.DateField(blank=True, default="")



class LineItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Description = models.CharField(max_length=4000, blank=True)
    Quantity = models.CharField(max_length=13, blank=True)
    UnitAmount = models.CharField(max_length=200, blank=True)
    ItemCode = models.CharField(max_length=200, blank=True)
    AccountCode = models.CharField(max_length=200, blank=True)
    TaxType = models.CharField(max_length=200, blank=True, default='OUTPUT')
    TaxAmount = models.CharField(max_length=200, blank=True)
    LineAmount = models.CharField(max_length=200, blank=True)
    DiscountRate = models.CharField(max_length=200, blank=True)



class Tracking(models.Model):
    lineitems = models.ForeignKey(LineItems, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Option = models.CharField(max_length=200)

