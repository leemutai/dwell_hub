from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import UserForm, PropertyForm, ReviewForm, MessageForm, PaymentForm, AppointmentForm
from main_app.models import User


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
    return render(request, 'forms/user.html', {"form": form})


def property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("property")
    else:
        form = PropertyForm
    form = PropertyForm()
    return render(request, 'forms/property.html', {"form": form})


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("review")
    form = ReviewForm()
    return render(request, 'forms/review.html', {"form": form})


def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("message")
    form = MessageForm()
    return render(request, 'forms/message.html', {"form": form})


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("appointment")
    form = AppointmentForm()
    return render(request, 'forms/appointment.html', {"form": form})


def payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST), request.FILES
        if form.is_valid():
            form.save()
            return redirect("payment")
    form = PaymentForm()
    return render(request, 'forms/payment.html', {"form": form})


def all_users(request):
    user = User.objects.all()
    # user = User.objects.filter(user_type="landlord")
    # user = User.objects.filter(user_type="student")
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_users.html', {"user": data})


def user_details(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user_details.html', {"user": user})


def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect("all")


def search_users(request):
    search_word = request.GET["search_word"]
    user = User.objects.filter(
        Q(username__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(user, 10)
    page_number = request.GET("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_users.html', {"user": data})
