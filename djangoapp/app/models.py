from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    # Attributes of the posts (title, content, date posted)
    title = models.CharField(max_length=100, verbose_name='A Title to Describe Today')
    content = models.TextField(verbose_name='What Happened?')
    diary_image = models.ImageField(default='default.jpg', blank=True, upload_to='diary_images',
                                    verbose_name='A Memorable Pic!')
    # The date the post was created, pass the function timezone.now
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # Redirect when calling CreateView
    def get_absolute_url(self):
        return reverse('diary-log', kwargs={'pk': self.pk})


class Account(models.Model):
    # Creating the My Account page with profile pic
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)