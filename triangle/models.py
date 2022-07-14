# from django.contrib import admin
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    email = models.EmailField()

    def __str__(self):
        return self.last_name

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently?',
    # )
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
