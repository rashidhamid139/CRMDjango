from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import User, Lead, Agent
from django.views.generic import (
    TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView )
from .forms import LeadForm, LeadModelForm
from django.contrib.auth.forms import UserCreationForm
from  . forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
#CRUD

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = 'leads/landing.html'

# Create your views here.
class LeadListView(LoginRequiredMixin,  ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, 'leads/lead_list.html', context)

class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:leads")

    def form_valid(self, form):
        send_mail(
            subject="Lead has been created",
            message="Go to site to see leads",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
def lead_create(request):
    print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:leads' )
    context  = {
        'form': form 
    }
    return render(request, 'leads/lead_create.html', context)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:leads')

def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead )
        if form.is_valid():
            form.save()
            return redirect('leads:lead_detail', pk=lead.id)
    context = {
        'lead': lead, 
        'form': form
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leads')
        
def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('leads:leads')