from django.db import models


class Calculation(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    _occurrences = models.IntegerField(default=0)
    last_occurrence = models.DateTimeField(auto_now=True)

    @property
    def number(self):
        return self.id

    @property
    def occurrences(self):
        return self._occurrences

    def increment_occurrences(self):
        self._occurrences += 1

    @property
    def value(self):
        square_of_sum = sum(range(1, self.id + 1))**2
        sum_of_squares = sum([x**2 for x in range(1, self.id + 1)])
        return square_of_sum - sum_of_squares
