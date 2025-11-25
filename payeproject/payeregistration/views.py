from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import PAYEAgentForm

def registration(request):
    form = None  # Placeholder for form instance, e.g., PAYEAgentForm()
    if request.method == 'POST':
        form = PAYEAgentForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False) # Adjust as necessary to handle password hashing if needed
            agent.agent_password = make_password(form.cleaned_data['agent_password'])
            agent.save()
            return redirect('success')  # Redirect to a success page after registration
    else:
        form = PAYEAgentForm()
    return render(request, 'registration.html', {'form': form})

def success(request):
    return render(request, 'success.html')
