from django.shortcuts import render
from .forms import ContactForm
from core.models import Profile

def contact(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., send email)
            # For now, just redirect or show success
            return render(request, 'contact/contact.html', {'form': ContactForm(), 'success': True, 'profile': profile})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'profile': profile})
