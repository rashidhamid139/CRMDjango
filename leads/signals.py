from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    #
    if created:
        User.objects.create(user=instance)