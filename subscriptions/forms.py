from django import forms
from .models import SubscriptionPlan, UserSubscription

class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = ('name', 'price', 'description')

class UserSubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserSubscription
        fields = ('user', 'subscription_plan', 'start_date', 'end_date')