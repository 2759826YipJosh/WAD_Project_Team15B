from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from GameDB.forms import UserProfileForm



# Create your views here.


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
            return redirect('some-view-name')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')
    


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # Password is hashed here
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', 
                  context = {'user_form': user_form, 
                             'profile_form': profile_form, 
                             'registered': registered})


def account(request):
    return render(request, 'account.html')

def search(request):
    search_kw = request.GET.get('kw')
    if search_kw:
        return HttpResponse(f"Search for: {search_kw}")
    else:
        return redirect("/")
    # return render(request, "06.html")

def categories(request):
    return render(request, 'categories.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def about_us(request):
    return render(request, 'about_us.html')

def logout_view(request):
    logout(request)
    return redirect('/')