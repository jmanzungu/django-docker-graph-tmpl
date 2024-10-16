from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            return JsonResponse({'message': 'User registered successfully!'})
        else:
            return JsonResponse({'message': 'Passwords do not match!'})
    return render(request, 'register.html')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful!'})
        else:
            return JsonResponse({'message': 'Invalid credentials!'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully!'})

