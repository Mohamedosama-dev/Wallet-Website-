from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from decimal import Decimal

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, username, password=None, is_active=True, phone_credit=Decimal('0.00')):
        if not phone:
            raise ValueError('Users must have a phone number')
        user = self.model(phone=phone, username=username, is_active=is_active, phone_credit=phone_credit)
        user.set_password(password)  # Set password correctly
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None):
        user = self.create_user(phone, username, password, is_active=True, phone_credit=Decimal('0.00'))
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phone_credit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin 
    



class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    


class Charity(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
   
    
    
    def __str__(self):
        return self.name
    


class Service(models.Model):
    SERVICE_TYPES = [
        ('Electricity', 'Electricity'),
        ('Gas', 'Gas'),
        ('Water', 'Water'),
    ]
    
    name = models.CharField(max_length=50, choices=SERVICE_TYPES)
    service_number = models.CharField(max_length=20)  # Customer service number

    def __str__(self):
        return f"{self.name} (Service Number: {self.service_number})"



class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
        ('Transfer', 'Transfer'),
        ('Recharge Phone', 'Recharge Phone'),
        ('Charity', 'Charity Transfer'),
        ('Service Payment', 'Service Payment') 
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # for recipient phone numbers
    charity = models.ForeignKey(Charity, on_delete=models.SET_NULL, null=True, blank=True)  
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


    def __str__(self):
        if self.charity:
            return f"{self.transaction_type} of {self.amount} to {self.charity.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        return f"{self.transaction_type} of {self.amount} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


    
    def __str__(self):
        if self.service:
            return f"{self.transaction_type} of {self.amount} for {self.service.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


    def __str__(self):
        if self.transaction_type == 'Charity' and self.charity:
            return f"{self.transaction_type} of {self.amount} to {self.charity.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        elif self.transaction_type == 'Service Payment' and self.service:
            return f"{self.transaction_type} of {self.amount} for {self.service.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            return f"{self.transaction_type} of {self.amount} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    transactions = models.ManyToManyField(Transaction, blank=True)

    def deposit(self, amount):
        if amount > 0:
            self.balance += Decimal(amount)
            transaction = Transaction(amount=amount, transaction_type="Deposit")
            transaction.save()
            self.transactions.add(transaction)
            self.save()
        else:
            raise ValueError("Amount must be > 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= Decimal(amount)
            transaction = Transaction(amount=amount, transaction_type="Withdrawal")
            transaction.save()
            self.transactions.add(transaction)
            self.save()
        else:
            raise ValueError(f"Cannot spend {amount}. Insufficient balance.")
    def check_balance(self):
        return self.balance
    


