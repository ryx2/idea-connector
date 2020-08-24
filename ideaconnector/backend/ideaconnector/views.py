from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View

from .models import Paragraph


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ideaconnector/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Paragraph.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
