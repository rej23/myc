from django.db import models
# FIRST THING IMPORT THIS TO HELP FOR USER AUTHENTICATION SUCH AS CREATING AND MANAGING USER ACCOUNT
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model): # THIS IS TO CREATE A PLAYER MODEL/ DJANGO DATABASE
  
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')

    def __str__(self):
        return self.name


class Result(models.Model): # THIS IS TO CREATE THE RESULT MODEL/ DJANGO DATABASE
   
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name='score')
    bot_move = models.CharField(max_length=50, blank=True)
    user_move = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return 'Status -- ' + self.status + ' ' + self.player.name