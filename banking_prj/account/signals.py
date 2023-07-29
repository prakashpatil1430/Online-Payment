from userauths.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account


@receiver(post_save, sender=User)
def create_bank_account_for_new_user(sender, instance, created, **kwargs):
    if created:
        # Create an account for the new user
        Account.objects.create(user=instance)