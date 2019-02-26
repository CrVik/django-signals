from django.db.models.signals import pre_save
from django.dispatch import receiver
from bill.models import Payment


@receiver(pre_save, sender=Payment)
def my_handler(sender, **kwargs):
    print 'tet!'
    # assert False
