from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from GameDB.forms import UserForm, UserProfileForm



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
    



#REGISTER CODE RIPPED FROM TANGO WITH DJANGO
def register(request):
    # registration logic here
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', 
                  context = {'user_form': user_form, 
                             'profile_form': profile_form, 
                             'registered': registered})
    

def account(request):
    return HttpResponse("This is the account page.")
    # return render(request, "05.html")

def search(request):
    search_kw = request.GET.get('kw')
    if search_kw:
        return HttpResponse(f"Search for: {search_kw}")
    else:
        return redirect("/")
    # return render(request, "06.html")

def categories(request):
    return HttpResponse("This is the categories page.")

def coming_soon(request):
    return render(request, 'coming_soon.html')

def about_us(request):
    return render(request, 'about_us.html')