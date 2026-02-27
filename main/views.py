from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def colleges(request):
    colleges = ['SVEW', 'VIT', 'BVRIT']
    return render(request, 'colleges.html', {'colleges': colleges})


@login_required(login_url='login')
def students(request):
    students = [
        {'sno': 1, 'name': 'meena', 'branch': 'IT', 'age': 20},
        {'sno': 2, 'name': 'neha', 'branch': 'ECE', 'age': 17},
        {'sno': 3, 'name': 'Ram', 'branch': 'AIDS', 'age': 90},
        {'sno': 4, 'name': 'sai', 'branch': 'MECH', 'age': 18},
    ]
    return render(request, 'students.html', {'students': students})
