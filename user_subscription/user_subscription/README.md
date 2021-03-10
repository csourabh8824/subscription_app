# User registration and Stripe Integration

User registration is managed by Django.Stripe is a payment infrastructure for the internet.

## Clone repo using command:

```bash
git clone https://github.com/csourabh8824/subscription_app.git
```

## Create Virtual environment and install:
```
Django==2.2
django-registration==3.1.1
mysqlclient==2.0.3
stripe==2.56.0
```
## Stripe account
1. Create account on stripe and then copy your publishable and secret key from Developers Api keys section.
2. In your Django settings.py Configure publishable keys and Secret Key.
3. In profile_page.html, setup your own publishable key in Stripe function.
4. Create products on stripe account. 



## Djstripe
djstripe is used to get all the products that have been created by you

## Install Djstripe
```
pip install dj-stripe
python manage.py djstripe_sync_plans_from_stripe
``` 

## Run migration commands and createsuperuser for setting up  database:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
## Run the Server using below command and then navigate to the [link](http://127.0.0.1:8000/)
```
python manage.py runserver
```

## Usage
After Navigating to the web, the homepage will get rendered, where you have to register first. Then ,You will be logged in immediately to your profile page.  

At profile page you'll see the products you have created then you can select any one product.  

Next step is a payment, To test you can use card number 4242 4242 4242 4242 then you can choose any cvv and 5 digit pin code.  

Finally, you're done and then click on subscribe button. It will take few seconds and will navigate to completion page. Where it will tell you that your payment is successful and it will also shows the trial ends date.   

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


