import django_filters
from .models import Transaction, Wallet, Charity, User
from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    is_active = filters.BooleanFilter()
    phone_credit = filters.NumberFilter(field_name='phone_credit', lookup_expr='gte')
    phone_creditlte = filters.NumberFilter(field_name='phone_credit', lookup_expr='lte')
    username = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search for usernames

    class Meta:
        model = User
        fields = ['is_active', 'phone_credit', 'username']



class TransactionFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='timestamp', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'min_amount', 'max_amount', 'start_date', 'end_date']

class WalletFilter(django_filters.FilterSet):
    min_balance = django_filters.NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = django_filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = Wallet
        fields = ['min_balance', 'max_balance']


class CharityFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name='transaction__amount', lookup_expr='gte')

    class Meta:
        model = Charity
        fields = ['name']
