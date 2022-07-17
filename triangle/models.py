from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    email = models.EmailField()

    def __str__(self):
        return self.last_name


class Logs(models.Model):
    path = models.CharField(max_length=300, verbose_name='Path')
    request_method = models.CharField(max_length=50, verbose_name='Request method')
    form_data = models.JSONField(verbose_name='Form data')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path
