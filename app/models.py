from django.db import models
from django.contrib.auth.models import User

class Computer(models.Model):
    computer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    system_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Computer")
        verbose_name_plural = ("Computers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("computer_detail", kwargs={"pk": self.pk})

class Instance(models.Model):
    instance_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Instance")
        verbose_name_plural = ("Instances")

    def __str__(self):
        return self.instance_id

    def get_absolute_url(self):
        return reverse("instance_detail", kwargs={"pk": self.pk})