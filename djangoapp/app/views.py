from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, AccountUpdateForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Homepage
@login_required
def home(request):
    return render(request, "app/home.html")

'''
@login_required
def diary(request):
    diary = {
        'title': 'Your Diary',
        'posts': Post.objects.order_by('-date_posted'),
    }
    return render(request, "app/diary.html", diary)
'''


# Diary logs lists
class DiaryLogs(ListView):
    model = Post
    template_name = "app/diary.html"
    context_object_name = 'posts' #rename the variable to match in HTML
    ordering = ['-date_posted']
    paginate_by = 3


# Accessing individual diary logs
class IndividualDiaryLogs(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'app/diarylog.html'


# Creating new diary logs
class NewDiaryLogs(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app/newdiaryform.html'


# Editing diary logs
class EditDiaryLogs(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app/newdiaryform.html'


# Deleting diary logs
class DeleteDiaryLogs(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'app/confirmdelete.html'
    success_url = '/yourdiary/'


# About
@login_required
def about(request):
    return render(request, "app/about.html", {'title': 'About'})


# Account
@login_required
def account(request):
    return render(request, "app/account.html", {'title': 'Account'})


# Settings
@login_required
def settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save() and account_form.save()
            messages.success(request, f"Account successfully updated!")
            return redirect('app-account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        account_form = AccountUpdateForm(instance=request.user.account)
    update_forms = {
        'title': 'Account',
        'user_form': user_form,
        'account_form': account_form,
    }
    return render(request, "app/settings.html", update_forms)
