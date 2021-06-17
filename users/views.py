from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Output blank registration form.
        form = UserCreationForm()
    else:
        # Processing the filled form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid:
            new_user = form.save()
            # Log in and redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Render blank or incorrect form.
    context = {'form': form}
    return render(request, 'users/register.html', context)
