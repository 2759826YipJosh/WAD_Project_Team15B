from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction, IntegrityError
from .forms import RegisterForm, UpdateAccountForm
from .models import Game
import csv
from decimal import Decimal

def home(request):
    username = request.user.username
    return render(request, "home.html", {'username': username, 'path': request.path})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html', {'username': username,'path': request.path})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'path': request.path})

def update_account(request):
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        form = UpdateAccountForm(instance=request.user)
    return render(request, 'account.html', {'form': form, 'path': request.path})

def account(request):
    form = UpdateAccountForm(instance=request.user)
    username = request.user.username
    return render(request, 'account.html', {'username': username,'form': form, 'path': request.path})

def categories(request):
    username = request.user.username
    return render(request, 'categories.html', {'username': username,'path': request.path})

def coming_soon(request):
    username = request.user.username
    return render(request, 'coming_soon.html', {'username': username,'path': request.path})

def about_us(request):
    username = request.user.username
    return render(request, 'about_us.html', {'username': username,'path': request.path})

def logout_view(request):
    logout(request)
    return redirect('/')

def check_login(request):
    if request.user.username:
        return JsonResponse({'logged_in': True})
    return JsonResponse({'logged_in': False})

def import_csv_data():
    try:
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    with transaction.atomic():
                        price = row[6].replace('$', '') 
                        if not price.replace('.', '', 1).isdigit():
                            print(f"Invalid price for game: {row[0]}")
                            continue
                        game = Game(
                            name=row[0],
                            release_date=row[1],
                            category=row[2],
                            platforms_available=row[3],
                            developer=row[4],
                            publisher=row[5],
                            price=Decimal(price),  
                            average_rating=row[7],
                            age_restriction=row[8],
                            multiplayer=row[9] == 'True',
                            average_completion_time=row[10],
                            trailer_link=row[11],
                            image_link=row[12],
                            description=row[13]
                        )
                        game.save()
                except IntegrityError:
                    print(f"Failed to create game: {row[0]}")
    except FileNotFoundError:
        print("The file data.csv does not exist.")

def search(request):
    username = request.user.username
    query = request.GET.get('q')
    if query is not None:
        words = query.split()
        results = Game.objects.all()

        for word in words:
            results = results.filter(name__icontains=word)

        results = results[:1]
    else:
        results = Game.objects.none()  

    return render(request, 'search_results.html', {'username': username,'results': results, 'path': request.path})
