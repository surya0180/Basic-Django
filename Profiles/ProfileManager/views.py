from django.shortcuts import redirect, render
from ProfileManager.models import Stu
from .forms import FormsHash

def index(request):
    if request.method == 'POST':
        form = FormsHash(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = FormsHash()
    return render(request, 'index.html', {'DATA': form})

def profiles(request):
    Dr = Stu.objects.all()
    return render(request, 'profiles.html', {'DATA': Dr})
    




