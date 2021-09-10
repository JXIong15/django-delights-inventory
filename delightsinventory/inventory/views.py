from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Owner, Patient, Appointment
# from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm, AppointmentCreateForm, AppointmentUpdateForm

# from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
#   context = {"name": request.user}
# return render(request, "inventory/home.html", context)
  return render(request, "inventory/home.html")