from django.shortcuts import render, redirect
from django.contrib import messages
from payeregistration.models import PAYEAgent


def login_view(request):
    if request.method == 'POST':
        agent_id = request.POST.get('id')
        password = request.POST.get('password')
        if agent_id and password:
            try:
                agent = PAYEAgent.objects.get(payer_id=agent_id)
                if agent.check_password(password):
                    # Successful login
                    return redirect('dashboard')  # Redirect to a dashboard or home page
                else:
                    error_message = "Invalid password."
            except PAYEAgent.DoesNotExist:
                error_message = "Agent ID does not exist."
    else:
        error_message = None
    return render(request, 'login.html')