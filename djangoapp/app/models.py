from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    # Attributes of the posts (title, content, date posted, image, motivation)
    title = models.CharField(max_length=100, verbose_name='A Title Describing Today')
    content = models.TextField(verbose_name='What Happened?')
    motivation = models.CharField(max_length=100, verbose_name='One Thing Motivating You for Tomorrow',
                                  null=True, blank=True,
                                  help_text="It doesn't have to be something big, it can be an upcoming trip, "
                                            "looking at the sunrise, another episode of "
                                            "drama coming out, playing games till midnight "
                                            "or even listening to music on the way to work! "
                                            "Try to not leave this blank so you can look back at it one day!")
    diary_image = models.ImageField(default='default.jpg', blank=True, upload_to='diary_images',
                                    verbose_name='A Memorable Pic!')

    # The date the post was created, pass the function timezone.now
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # Redirect when calling CreateView and UpdateView
    def get_absolute_url(self):
        return reverse('diary-log', kwargs={'pk': self.pk})


class Account(models.Model):
    # Creating the My Account page with profile pic
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Overriding save method
        # To save new profile pic when updating
        super().save(*args, **kwargs)