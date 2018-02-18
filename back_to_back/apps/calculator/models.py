from django.db import models


# Create your models here.
class Calculation(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    _occurrences = models.IntegerField(default=0)

    @property
    def number(self):
        return self.id

    @property
    def occurrences(self):
        return self._occurrences

    def increment_occurrences(self):
        self._occurrences += 1
