import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(_("Question text"), max_length=200)
    pub_date = models.DateTimeField(_("Published date"))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_this_year(self):
        current_year = timezone.now().year
        return self.pub_date.year == current_year

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey("Question", verbose_name=_("Question"), on_delete=models.CASCADE)
    choice_text = models.CharField(_("Choice text"), max_length=200)
    votes = models.IntegerField(_("Votes"), default=0)

    def __str__(self) -> str:
        return self.choice_text
