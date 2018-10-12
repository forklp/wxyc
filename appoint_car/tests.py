from django.test import TestCase
from . import models
from django.shortcuts import render, HttpResponse
# Create your tests here.
def test(request):
    user = models.User.objects.all()[0]
    user.status = 1
    user.save()
    return HttpResponse(1)