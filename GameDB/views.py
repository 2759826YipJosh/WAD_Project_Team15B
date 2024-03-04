from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



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

def register_view(request):
    # registration logic here
    pass

def index(request):
    return render(request, 'index.html')

def about_us_view(request):
    return render(request, 'about_us.html')



