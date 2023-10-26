# THIS NEEDS TO BE IMPORTED BEFORE THE CODE BELOW CAN RUN


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Player, Result
from django.shortcuts import redirect
import random


import logging
log = logging.getLogger(__name__)
# Create your views here.
# THIS IS THE FIRST FUNCTION def home <CALL THIS URL path('',views.home, name='home'),>


def home(request):
    if request.method=='POST': #THIS IS FROM THE FORM ACTION IN INDEX.HTML THIS MEANS IF THE USER CLICK SUBMIT!
        playername = request.POST.get('name') #playername is a variable = THIS COMMAND is used to retrieve the value of the name field
        if User.objects.filter(username__iexact=playername): #IF THIS USER NAME IS EXISTING = THE MESSAGE BELOW
            messages.warning(request, 'This name is already exists, please try another one.') #THIS MESSAGE NEED A MESSAGE ALERT ON THE INDEX.HTML PAGE
            return HttpResponseRedirect(request.path_info) #THIS CODE REDIRECT THE USER TO THE SAME PAGE IF THE NAME ALREADY EXIST
        create_user = User.objects.create(first_name=playername, username=playername) #create_user is a variable = THIS COMMAND is use to create user in django
        create_player = Player.objects.create(name=playername, user=create_user) #CREATE_PLAYER is a variable FIRSTLY IMPORT PLAYER FROM MODEL =

# WHAT IS THE DIFFERENT BETWEEN USER AND PLAYER
# THE USER MODEL IS A BUILD-IN MODEL IN DJANGO / USE FOR AUTHENTICATION AND AUTHORIZATION E.G the second if command.
# WHILE THE PLAYER IS CUSTOM MODEL TO REPRESENT A PLAYER IN A GAME / USE FOR STORING PLAYER INFORMATION EG score.

        return redirect('thegame') #THIS CODE IS USE TO REDIRECT TO THE GAME URL PATH. #url.py to set the path
    return render(request, "index.html.html")

def thegame(request):

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user = Player.objects.all().last() #THIS IS THE RETRIVE THE DETAIL OF THE LAST PLAYER CREATED


    if request.method == 'POST':
        user_action = request.POST.get('name')
        if computer_action == user_action:
            messages.info(request, f'IT WAS A TIE TRY AGAIN')
            result = Result.objects.create(player=user, bot_move=computer_action, status='Tie', user_move=user_action)
            log.debug("Both players selected. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                messages.success(request,f"Rock smashes scissors! You win!")
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Win')
                log.debug("players selected Rock. Rock smashes scissors! You win!")
            else:
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Lose')
                messages.info(request, f"Paper covers rock! You lose.")
                log.debug("paper cover rock. You Lose!")

        elif user_action == "paper":
            if computer_action == "rock":
                messages.success(request,f"paper cover rock. You Win!")
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Win')
                log.debug("players selected Paper. paper cover rock. You Win!")
            else:
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Lose')
                messages.info(request, f"Scissors cuts paper! You lose.")
                log.debug("Scissors cuts paper! You lose!")

        elif user_action == "scissors":
            if computer_action == "paper":
                messages.success(request,f"Scissors cuts paper! You win!")
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Win')
                log.debug("players selected Paper. paper cover rock. You Win!")
            else:
                result = Result.objects.create(player=user, bot_move=computer_action, user_move=user_action, status='Lose')
                messages.info(request, f"Rock smashes scissors! You lose.")
                log.debug("Rock smashes scissors! You lose.")



    return render(request, "thegame.html" , {'user':user}) 

def new(request):
    res = Result.objects.all().order_by('-id')
    context = {'res' :res}
    return render(request, "game_record.html", context ) 


    
    