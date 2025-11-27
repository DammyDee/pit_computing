from django.shortcuts import render, redirect
from django.contrib import messages
from payeproject.decorators import login_required
from payeregistration.models import PAYEAgent


def login_view(request):
    if request.method == 'POST':
        agent_id = request.POST.get('id')
        password = request.POST.get('password')
        if agent_id and password:
            try:
                agent = PAYEAgent.objects.get(payer_id=agent_id)
                if agent.check_password(password):
                    request.session['agent_id'] = agent.payer_id
                    return redirect('dashboard')  # Redirect to a dashboard or home page
                else:
                    error_message = "Invalid password."
                    messages.error(request, error_message)
            except PAYEAgent.DoesNotExist:
                error_message = "Agent ID does not exist."
                messages.error(request, error_message)
        else:
            error_message = "Please enter both Agent ID and password."
            messages.error(request, error_message)
    else:
        error_message = None
        messages.error(request, error_message)
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'payedashboard.html')