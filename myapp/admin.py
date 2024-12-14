from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import User, Wallet, Transaction, Charity,Service
from django.db.models import Count
from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import User, Wallet, Transaction, Charity, Service
from django.contrib.auth.models import  Group
# Unregister the Group model (used for authorization groups)
admin.site.unregister(Group)

class DateRangeFilter(admin.SimpleListFilter):
    title = 'Date Range'
    parameter_name = 'date_range'

    def lookups(self, request, model_admin):
        return (
            ('last_7_days', 'Last 7 days'),
            ('last_30_days', 'Last 30 days'),
            ('this_month', 'This month'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'last_7_days':
            return queryset.filter(timestamp__gte=timezone.now() - timedelta(days=7))
        if self.value() == 'last_30_days':
            return queryset.filter(timestamp__gte=timezone.now() - timedelta(days=30))
        if self.value() == 'this_month':
            return queryset.filter(timestamp__month=timezone.now().month)
        return queryset

# Custom filter for phone credit
class PhoneCreditFilter(admin.SimpleListFilter):
    title = 'Phone Credit'
    parameter_name = 'phone_credit'

    def lookups(self, request, model_admin):
        return (
            ('greater_than_25', 'Greater than 25'),
            ('greater_than_50', 'Greater than 50'),
            ('greater_than_100', 'Greater than 100'),
            ('greater_than_200', 'Greater than 200'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'greater_than_25':
            return queryset.filter(phone_credit__gt=25)
        if self.value() == 'greater_than_50':
            return queryset.filter(phone_credit__gt=50)
        if self.value() == 'greater_than_100':
            return queryset.filter(phone_credit__gt=100)
        if self.value() == 'greater_than_200':
            return queryset.filter(phone_credit__gt=200)
        return queryset

# Custom filter for wallet balance
class BalanceFilter(admin.SimpleListFilter):
    title = 'Balance'
    parameter_name = 'balance'

    def lookups(self, request, model_admin):
        return (
            ('greater_than_500', 'Greater than 500'),
            ('greater_than_1000', 'Greater than 1000'),
            ('greater_than_2000', 'Greater than 2000'),
            ('greater_than_3000', 'Greater than 3000'),
            ('greater_than_5000', 'Greater than 5000'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'greater_than_500':
            return queryset.filter(balance__gt=500)
        if self.value() == 'greater_than_1000':
            return queryset.filter(balance__gt=1000)
        if self.value() == 'greater_than_2000':
            return queryset.filter(balance__gt=2000)
        if self.value() == 'greater_than_3000':
            return queryset.filter(balance__gt=3000)
        if self.value() == 'greater_than_5000':
            return queryset.filter(balance__gt=5000)
        return queryset

# Custom filter for transaction types
class TransactionTypeFilter(admin.SimpleListFilter):
    title = 'Transaction Type'
    parameter_name = 'transaction_type'

    def lookups(self, request, model_admin):
        return (
            ('Deposit', 'Deposit'),
            ('Withdrawal', 'Withdrawal'),
            ('Transfer', 'Transfer'),
            ('Recharge Phone', 'Recharge Phone'),
            ('Charity', 'Charity Transfer'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(transaction_type=self.value())
        return queryset

# Custom filter for charity amounts
class CharityAmountFilter(admin.SimpleListFilter):
    title = 'Amount Filter'
    parameter_name = 'amount'

    def lookups(self, request, model_admin):
        return (
            ('greater_than_1000', 'Greater than 1000'),
            ('greater_than_2000', 'Greater than 2000'),
            ('greater_than_5000', 'Greater than 5000'),
            ('greater_than_10000', 'Greater than 10000'),
            ('greater_than_20000', 'Greater than 20000'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'greater_than_1000':
            return queryset.filter(transaction__amount__gt=1000)
        if self.value() == 'greater_than_2000':
            return queryset.filter(transaction__amount__gt=2000)
        if self.value() == 'greater_than_5000':
            return queryset.filter(transaction__amount__gt=5000)
        if self.value() == 'greater_than_10000':
            return queryset.filter(transaction__amount__gt=10000)
        if self.value() == 'greater_than_20000':
            return queryset.filter(transaction__amount__gt=20000)
        return queryset

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_number')
    search_fields = ('name', 'service_number')

# Function to create initial data
@receiver(post_migrate)
def create_initial_services(sender, **kwargs):
    if sender.name == 'myapp':  # Replace 'myapp' with your actual app name
        # Create services if they do not exist
        services_data = [
            {'name': 'Electricity', 'service_number': '12345'},
            {'name': 'Gas', 'service_number': '67890'},
            {'name': 'Water', 'service_number': '54321'},
        ]
        for service in services_data:
            Service.objects.get_or_create(**service)

# User admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'is_active', 'phone_credit')
    list_filter = ('is_active', PhoneCreditFilter)
    search_fields = ('username', 'phone')

# Wallet admin
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_filter = (BalanceFilter,)
    search_fields = ('user__username', 'balance')

# Transaction admin
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'transaction_type', 'service_name', 'charity_name', 'phone_number', 'timestamp')
    list_filter = ('transaction_type', DateRangeFilter, 'charity', TransactionTypeFilter)
    search_fields = ('phone_number', 'charity__name', 'service_name')

    def charity_name(self, obj):
        return obj.charity.name if obj.charity else 'N/A'
    charity_name.admin_order_field = 'charity'
    charity_name.short_description = 'Charity Name'

    def service_name(self, obj):
        return obj.service.name if obj.service else 'N/A'
    service_name.admin_order_field = 'service'
    service_name.short_description = 'Service Name'

# Charity admin
@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'total_amount_received')
    list_filter = (CharityAmountFilter, 'name')
    search_fields = ('name', 'phone_number')

    def total_amount_received(self, obj):
        total_amount = Transaction.objects.filter(charity=obj).aggregate(total=Sum('amount'))['total']
        return total_amount or '0.00'
    total_amount_received.admin_order_field = 'total_amount_received'
    total_amount_received.short_description = 'Total Amount Received'

# Function to create initial charities
@receiver(post_migrate)
def create_initial_charities(sender, **kwargs):
    if sender.name == 'myapp':  # Replace 'myapp' with your actual app name
        charities_data = [
            {"name": "Magdi Yacoub", "phone_number": "9698"},
            {"name": "Children's Cancer Hospital", "phone_number": "57357"},
            {"name": "Orman", "phone_number": "990"},
            {"name": "Egyptian Red Crescent", "phone_number": "911111"},
            {"name": "Mersal Charitable", "phone_number": "19340"},
            {"name": "Egyptian Food Bank", "phone_number": "16060"},
            {"name": "Baheya Hospital", "phone_number": "6666 6666"},
            {"name": "Misr Al Khair", "phone_number": "7000"},
            {"name": "Resala", "phone_number": "9599"},
            {"name": "New National Cancer Institute", "phone_number": "500500"},
        ]
        for charity in charities_data:
            Charity.objects.get_or_create(**charity)
