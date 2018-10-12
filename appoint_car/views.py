from django.shortcuts import render, HttpResponse
from . import models
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        time = request.POST['time']
        phone = request.POST['phone']
        address = request.POST['address']
        if models.User.objects.filter(phone=phone):
            temp = models.User.objects.get(phone=phone)
            temp.appoint_time = time
            temp.address = address
            temp.status = 0
            temp.save()
        else:
            models.User.objects.create(name=name, phone=phone, address=address, appoint_time=time)
        return render(request, 'repair_form.html', {'message': '预约成功'})
    return render(request, 'repair_form.html')

