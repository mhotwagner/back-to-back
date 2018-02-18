from django.db import models


# Create your models here.
class Calculation(models.Model):
    id = models.IntegerField(null=False, primary_key=True)

    @property
    def number(self):
        return self.id
