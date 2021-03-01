from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)


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


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('leads:leads')