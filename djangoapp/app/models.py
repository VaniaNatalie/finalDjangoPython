from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #the date the post was created, pass the function timezone.now
    #author = models.ForeignKey(User, on_delete=models.CASCADE) #to delete posts if user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary-log', kwargs={'pk': self.pk})

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)