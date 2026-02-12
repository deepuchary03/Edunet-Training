from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Agent
from .serializer import AgentSerializer


def home(request):
    agents = Agent.objects.all()
    return render(request, "home.html", {"agents": agents})


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    

