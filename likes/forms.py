from django import forms
from .models import Like

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('user', 'track', 'like_date_time')