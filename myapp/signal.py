import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

# 1 Create a New Django Project:
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received synchronously")


# 2. Running in the Same Thread

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Thread ID: {threading.get_ident()}")