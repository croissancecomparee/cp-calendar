from django.db import models
import datetime

EVENT_TYPE_CHOICES = [
    ("smash","Smash"),
    ("mtg","MTG"),
    ("lorcana", "Lorcana"),
    ("street_fighter","Street Fighter"),
    ("rpg","RPG"),
    ("board_games","Jeux de sociétés"),
    ("other","Autre"),
]

RECURRING_RULES = [
    ("daily", "Quotidien"),
    ("weekly", "Hebdomadaire"),
    ("monthly", "Mensuel"),
    ("other", "Autre"),
]

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField()
    type= models.CharField(
        max_length=50,
        choices=EVENT_TYPE_CHOICES,
        default="other"
    )
    link = models.CharField(max_length=500, blank=True)
    is_recurring = models.BooleanField(default=False)
    recurrence_rule = models.CharField(
        max_length=50,
        choices = RECURRING_RULES,
        default = "other"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = (('title', 'date'),)

    def get_recurrences(self):
        """ generate the recurring occurences """
        occurrences = []
        if self.is_recurring:
            if self.recurrence_rule == 'weekly':
                current_date = self.date
                for i in range(10):
                    occurrences.append({
                        'id': self.id,
                        'title': self.title,
                        'start': current_date.strftime('%Y-%m-%d %H:%M:%S'),
                        'description': self.description,
                        'type': self.type,
                        'link': self.link,
                        'is_recurring': self.is_recurring,
                        'recurrence_rule': self.recurrence_rule,
                    })
                    current_date += datetime.timedelta(weeks=1)
            

            else:
                occurrences.append({
                    'id': self.id,
                    'title': self.title,
                    'start': self.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'description': self.description,
                })
            return occurrences