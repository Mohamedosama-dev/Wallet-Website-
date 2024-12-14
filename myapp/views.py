from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import requests
import logging
import requests
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from .models import User, Wallet
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout,authenticate, login
from .models import Wallet, Charity, Transaction,User ,Service
from .forms import CharityTransferForm,ServicePaymentForm
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Wallet, Charity, Transaction
from .serializers import CharitySerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Service, Transaction
from .serializers import TransactionSerializer

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
import requests
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Wallet, Transaction
from .serializers import TransferSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User, Wallet, Transaction, Charity
from .serializers import UserSerializer, WalletSerializer, TransactionSerializer, CharitySerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Wallet, Transaction, Charity, Service  # Ensure you import your models
from .serializers import UserSerializer, WalletSerializer, TransactionSerializer, CharitySerializer, ServiceSerializer  # Ensure you import your serializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet, User, Transaction
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from .serializers import TransferSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal
from .models import Wallet, User, Transaction
from django.core.exceptions import ObjectDoesNotExist
# views.py
from django.shortcuts import render
from .serializers import CharityTransferSerializer, CharitySerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Wallet, Transaction, User
from .models import User, Wallet, Transaction

def home(request):
    return render(request, 'home.html')


def custom_logout(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        if User.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists')
            return redirect('sign_up')

        # Hash password and create user
        hashed_password = make_password(password)
        user = User(username=username, phone=phone, password=hashed_password)
        user.save()

        # Create wallet for new user
        Wallet.objects.create(user=user)

        messages.success(request, 'User created successfully')
        return redirect('sign_in')

    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid phone number or password')

    return render(request, 'sign_in.html')


@login_required
def show_transactions(request):
    try:
        wallet = Wallet.objects.get(user=request.user)
        deposit_withdrawal_transactions = wallet.transactions.filter(
            transaction_type__in=['Deposit', 'Withdrawal']
        )
        transfer_recharge_transactions = wallet.transactions.filter(
            transaction_type__in=['Transfer', 'Recharge Phone']
        )
        charity_transactions = wallet.transactions.filter(
            transaction_type='Charity'
        )
        service_payment_transactions = wallet.transactions.filter(
            transaction_type='Service Payment'
        )
    except Wallet.DoesNotExist:
        deposit_withdrawal_transactions = []
        transfer_recharge_transactions = []
        charity_transactions = []
        service_payment_transactions = []
      
        messages.error(request, 'Wallet not found. Please contact support.')

    return render(request, 'show_transactions.html', {
        'deposit_withdrawal_transactions': deposit_withdrawal_transactions,
        'transfer_recharge_transactions': transfer_recharge_transactions,
        'charity_transactions': charity_transactions,
        'service_payment_transactions': service_payment_transactions,  # Add this line
    })

@login_required
def dashboard(request):
    try:
        user_wallet = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        messages.error(request, 'Wallet not found. Please contact support.')
        return redirect('home')

    return render(request, 'dashboard.html', {'wallet': user_wallet})




@login_required
def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount <= 0:
                messages.error(request, 'Amount must be greater than zero.')
                return redirect('deposit')
            
            wallet = Wallet.objects.get(user=request.user)
            if wallet:
                wallet.deposit(amount)
                messages.success(request, 'Deposit successful.')
            else:
                messages.error(request, 'Wallet not found.')
        
        except (ValueError, InvalidOperation):
            messages.error(request, 'Invalid amount.')
    
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            wallet = Wallet.objects.get(user=request.user)
            if wallet.balance >= amount:
                wallet.withdraw(amount)
                messages.success(request, f'Withdrew {amount}. New balance: {wallet.balance}')
            else:
                messages.error(request, 'Insufficient balance')
        except (ValueError, InvalidOperation):
            messages.error(request, 'Invalid amount')
        except ObjectDoesNotExist:
            messages.error(request, 'Wallet not found')
        return redirect('dashboard')
    return render(request, 'withdraw.html')

@login_required
def view_user_info(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    return render(request, 'user_info.html', {'user': user, 'wallet': wallet})


@login_required
def transfer(request):
    if request.method == 'POST':
        target_phone = request.POST['target_phone']
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            source_wallet = Wallet.objects.get(user=request.user)
            target_user = User.objects.get(phone=target_phone)
            target_wallet = Wallet.objects.get(user=target_user)
            if source_wallet.balance >= amount:
                source_wallet.balance -= amount
                target_wallet.balance += amount
                source_wallet.save()
                target_wallet.save()

                # Log the transaction
                transfer_transaction = Transaction(
                    amount=amount,
                    transaction_type="Transfer",
                    phone_number=target_phone
                )
                transfer_transaction.save()
                source_wallet.transactions.add(transfer_transaction)
                target_wallet.transactions.add(transfer_transaction)
                
                messages.success(request, f'Transferred {amount} to {target_user.username}')
            else:
                messages.error(request, 'Insufficient balance')
        except (ValueError, InvalidOperation):
            messages.error(request, 'Invalid amount')
        except ObjectDoesNotExist:
            messages.error(request, 'User or wallet not found')
        return redirect('dashboard')
    return render(request, 'transfer.html')
@login_required
def pay_service(request):
    if request.method == 'POST':
        form = ServicePaymentForm(request.POST)
        if form.is_valid():
            service = form.cleaned_data['service']
            service_number = form.cleaned_data['service_number']
            amount = form.cleaned_data['amount']

            try:
                wallet = Wallet.objects.get(user=request.user)
                if wallet.balance >= amount:
                    wallet.balance -= amount
                    wallet.save()

                    # Create transaction for the service payment
                    transaction = Transaction(
                        amount=amount,
                        transaction_type="Service Payment",
                        service=service,
                        phone_number=service_number
                    )
                    transaction.save()
                    wallet.transactions.add(transaction)

                    # Respond to AJAX with success
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({'success': True, 'amount': amount, 'service_name': service.name})

                    messages.success(request, f'Successfully paid {amount} to {service.name}')
                else:
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({'error': 'Insufficient balance'})
                    messages.error(request, 'Insufficient balance')

            except Wallet.DoesNotExist:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'error': 'Wallet not found. Please ensure your account is set up correctly.'})
                messages.error(request, 'Wallet not found. Please ensure your account is set up correctly.')

            if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return redirect('dashboard')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Form is not valid', 'errors': form.errors})

    else:
        form = ServicePaymentForm()

    return render(request, 'pay_service.html', {'form': form})

@login_required
def transfer_to_charity(request):
    if request.method == 'POST':
        form = CharityTransferForm(request.POST)
        if form.is_valid():
            charity = form.cleaned_data['charity']
            amount = form.cleaned_data['amount']

            try:
                wallet = Wallet.objects.get(user=request.user)
                if wallet.balance >= amount:
                    wallet.balance -= amount
                    wallet.save()

                
                    transaction = Transaction(
                        amount=amount,
                        transaction_type="Charity",
                        charity=charity 
                    )
                    transaction.save()
                    wallet.transactions.add(transaction)  # Link the transaction to the wallet

                    messages.success(request, f'Successfully sent {amount} to {charity.name}')
                else:
                    messages.error(request, 'Insufficient balance')
            except Wallet.DoesNotExist:
                messages.error(request, 'Wallet not found')

            return redirect('dashboard')
    else:
        form = CharityTransferForm()

    return render(request, 'transfer_to_charity.html', {'form': form})


@login_required
def recharge_phone(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        target_phone = request.POST.get('target_phone')  # Get the phone number from POST data
        try:
            amount = Decimal(amount)
            if amount > 0:
                user = request.user
                wallet = Wallet.objects.get(user=user)

                if wallet.balance >= amount:
                    # Deduct from the wallet balance
                    wallet.balance -= amount
                    wallet.save()

                    # Add to the phone credit of the specified phone number
                    target_user = User.objects.get(phone=target_phone)
                    target_user.phone_credit += amount
                    target_user.save()

                    # Create a recharge phone transaction
                    transaction = Transaction(
                        amount=amount,
                        transaction_type="Recharge Phone",
                        phone_number=target_phone
                    )
                    transaction.save()
                    wallet.transactions.add(transaction)

                    messages.success(request, f'Recharged phone {target_phone} with {amount}. '
                                              f'New phone credit: {target_user.phone_credit}, '
                                              f'new wallet balance: {wallet.balance}')
                else:
                    messages.error(request, 'Insufficient wallet balance to recharge phone credit')
            else:
                messages.error(request, 'Amount must be greater than zero')
        except (ValueError, InvalidOperation):
            messages.error(request, 'Invalid amount')
        except User.DoesNotExist:
            messages.error(request, 'User with the specified phone number does not exist')

    return render(request, 'recharge_phone.html')  # Ensure we are rendering the same page
import requests


def currency_rates(request):
    api_key = '712d314c601acd45b28a3ae8'  # Your API key from ExchangeRate-API
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EGP"
    
    # Fetch the exchange rates from the API
    response = requests.get(url)
    rates = {}
    if response.status_code == 200:
        data = response.json()
        # Extracting conversion rates for EGP to other currencies
        rates['USD'] = 1 / data['conversion_rates']['USD']  # 1 USD to EGP
        rates['EUR'] = 1 / data['conversion_rates']['EUR']  # 1 EUR to EGP
        rates['GBP'] = 1 / data['conversion_rates']['GBP']  # 1 GBP to EGP
        rates['SAR'] = 1 / data['conversion_rates']['SAR']  # 1 SAR to EGP
        rates['KWD'] = 1 / data['conversion_rates']['KWD']  # 1 KWD to EGP
        rates['AED'] = 1 / data['conversion_rates']['AED']  # 1 AED to EGP
        rates['CAD'] = 1 / data['conversion_rates']['CAD']  # 1 CAD to EGP
        rates['AUD'] = 1 / data['conversion_rates']['AUD']  # 1 AUD to EGP
        rates['JPY'] = 1 / data['conversion_rates']['JPY']  # 1 JPY to EGP
        rates['CHF'] = 1 / data['conversion_rates']['CHF']  # 1 CHF to EGP
        rates['CNY'] = 1 / data['conversion_rates']['CNY']  # 1 CNY to EGP
        rates['INR'] = 1 / data['conversion_rates']['INR']  # 1 INR to EGP
    else:
        return render(request, 'currency_rates.html', {'error': 'Unable to fetch rates'})

    if request.method == "POST":
        amount = float(request.POST.get('amount', 0))
        selected_currency = request.POST.get('currency')

        # Convert the amount based on the selected currency
        if selected_currency in rates:
            converted_amount = amount / rates[selected_currency]
            return render(request, 'currency_rates.html', {
                'rates': rates,
                'converted_amount': converted_amount,
                'selected_currency': selected_currency,
            })
    
    return render(request, 'currency_rates.html', {'rates': rates})





from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings
import paypalrestsdk

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

def create_payment(request):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:8000/payments/execute/",
            "cancel_url": "http://localhost:8000/payments/cancel/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Wallet Balance Top-up",
                    "sku": "wallet_topup",
                    "price": "10.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "10.00",
                "currency": "USD"},
            "description": "Top up your wallet balance."}]})

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return redirect(approval_url) 
    else:
        print("Payment creation failed:", payment.error)
    return redirect('payment_error') 

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Payment successful
        return JsonResponse({"status": "Payment executed successfully!"})
    else:
        return JsonResponse({"status": "Payment failed", "error": payment.error})

def payment_cancel(request):
    return JsonResponse({"status": "Payment was cancelled."})

def payment_error(request):
    return JsonResponse({"status": "An error occurred during the payment process."})

import requests
from django.shortcuts import render
from django.conf import settings
def get_top_15_stocks(request):
    # Example famous stock symbols
    symbols = ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT",
                "META", "NVDA", "AMD", "NFLX", "BA", "INTC", 
                "IBM", "DIS", "V", 
                "PYPL","CSCO ","ORCL",
                "PEP","KO","T","PG","NKE","MCD ","JNJ","ADBE ","XOM ","WMT","VZ"]
    
    stock_data = []
    
    url = "https://finnhub.io/api/v1/quote"
    
    for symbol in symbols:
        params = {'symbol': symbol, 'token': settings.FINNHUB_API_KEY}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            stock_data.append({
                'symbol': symbol,
                'price': data['c'],
                'change': data['d'],
                'percent_change': data['dp']
            })
        else:
            stock_data.append({
                'symbol': symbol,
                'price': 'N/A',
                'change': 'N/A',
                'percent_change': 'N/A'
            })
    
    return render(request, 'stocks_table.html', {'stocks': stock_data})


logger = logging.getLogger(__name__)
class NearbyATMsView(View):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if not latitude or not longitude:
            return JsonResponse({'error': 'Latitude and Longitude are required'}, status=400)

        radius = 15000  # radius in meters

        overpass_url = "http://overpass-api.de/api/interpreter"
        overpass_query = f"""
            [out:json];
            node["amenity"="atm"](around:{radius},{latitude},{longitude});
            out;
        """
        try:
            response = requests.get(overpass_url, params={'data': overpass_query})
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch ATM data: {e}")
            return JsonResponse({'error': 'Failed to fetch ATM data', 'details': str(e)}, status=500)

        try:
            data = response.json()
            logger.info("JSON response received: %s", data)  # Log the full response
        except ValueError as e:
            logger.error(f"Invalid JSON response: {e}")
            return JsonResponse({'error': 'Invalid JSON response', 'details': str(e)}, status=500)

        atms = [
            {
                'id': element['id'],
                'lat': element['lat'],
                'lon': element['lon'],
                'operator': element.get('tags', {}).get('operator', 'N/A'),
                'brand': element.get('tags', {}).get('brand', 'N/A')
            }
            for element in data.get('elements', [])
            if element.get('tags', {}).get('amenity') == 'atm'
        ]

        if atms:
            return JsonResponse({'atms': atms})
        else:
            logger.info("No ATMs found near the provided location.")
            return JsonResponse({'message': 'No ATMs found near your location'}, status=404)

def map_view(request):
    return render(request, 'map.html')


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        # Create wallet for the new user
        Wallet.objects.create(user=user)

class SignInView(generics.GenericAPIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(phone=phone, password=password)
        if user:
            return Response({'message': 'Sign in successful', 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_400_BAD_REQUEST)


class DepositView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def post(self, request, user_id):
        amount = request.data.get('amount')
        
        try:
       
            amount = Decimal(amount)
            if amount <= 0:
                return Response({'message': 'Amount must be greater than zero.'}, status=status.HTTP_400_BAD_REQUEST)

            wallet = Wallet.objects.get(user_id=user_id)
            wallet.balance += amount  # Adding decimal values
            wallet.save()
            Transaction.objects.create(amount=amount, transaction_type='Deposit', wallet=wallet)
            return Response({'message': 'Deposit successful', 'new_balance': wallet.balance}, status=status.HTTP_200_OK)

        except Wallet.DoesNotExist:
            return Response({'message': 'Wallet not found.'}, status=status.HTTP_404_NOT_FOUND)
        except InvalidOperation:
            return Response({'message': 'Invalid amount.'}, status=status.HTTP_400_BAD_REQUEST)



class WithdrawView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def post(self, request, user_id):
        try:
            # Convert the amount to Decimal for consistency
            amount = Decimal(request.data.get('amount'))
            wallet = Wallet.objects.get(user_id=user_id)
            if wallet.balance >= amount:
                wallet.balance -= amount  # Subtracting decimal values
                wallet.save()
                Transaction.objects.create(amount=amount, transaction_type='Withdraw', wallet=wallet)
                return Response({'message': 'Withdraw successful', 'new_balance': wallet.balance})
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        except Wallet.DoesNotExist:
            return Response({'error': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)
        except InvalidOperation:
            return Response({'error': 'Invalid amount.'}, status=status.HTTP_400_BAD_REQUEST)
  


def user_info_api(request, pk):
    try:
        user = User.objects.get(pk=pk)
        wallet = Wallet.objects.get(user=user)


        user_data = {
            'username': user.username,
            'phone': user.phone,
            'phone_credit': user.phone_credit,
        }

        wallet_data = {
            'balance': wallet.balance,
        }

        return JsonResponse({'user': user_data, 'wallet': wallet_data})

    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Wallet.DoesNotExist:
        return JsonResponse({'error': 'Wallet not found'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class RechargePhoneView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def post(self, request):
        # Get the required data from the request
        user_id = request.data.get('user_id')  # ID of the user who wants to recharge
        amount = request.data.get('amount')  # Amount to recharge
        phone_number = request.data.get('target_phone')  # Phone number to recharge

        # Get the user's wallet
        wallet = get_object_or_404(Wallet, user_id=user_id)

      
        if wallet.balance >= amount:
    
            wallet.balance -= amount
            wallet.save()  
            
            # Record the transaction
            Transaction.objects.create(amount=amount, transaction_type='Recharge Phone', wallet=wallet)

            return Response({'message': 'Phone recharge successful', 'new_balance': wallet.balance})
        
        return Response({'error': 'Insufficient balance for recharge'}, status=status.HTTP_400_BAD_REQUEST)


class CheckBalanceAPIView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)  # Make sure this corresponds to your user model
            balance = user.wallet.balance  # Adjust based on how you're storing the balance
            return Response({'balance': balance}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)



class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(wallet__user_id=user_id)


@api_view(['POST'])
def service_pay_service(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    form = ServicePaymentForm(request.data)

    if form.is_valid():
        service = form.cleaned_data['service']
        service_number = form.cleaned_data['service_number']
        amount = form.cleaned_data['amount']

        try:
            wallet = Wallet.objects.get(user=request.user)
            if wallet.balance >= amount:
                wallet.balance -= amount
                wallet.save()

                # Create transaction for the service payment
                transaction = Transaction(
                    amount=amount,
                    transaction_type="Service Payment",
                    service=service,
                    phone_number=service_number
                )
                transaction.save()
                wallet.transactions.add(transaction)

                return Response({"success": f'Successfully paid {amount} to {service.name}'}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
        except Wallet.DoesNotExist:
            return Response({"detail": "Wallet not found. Please ensure your account is set up correctly."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@login_required
def check_balance(request, user_id):  
    try:
        wallet = Wallet.objects.get(user_id=user_id)  # Use user_id to fetch the wallet
        balance = wallet.balance
    except Wallet.DoesNotExist:
        balance = None  # Handle the error as needed

    return render(request, 'check_balance.html', {'balance': balance})


@api_view(['POST'])
def pay_service_api(request):
    try:
        wallet = Wallet.objects.get(user=request.user)  # Get the user's wallet
    except Wallet.DoesNotExist:
        return Response({'error': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)

    # Extract the service, service_number, and amount from the POST data
    service_id = request.data.get('service_id')
    service_number = request.data.get('service_number')
    amount = request.data.get('amount')

    if not service_id or not service_number or not amount:
        return Response({'error': 'Invalid input. Please provide service_id, service_number, and amount.'}, status=status.HTTP_400_BAD_REQUEST)

    # Fetch the service
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the wallet has enough balance
    if wallet.balance >= amount:
        wallet.balance -= amount
        wallet.save()

        # Create a transaction for the service payment
        transaction = Transaction.objects.create(
            wallet=wallet,
            amount=amount,
            transaction_type='Service Payment',
            service=service,
            phone_number=service_number
        )

        # Serialize the transaction to return as JSON
        transaction_serializer = TransactionSerializer(transaction)
        return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)


class TransferAPIView(APIView):
    def post(self, request):
        target_phone = request.data.get('recipient_phone_number')
        amount = request.data.get('amount')
        
        try:
            amount = Decimal(amount)
            # Get the sender's wallet
            source_wallet = Wallet.objects.get(user=request.user)

            # Get the target user and their wallet
            target_user = User.objects.get(phone=target_phone)
            target_wallet = Wallet.objects.get(user=target_user)

            # Ensure the source wallet has enough balance
            if source_wallet.balance >= amount:
                # Perform the transfer
                source_wallet.balance -= amount
                target_wallet.balance += amount
                source_wallet.save()
                target_wallet.save()

                # Log the transaction
                transfer_transaction = Transaction(
                    amount=amount,
                    transaction_type="Transfer",
                    phone_number=target_phone
                )
                transfer_transaction.save()
                source_wallet.transactions.add(transfer_transaction)
                target_wallet.transactions.add(transfer_transaction)

                # Return success message and new balance
                return Response({
                    'message': f'Transferred {amount} to {target_user.username}',
                    'new_balance': source_wallet.balance
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({'error': 'User or wallet not found'}, status=status.HTTP_404_NOT_FOUND)

        except (ValueError, Decimal.InvalidOperation):
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

class TransferToCharityView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CharityTransferSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        charity_id = serializer.validated_data['charity_id']
        amount = serializer.validated_data['amount']

       
        wallet = get_object_or_404(Wallet, user=user)

    
        charity = get_object_or_404(Charity, id=charity_id)

        if wallet.balance >= amount:
            wallet.balance -= amount
            wallet.save()

            # Create the transaction record
            transaction = Transaction(
                amount=amount,
                transaction_type="Charity",
                charity=charity,
                wallet=wallet
            )
            transaction.save()

            return Response({'message': 'Transfer to charity successful', 'new_balance': wallet.balance}, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Insufficient balance for charity transfer'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Service, Transaction
from .serializers import TransactionSerializer

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet, Transaction
from .serializers import TransferSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet, Transaction, User
from .serializers import TransferSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Wallet, Transaction
from .serializers import TransferSerializer


class TransferToCharityView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CharityTransferSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        charity_id = serializer.validated_data['charity_id']
        amount = serializer.validated_data['amount']

       
        wallet = get_object_or_404(Wallet, user=user)

    
        charity = get_object_or_404(Charity, id=charity_id)

        if wallet.balance >= amount:
            wallet.balance -= amount
            wallet.save()

            # Create the transaction record
            transaction = Transaction(
                amount=amount,
                transaction_type="Charity",
                charity=charity,
                wallet=wallet
            )
            transaction.save()

            return Response({'message': 'Transfer to charity successful', 'new_balance': wallet.balance}, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Insufficient balance for charity transfer'}, status=status.HTTP_400_BAD_REQUEST)
