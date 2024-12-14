# serializers.py
from rest_framework import serializers
from .models import User, Wallet, Transaction, Charity ,Service # Import your models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone', 'password']  # Add necessary fields

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'timestamp']

from rest_framework import serializers
from .models import Charity

from rest_framework import serializers

class CharityTransferSerializer(serializers.Serializer):
    charity_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ['id', 'name', 'phone_number']



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service  # Replace with your actual Service model
        fields = '__all__' 



from rest_framework import serializers
from .models import Wallet, Transaction, User

class TransferSerializer(serializers.Serializer):
    target_phone = serializers.CharField(max_length=15)  # Assuming phone numbers are up to 15 characters
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self, data):
        user = self.context['request'].user  # Source user
        amount = data.get('amount')

        # Get the source user's wallet
        try:
            wallet = Wallet.objects.get(user=user)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError('Source wallet not found')

        if wallet.balance < amount:
            raise serializers.ValidationError('Insufficient balance')

        return data 


















# class TransferSerializer(serializers.Serializer):
#     sender_user_id = serializers.IntegerField()
#     recipient_phone_number = serializers.CharField()
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2)

#     def validate(self, data):
#         # Add validation logic, e.g., check if the sender exists and has enough balance
#         sender_wallet = Wallet.objects.filter(user_id=data['sender_user_id']).first()
#         if not sender_wallet:
#             raise serializers.ValidationError("Sender wallet does not exist.")
#         if sender_wallet.balance < data['amount']:
#             raise serializers.ValidationError("Insufficient balance.")
        
#         # Optionally, check if the recipient exists
#         # You can add additional checks if needed
        
#         return data