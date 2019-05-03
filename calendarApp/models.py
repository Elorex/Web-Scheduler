import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

# needed for custom user profile fields
# retrieved from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Events(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    def create(cls, start, end, title, description):
        newEvent = cls(start=start, end=end, title=title, description=description)
        return newEvent


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #message sender
    text = models.TextField()           #long text without a limit
    sent = models.DateTimeField(default=timezone.now)  #message sent time

    def publish(self):
        self.sent = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
