from django.db import models
from model_utils import Choices
from django.utils.translation import gettext as _


class Task(models.Model):
    STATUS_CHOICES = Choices(
        ('Draft', _('Draft')),
        ('Active',_('Active')),
        ('Done',_('Done')),
        ('Archived', _('Archived'))
    )
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.Draft, max_length=12)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.Title
