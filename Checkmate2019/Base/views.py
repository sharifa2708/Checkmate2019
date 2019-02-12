from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Member
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import Sign_up, LoginForm
from django.http import HttpResponse
from django.contrib import messages
from ipware import get_client_ip
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        #The url endpoint below needs to be updated after the game is made.
        return render(request, "Base/index.html", {})
    return render(request, "Base/index.html", {})

    
def sign_up(request):
    if request.method == 'POST':
        team_name = request.POST.get('teamname')
        # Next 2 lines are for Checking if the team_name has already been taken. This can be improved by using AJAX request (Frontend part)
        if User.objects.filter(username=team_name).exists():
            return HttpResponse("Sorry the Team Name has already been taken. Please try with some other team name")
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=team_name, password=password)
        user.save()
        id1 = request.POST.get('id1')
        id2 = request.POST.get('id2')
        ip = get_client_ip(request)
        team = Team(user=user,
                    ip_address=ip, score=0, puzzles_solved=0, rank=0)
        team.save()
        member1 = Member(id=id1, team=team)
        check_existence(request, id1) #If this bits id is registered with a team that has only one person, that team will be deleted. Otherwise nothing happens.
        member1.save()
        if id2:
            member2 = Member(id=id2, team=team)
            check_existence(request, id2)
            member2.save()
        messages.success(request, 'Team Successfully created!!')
        return redirect('/sign_in')
    else:
        form = Sign_up()
        return render(request, 'Base/sign_up.html')   


def sign_in(request):
    if request.method == 'POST':
        team_name = request.POST.get('teamname')
        password = request.POST.get('password')
        user = authenticate(
            username=team_name, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Successfully logged in .')
            # Base/index written below needs to be updated after the game is completed.
            return redirect('/game')
        else:
            messages.error(
                request, 'Login failed. Enter Correct Details .')
            return redirect('/sign_in')

    else:
        return render(request, 'Base/sign_in.html')

@login_required(login_url='/sign_in/')
def game(request):
    return render(request, "Base/main.html")


@login_required
def sign_out(request):
    # we need to add a function here that will invoke the function : position and will store the coordinates
    logout(request)
    return HttpResponse("You have been successfully logged out. We hope that you had a great time solving the puzzles. ")


@login_required
def leaderboard(request):
    leaderboard = Team.objects.order_by('rank')[:9]
    Leaderboard = enumerate([[team.user.username, team.score]
                             for team in leaderboard], 1)
    return render(request, 'Base/leaderboard.html', {'Leaderboard': Leaderboard})


#Checks if a member is in a particular team. If the member is already in a team that has just one member, the team is deleted. Otherwise nothing happens to the team.
def check_existence(request, bitsid):
    if Member.objects.filter(id=str(bitsid)).exists():
        current_member = Member.objects.filter(id = str(bitsid))[0]
        current_team = current_member.team
        list_of_members = current_team.Member.all()
        if len(list_of_members) == 2:
            pass
        else:
            current_team.delete()
    else:
        pass

@login_required
def score(request):
    if request.method=="POST":
        score = request.POST['score']
        user = Team.objects.get(user=request.user)
        user.score += int(score)
        user.save()
        return redirect("/score") # needs to be updated after frontend is done
    else:
        #remove this part later....Currently its here only for a visual interface
        return render(request, 'Base/score.html', {})

#in case the user logs out of the system or the system crashes this functions comes into picture
@login_required
def position(request):
    if request.method=="POST":
        # Needs to be updated after frontend is done. input is to be taken not as a form, but every time the system crashes ot user logs out
        x_coordinates = request.POST['x_coordinates']
        y_coordinates = request.POST['y_coordinates']
        user = Team.objects.get(user=request.user)
        user.x_coordinates = float(x_coordinates)
        user.y_coordinates = float(y_coordinates)
        user.save()
        return redirect("/position")
    else :
        return render(request, 'Base/position.html', {})
