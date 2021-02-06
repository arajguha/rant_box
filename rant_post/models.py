from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class RantPost(models.Model):
    FEELING_CHOICES = [
        ('S', 'Sad'),
        ('VS', 'Very Sad'),
        ('N', 'Neutral'),
        ('P', 'Pissed'),
        ('EP', 'Extremely Pissed'),
        ('FF', 'Fucking Furious')
    ]

    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=2000, blank=False)
    feeling_level = models.CharField(max_length=3, choices=FEELING_CHOICES, default='N')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class PostReact(models.Model):
    post = models.ForeignKey(RantPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'(user: {self.user}, post: {self.post})'


class CategoryOption(models.Model):
    category_name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.category_name
