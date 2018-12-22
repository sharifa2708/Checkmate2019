from django.shortcuts import render, get_object_or_404, redirect
from .models import Team

def index(request):
    if not request.user.is_authenticated():
        render(request, 'base/index.html')
    render(request, 'mainapp:game')