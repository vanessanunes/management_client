from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def logout(request):
    request.user.logout()
    return redirect('home')
