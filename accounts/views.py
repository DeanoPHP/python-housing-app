from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        print('SUBMITTED SUCCESSFULLY')
        # Login user
        print('moo')
    else: 
        return render(request, 'accounts/login.html')
    
def register(request):
    if request.method == 'POST':
        # register user
        print('sup')
    else: 
        return render(request, 'accounts/register.html')
    
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
    
def logout(request):
    return redirect('index')
    