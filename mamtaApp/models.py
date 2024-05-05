from django.contrib.auth.models import User
from django.db import models
from stdimage import StdImageField


class SuperAdmin(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class Company(models.Model):
    name = models.CharField(blank=True, null=True, max_length=250)
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class StaffType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class Admin(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class StaffUser(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    photo = StdImageField(upload_to='Images', blank=True, null=True,
                          variations={'thumbnail': {'width': 70, 'height': 70}})
    idProof = StdImageField(upload_to='IdProof', blank=True, null=True,
                            variations={'thumbnail': {'width': 70, 'height': 70}})
    isActive = models.BooleanField(default=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    staffTypeID = models.ForeignKey(StaffType, blank=True, null=True, on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    canTakePayment = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=100, blank=True, null=True)
    closingBalance = models.FloatField(default=0.0)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class MoneyToCollect(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=200, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class MoneyCollection(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    collectedBy = models.ForeignKey(StaffUser, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    paymentMode = models.CharField(max_length=100, default='Cash')
    chequeImage = models.ImageField(upload_to='Cheques', blank=True, null=True)
    latitude = models.CharField(max_length=200, default='0.0')
    longitude = models.CharField(max_length=200, default='0.0')
    isDeleted = models.BooleanField(default=False)
    isAddedInSales = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class CashMoneyCollection(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    collectedBy = models.ForeignKey(StaffUser, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    paymentMode = models.CharField(max_length=100, default='Cash')
    chequeImage = models.ImageField(upload_to='Cheques', blank=True, null=True)
    latitude = models.CharField(max_length=200, default='0.0')
    longitude = models.CharField(max_length=200, default='0.0')
    isDeleted = models.BooleanField(default=False)
    isAddedInSales = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class SupplierCollection(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    collectedBy = models.ForeignKey(StaffUser, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    paymentMode = models.CharField(max_length=100, default='Cash')
    isDeleted = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isApproved = models.BooleanField(default=False)
    approvedBy = models.CharField(max_length=100, blank=True, null=True, default='N/A')


class LoginAndLogoutStatus(models.Model):
    userID = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    statusType = models.CharField(max_length=100, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)


class SupplierInvoiceCollection(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    collectedBy = models.ForeignKey(StaffUser, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=500, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    invoiceNumber = models.CharField(max_length=100, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isApproved = models.BooleanField(default=False)
    approvedBy = models.CharField(max_length=100, blank=True, null=True, default='N/A')


class StaffAdvanceToBuyer(models.Model):
    buyerID = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    collectedBy = models.ForeignKey(StaffUser, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    remark = models.CharField(max_length=500, blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    companyID = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
