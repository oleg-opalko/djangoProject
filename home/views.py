
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation

from djangoProject import settings

# Create your views here.

def index(request):
    return render(request, 'home.html')

def set_language(request):
    language = request.GET.get('language', settings.LANGUAGE_CODE)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    translation.activate(language)
    return response