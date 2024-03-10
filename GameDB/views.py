from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateAccountForm
from django.contrib import messages
from .models import Game, Review



def home(request):
    username = request.user.username
    
    return render(request, "home.html", {'username': username})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to a login page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def update_account(request):
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        form = UpdateAccountForm(instance=request.user)
    return render(request, 'account.html', {'form': form})

def account(request):
    form = UpdateAccountForm(instance=request.user)
    return render(request, 'account.html', {'form': form})


def search(request):
    search_kw = request.GET.get('kw')
    if search_kw:
        return HttpResponse(f"Search for: {search_kw}")
    else:
        return redirect("/")
    # return render(request, "06.html")

def categories(request):
    if request.method == 'POST' and request.user.is_superuser:
        category_form = AddCategoryForm(request.POST)
        game_form = AddGameForm(request.POST)
        if category_form.is_valid():
            category_form.save()
        if game_form.is_valid():
            game_form.save()
        return redirect('categories')
    else:
        category_form = AddCategoryForm()
        game_form = AddGameForm()
    return render(request, 'categories.html', {'category_form': category_form, 'game_form': game_form})

def coming_soon(request):
    return render(request, 'coming_soon.html')

def about_us(request):
    return render(request, 'about_us.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def chosen_game(request, gameID):
    # game = Game.objects.get(pk=gameID)
    game = {'videoName': 'deadcells.mp4', 
            'pictureName': 'deadcells.jpg', 
            'description': """
                Dead Cells is a rogue-lite, Castlevania-inspired action-platformer, allowing you to explore a sprawling, ever-changing castle… assuming you're able to fight your way past its keepers.
                To beat the game, you'll have to master 2D "souls-lite combat" with the ever-present threat of permadeath looming. No checkpoints. Kill, die, learn, repeat.
            """}
    game['description'] = game['description'].splitlines()
    return render(request, 'chosen_game.html', {'game': game})


def check_login(request):
    if request.user.username:
        return JsonResponse({'logged_in': True})
    return JsonResponse({'logged_in': False})