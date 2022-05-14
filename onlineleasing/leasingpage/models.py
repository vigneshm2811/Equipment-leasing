from django.db import models

class lessor(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

class lesse(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

class container(models.Model):
    container_id = models.IntegerField
    container_type = models.CharField(max_length=30)
    container_history = models.CharField(max_length=30)
    rate = models.IntegerField(default=0)

class leasinglist(models.Model):
    fk = models.ForeignKey(container, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    containers_id = models.IntegerField(default=0)
    years = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)


