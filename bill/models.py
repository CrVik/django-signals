# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import IntegerField

class Payment(models.Model):
    summ=IntegerField()

    