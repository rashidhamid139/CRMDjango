from django.urls import path
from . import views
app_name = 'agents'

urlpatterns = [
    path('', views.AgentsListView.as_view(), name='agents'),
    path('create/', views.AgentCreateView.as_view(), name='agent-create'),
]
