# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class BillConfig(AppConfig):
    name = 'bill'
    verbose_name = "Tasks"

    def ready(self):
        from bill.signals import handlers
