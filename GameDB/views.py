from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from GameDB.forms import UserForm, UserProfileForm





def login_view(request):
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
def register_view(request):
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
    
    
    

def index(request):
    return render(request, 'index.html')

def about_us_view(request):
    return render(request, 'about_us.html')



