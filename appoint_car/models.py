from django.db import models


# Create your models here.
class Driver(models.Model):
    car_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    status_choice = (
        (0, '未预约'),
        (1, '已预约'),
    )
    status = models.IntegerField(choices=status_choice, default=0)

    def __str__(self):
        return self.car_number


class User(models.Model):
    phone = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    appoint_time = models.CharField(max_length=50, default='0')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, blank=True, null=True)
    status_choice = (
        (0, '未分配'),
        (1, '已分配'),
    )
    status = models.IntegerField(choices=status_choice, default=0)

    def __str__(self):
        return self.name
