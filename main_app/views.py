from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import UserForm, PropertyForm, ReviewForm, MessageForm, PaymentForm, AppointmentForm, LoginForm
from main_app.models import User


# Create your views here.
@login_required
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
            messages.info(request, "User was saved")
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


@login_required
def all_users(request):
    user = User.objects.all()
    # user = User.objects.filter(user_type="landlord")
    # user = User.objects.filter(user_type="student")
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_users.html', {"user": data})


@login_required
def user_details(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'user_details.html', {"user": user})


@login_required
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.warning(request, "The user was deleted permanently")
    return redirect("all")


def search_users(request):
    search_word = request.GET.get("search_word")
    user = User.objects.filter(
        Q(username__icontains=search_word) | Q(email__icontains=search_word)
    )
    paginator = Paginator(user, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_users.html', {"user": data})


@login_required
def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)  # SELECT * FROM user WHERE id=1
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully")
            return redirect('details', user_id)
    else:
        form = UserForm(instance=user)
    return render(request, 'update.html', {"form": form})


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('user')
        messages.error(request, "Wrong username or password")
        return render(request, "login.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')
