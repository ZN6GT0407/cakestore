from django import forms
from.models import Profile, Order, Cake

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone']

class OrderForm(forms.ModelForm):
    cake = forms.ModelChoiceField(queryset=Cake.objects.all(), empty_label="Select Cake")

    class Meta:
        model = Order
        fields = ['cake', 'quantity']