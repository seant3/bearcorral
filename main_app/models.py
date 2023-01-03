from django.db import models
from django.urls import reverse
from datetime import date

SIZE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0])
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Bear(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bear_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= 1


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    bear = models.ForeignKey(Bear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
     # change the default sort
    class Meta:
        ordering = ['date']