from django.db import models

class Event(models.Model):
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    title = models.CharField(max_length=50)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")

    def __str__(self):
        return self. title

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
