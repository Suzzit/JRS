from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login  # Import as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from .algo.tfidf import get_recommendation
def index(request):
    
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
             auth_login(request, user) 
             return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')




def process_data(request):
    # Define the demo data
    demo_data = "demo"

    # Pass the demo data to the template context
    context = {'demo': demo_data}
    return render(request, 'results.html', context)
