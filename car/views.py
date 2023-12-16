from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CreateUser,ChangeUserData,CommentFrom
from .models import CarModel
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Create your views here.
class SignUp(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = CreateUser

class LogIn(LoginView):
    template_name = 'signup.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'login successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'login information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context




@login_required
def profile(req):
    data = CarModel.objects.filter(user=req.user)
    return render(req, 'profile.html', {'data':data})
@login_required
def edit(req):
    profile = ChangeUserData(instance=req.user)
    if req.method == 'POST':
        profile = ChangeUserData(req.POST, instance=req.user)
        if profile.is_valid():
            profile.save()
            messages.success(req, 'Profile Upadated successfully')
            return redirect('profile')
    return render(req, 'profile2.html',{'form': profile})


def details(req, id):
    data = CarModel.objects.get(pk=id)
    return render(req, 'details.html',{'data':data,})

method_decorator(login_required,name='dispatch')
class LogOut(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')