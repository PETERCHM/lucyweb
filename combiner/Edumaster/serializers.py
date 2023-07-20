from rest_framework import serializers
from .models import UserProfile, Payment, Website

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'country', 'phone_number']
        read_only_fields = ['id', 'user']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'payment_method', 'timestamp']
        read_only_fields = ['id', 'user', 'timestamp']

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'name', 'url']
        read_only_fields = ['id']
