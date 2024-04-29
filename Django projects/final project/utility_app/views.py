from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponse
import requests
from forex_python.converter import CurrencyRates
from .forms import NoteForm, FeedbackForm
from .models import Notes
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            # Display error message using messages framework
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')  # Redirect back to login page
    else:
        return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def currency_converter(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    currencies = data['rates']
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']

        # Make API request to get exchange rate
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
        data = response.json()
        exchange_rate = data['rates'][to_currency]

        # Perform conversion
        converted_amount = round(amount * exchange_rate, 2)

        context = {
             'amount': amount,
             'from_currency': from_currency,
             'to_currency': to_currency,
             'converted_amount': converted_amount,
             'exchange_rate': exchange_rate,
             'currencies': currencies
            }
        return render(request, 'result.html', context)
    else:
        return render(request, 'converter.html', {'currencies': currencies})



def calculator_view(request):
    return render(request, 'calculator.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def new_notepad(request):
    user_notes = Notes.objects.filter(user=request.user)
    return render(request, 'new_notepad.html', {'notes': user_notes})

@login_required
def open_notepad(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'open_notepad.html', {'note' : note})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
            return redirect('new_notepad')
    else:
        form = NoteForm()
    return render(request, 'new_note.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('open_notepad', pk=pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('new_notepad')
    return render(request, 'confirm_delete_note.html', {'note': note})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_success.html')