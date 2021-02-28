from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Lead, Agent
# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(pk=pk)
    print(lead)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)
