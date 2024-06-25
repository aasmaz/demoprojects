from django.shortcuts import render
from.models import Subscriber
from.forms import SubscriptionForm

def subscription_view(request):
    message = None
    message_type = None

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            action = form.cleaned_data['action']
            name = form.cleaned_data['name']

            if action == 'subscribe':
                if Subscriber.objects.filter(email=email).exists():
                    message = "You are already subscribed"
                    message_type = "error"
                else:
                    Subscriber.objects.create(email=email)
                    message = "Subscription successful!"
                    message_type = "success"
            elif action == 'unsubscribe':
                if Subscriber.objects.filter(email=email).exists():
                    Subscriber.objects.filter(email=email).delete()
                    message = "Unsubscription successful!"
                    message_type = "success"
                else:
                    message = "This email is not subscribed."
                    message_type = "error"

        return render(request, 'subscription.html', {'message': message, 'essage_type': message_type})
    return render(request, 'subscription.html')