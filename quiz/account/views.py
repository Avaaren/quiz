from django.shortcuts import render

from .forms import UserForm
from .models import Profile


def registration(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            return render(request,
                          'account/registration_done.html',
                          {'user': user})
    else:
        form = UserForm()
    return render(request,
                  'account/registration.html',
                  {'form': form})
