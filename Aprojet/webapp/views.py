# THIS NEEDS TO BE IMPORTED BEFORE THE CODE BELOW CAN RUN


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Player, Result
from django.shortcuts import render, redirect

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
        return redirect('new') #THIS CODE IS USE TO REDIRECT TO THE GAME URL PATH. #url.py to set the path

    return render(request, "index.html.html")




def new(request):
    
    return render(request, "game_record.html" )