from django.shortcuts import render,get_object_or_404,redirect
from .models import Project,Rating,Profile
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  ProjectRatingForm
from django.db.models import Avg
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

# def home(request):
#     context = {
#         'projects':Project.objects.all()
#     }
#     return render(request,'index.html',context)

# def detail(request,id):
#     context = {
#         'project':get_object_or_404(Project,pk=id)
#     }
#     return render(request,'detail.html',context)

class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Project
    context_object_name ='projects'
    
class ProjectDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Project
    context_object_name = 'project'
    
@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Project.objects.filter(
            Q(name__icontains=search_term)|
            Q(email__icontains=search_term)|
            Q(info__icontains=search_term)
            )
        context = {
             'search_term': search_term,
             'projects':search_results
    }
        return render(request,'search.html',context)
    else:
        return redirect('home')

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'create.html'
    fields = ['name','url','info','image']
    success_url = '/'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(
            self.request, 'Your project has been successfully created!')
        return redirect('home')
    
class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'update.html'
    fields = ['name','url','info','image']
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(
            self.request, 'Your project has been successfully updated!')
        return redirect('detail', instance.pk)
        
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Your project has been successfully deleted!')
        return super().delete(self, request, *args, **kwargs)
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    

class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'create_profile.html'
    fields = ['name','email','image','bio']
    success_url = '/'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(
            self.request, 'Your contact has been successfully created!')
        return redirect('/')
    
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['name','email','image','bio']
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(
            self.request, 'Your profile has been successfully updated!')
        return redirect('profile_detail', instance.pk)
    
class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = '/'

class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = Project
    context_object_name = 'profile'

# def user(request, user_id):
#     user_object = get_object_or_404(User, pk=user_id)
#     if request.user == user_object:
#         return redirect('profile')
#     user_projects = user_object.posts.all()
#     return render(request, 'user.html', locals())


# def single_project(request, c_id):
#     current_user = request.user
#     current_project = Post.objects.get(id=c_id)
#     ratings = Rating.objects.filter(post_id=c_id)
#     usability = Rating.objects.filter(post_id=c_id).aggregate(Avg('usability_rating'))
#     content = Rating.objects.filter(post_id=c_id).aggregate(Avg('content_rating'))
#     design = Rating.objects.filter(post_id=c_id).aggregate(Avg('design_rating'))

#     return render(request, 'project.html',
#                   {"project": current_project, "user": current_user, 'ratings': ratings, "design": design,
#                    "content": content, "usability": usability})


def review_rating(request, id):
    current_user = request.user

    current_project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = current_project
            rating.user = current_user
            rating.save()
            return redirect('project', id)
    else:
        form = ProjectRatingForm()

    return render(request, 'rating.html', {'form': form, "project": current_project, "user": current_user})