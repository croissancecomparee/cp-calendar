from django.db import models

EVENT_TYPE_CHOICES = [
    ("smash","Smash"),
    ("mtg","MTG"),
    ("street_fighter","Street Fighter"),
    ("rpg","RPG"),
    ("board_games","Jeux de sociétés"),
    ("other","Autre"),
]

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    organizer = models.CharField(max_length=100)
    type= models.CharField(
        max_length=50,
        choices=EVENT_TYPE_CHOICES,
        default="other"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = (('title', 'date'),)