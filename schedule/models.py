from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


EXAMINATION = 0
LABLESSON = 1
CEREMONY = 2


LESSON1 = 1
LESSON2 = 2
LESSON3 = 3
LESSON4 = 4
LESSON5 = 5
LESSON6 = 6
LESSON7 = 7
LESSON8 = 8
LESSON9 = 9
EVENT_CHOICES = ((EXAMINATION, _('Examination')),
                 (LABLESSON, _('Lab Lesson')),
                 (CEREMONY, _('Ceremony')))
TIME_CHOICES = ((LESSON1, _('1.LESSON(08.00)')),
                (LESSON2, _('2.LESSON(09.00)')),
                (LESSON3, _('3.LESSON(10.00)')),
                (LESSON4, _('4.LESSON(11.00)')),
                (LESSON5, _('5.LESSON(12.00)')),
                (LESSON6, _('6.LESSON(13.00)')),
                (LESSON7, _('1.LESSON(14.00)')),
                (LESSON8, _('2.LESSON(15.00)')),
                (LESSON9, _('3.LESSON(16.00)')))


class Event(models.Model):
    event_type = models.PositiveSmallIntegerField(
        default=0,
        help_text=_('Choose your event type'),
        choices=EVENT_CHOICES)
    title = models.CharField(
        max_length=255,
        default="",
        help_text=_('Enter a name for your event'))
    content = models.TextField(
        blank=True,
        null=True,
        help_text=_('Not necessary,'
                    'if you want to explain your event you can use here.'))
    user = models.ForeignKey(User)
    created_time = models.DateTimeField(editable=True, auto_now_add=True)
    date = models.DateField()
    time = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("Choose a time for your event"),
        choices=TIME_CHOICES)

    class Meta:
        ordering = ('time', )
