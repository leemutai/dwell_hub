from django.shortcuts import render, redirect

from main_app.app_forms import UserForm, PropertyForm, ReviewForm, MessageForm, PaymentForm, AppointmentForm


# Create your views here.

def home(request):
    return render(request, 'index.html')


def properties(request):
    return render(request, 'properties.html')


def property_details(request):
    return render(request, 'property-details.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("user")
    else:
        form = UserForm()
    form = UserForm()
    return render(request, 'user.html', {"form": form})


def property(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("property")
    else:
        form = PropertyForm
    form = PropertyForm()
    return render(request, 'property.html', {"form": form})


def review(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("review")
    form = ReviewForm()
    return render(request, 'review.html', {"form": form})


def message(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("message")
    form = MessageForm()
    return render(request, 'message.html', {"form": form})


def appointment(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("appointment")
    form = AppointmentForm()
    return render(request, 'appointment.html', {"form": form})


def payment(request):
    if request.method == "POST":
        form = UserForm(request.POST), request.FILES
        if form.is_valid():
            form.save()
            return redirect("payment")
    form = PaymentForm()
    return render(request, 'payment.html', {"form": form})


def all_users(request):
    return None


def user_details(request):
    return None