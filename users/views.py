from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.post)

        if form.is_valid():
            return redirect('/success/')
    form = UserCreationForm()
    return render(req, 'users/register.html', {'form': form})
