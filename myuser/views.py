from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecionar para a página desejada após o registro
    else:
        form = UserRegistrationForm()
    return render(request, 'register_user.html', {'form': form})
