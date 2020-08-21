from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View

class Home(View):
    def get(self, request):
        render(request, "ideaconnector/index.html")
