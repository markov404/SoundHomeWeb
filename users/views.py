
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["POST"])
def auth(request):
    return HttpResponse("O lala")
