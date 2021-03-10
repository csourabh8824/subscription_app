import json
import stripe
import djstripe

from django.views import View
from django.conf import settings
from djstripe.models import Product
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect

from .models import CustomUser


# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfilePage(View):
    '''
    It displays the prfile page after logging in.
    '''

    def get(self,request,*args, **kwargs):

        context={
            "products": Product.objects.all(),
            "publishable_key": settings.STRIPE_TEST_PUBLIC_KEY
        }
        return render(request,'login/profile_page.html',context)




@login_required(login_url='/')
def logout_view(request):
    #used to logout

    logout(request)
    return render(request,'logout/logout_page.html')



@login_required
def create_sub(request):
    
    if request.method == 'POST':
        # Reads application/json and returns a response
    
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )
        
            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
            request.user.customer = djstripe_customer
            

            # At this point, associate the ID of the Customer object with your
            # own internal representation of a customer, if you have one.
            print(111111111111111111111111,customer)

            # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                trial_period_days=7,
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            request.user.subscription = djstripe_subscription
            request.user.save()
            print(2222222222222222222,subscription)
            return JsonResponse(subscription)
        except Exception as e:
            print("here")
            return JsonResponse({'error': (e.args[0])}, status =403)
    else:
        print("here")
        return HttpResponse('request method not allowed')

@login_required
def complete(request):
    # this view render the template if subscription get completed.

    return render(request, "subscription/subscriptioncomplete.html")



