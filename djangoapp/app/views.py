from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, AccountUpdateForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


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
class DiaryLogs(LoginRequiredMixin, ListView):
    model = Post
    template_name = "app/diary.html"
    # Rename the variable to match in HTML
    context_object_name = 'posts'
    # Order from recently created to last created post
    ordering = ['-date_posted']
    # Number of diary to display per page
    paginate_by = 3


class SearchResultView(LoginRequiredMixin, ListView):
    # Similar to DiaryLogs however this is for returning search result
    model = Post
    template_name = "app/searchbar.html"
    context_object_name = 'posts'

    def get_queryset(self):
        # Takes q value from submission in html
        query = self.request.GET.get('q')
        search_list = Post.objects.order_by('-date_posted').filter(
            Q(title__icontains=query) | Q(content__icontains=query)
            | Q(motivation__icontains=query)
        )
        return search_list


# Accessing individual diary logs
class IndividualDiaryLogs(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'app/diarylog.html'


# Creating new diary logs
class NewDiaryLogs(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'motivation', 'diary_image']
    template_name = 'app/newdiaryform.html'


# Editing diary logs
class EditDiaryLogs(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'motivation', 'diary_image']
    template_name = 'app/newdiaryform.html'


# Deleting diary logs
class DeleteDiaryLogs(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'app/confirmdelete.html'
    # If delete is successful, redirect to
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
        # If user submit the data to database
        user_form = UserUpdateForm(request.POST, instance=request.user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)
        if user_form.is_valid() and account_form.is_valid():
            # If data is valid
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
