# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from lungColonApp.forms import CustomUserCreationForm, AppointmentForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from LungColonClassifier.pipeline.prediction import PredictionPipeline
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import PatientRecords, Appointment

media = "media"
import os


def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data["appointment_date"]
            # Check if the date is available
            if not Appointment.objects.filter(
                appointment_date=appointment_date, is_booked=True
            ).exists():
                form.save()
                return redirect("home")
            else:
                return render(
                    request,
                    "404.html",
                    {"error_message": "Appointment date is not available."},
                )
    else:
        form = AppointmentForm()
    return render(request, "appointment.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Hash the password using make_password
            password = make_password(form.cleaned_data["password"])

            # Create a new user instance with the hashed password
            user = User.objects.create(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=password,
            )
            user.save()
            messages.success(
                request, "You have successfully registered. Please log in."
            )
            return redirect("signIn/")

        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def signIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


@login_required
def customer_logout_view(request):
    logout(request)
    return redirect("home")


# Create your views here.
def index(request):
    return render(request, "index.html")


def results(request):
    record = PatientRecords.objects.last()
    context = {"record": record}
    return render(request, "results.html", context)


@login_required(login_url="/signUp/")
def upload(request):
    if request.method == "POST" and request.FILES["upload"]:
        f = request.FILES["upload"]
        fss = FileSystemStorage()
        file = fss.save(f.name, f)
        file_url = fss.url(file)
        pred_img = os.path.join(media, file)
        pred = PredictionPipeline(pred_img)
        class_name, conf = pred.makePrediction()
        patient = request.user
        record = PatientRecords.objects.create(
            patient=patient, image=f, pred_class=class_name, score=conf
        )
        record.save()

        return redirect("results")

    return render(request, "upload.html")


@login_required(login_url="/signUp/")
def dashboard(request):
    records = PatientRecords.objects.all().order_by("-date_added")
    context = {"records": records}
    return render(request, "dashboard.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = ContactForm()

    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")
