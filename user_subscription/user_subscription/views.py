from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class HomeView(View):

    def get(self,request,*args, **kwargs):
        return render(request,'user_subscription/base.html')