from django import forms

from main_app.models import User, Property, Review, Message, Payment, Appointment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date", "min": "2023-11-25", "max": "2024-01-01"})
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            "amount": forms.NumberInput(attrs={"max": 50000, "min": 5000}),
            " payment_date": forms.DateInput(attrs={"type": "date", "min": "2023-11-25", "max": "2024-01-01"})
        }
