from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .EmailForm import EmailForm

BRANCH_EMAILS = {
    'CSE': 'csehod@gmail.com',
    'IT': 'ithod@gmail.com',
    'ECE': 'ecehod@gmail.com',
    'EEE': 'eeehod@gmail.com',
    'CIVIL': 'civilhod@gmail.com',
    'MECH': 'mechod@gmail.com'
}


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
@login_required(login_url='login')
def email(request):

    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            to_email = BRANCH_EMAILS.get(branch)

            full_message = f"Message from: {name}\nBranch: {branch}\n\n{message}"

            send_mail(
                subject,
                full_message,
                'reshmakalidindi13@gmail.com',
                [to_email],
                fail_silently=False,
            )

            return HttpResponse(
                f"<h2>Email sent to {branch} department successfully!</h2>"
            )

    else:
        form = EmailForm()

    return render(request, "mail_form.html", {"form": form})