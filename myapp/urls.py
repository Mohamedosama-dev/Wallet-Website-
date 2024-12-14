from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import SignUpView, SignInView, DepositView, WithdrawView, RechargePhoneView, TransactionHistoryView
from .views import TransferAPIView
from django.urls import path
from .views import user_info_api
from django.urls import path
from .views import NearbyATMsView, map_view


from .views import service_pay_service  
from .views import check_balance, CheckBalanceAPIView
from .views import pay_service_api
from django.urls import path, include







urlpatterns = [
    
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('view_user_info/', views.view_user_info, name='view_user_info'),
    path('transfer/', views.transfer, name='transfer'),
    path('recharge_phone/', views.recharge_phone, name='recharge_phone'),
    path('currency-rates/', views.currency_rates, name='currency_rates'),
    path('show_transactions/', views.show_transactions, name='show_transactions'), 
    path('stocks/', views.get_top_15_stocks, name='get_top_15_stocks'),
    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/execute/', views.execute_payment, name='execute_payment'),
    path('payments/cancel/', views.payment_cancel, name='payment_cancel'),

    path('payment/error/', views.payment_error, name='payment_error'),
    path('nearby-atms/', NearbyATMsView.as_view(), name='nearby-atms'),
    path('map/', map_view, name='map'),
    path('logout/', views.custom_logout, name='logout'),
    path('transfer_to_charity/', views.transfer_to_charity, name='transfer_to_charity'),
    path('pay_service/', views.pay_service, name='pay_service'), 
    path('pay-service/', pay_service_api, name='pay-service-api'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('deposit/<int:user_id>/', DepositView.as_view(), name='deposit'),
    path('withdraw/<int:user_id>/', WithdrawView.as_view(), name='withdraw'),
    path('userinfo/<int:pk>/', user_info_api, name='user_info_api'),
    path('recharge/', RechargePhoneView.as_view(), name='recharge'), 
   
    path('transactions/<int:user_id>/', TransactionHistoryView.as_view(), name='transaction_history'),
    #path('api/transfer-to-charity/', TransferToCharityView.as_view(), name='transfer_to_charity'),
   
   

    path('check_balance/<int:user_id>/', check_balance, name='check_balance'),  # For rendering the HTML
    path('api/check_balance/<int:user_id>/', CheckBalanceAPIView.as_view(), name='check_balance'),
    path('api/transfer/', TransferAPIView.as_view(), name='api_transfer'),

   
    
]
