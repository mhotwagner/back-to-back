from django.db import models


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

    @property
    def value(self):
        sum_of_squares = sum([x**2 for x in range(1, self.id + 1)])
        square_of_sum = sum(range(1, self.id + 1))**2
        return sum_of_squares - square_of_sum
