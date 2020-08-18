from django.urls import path
from . import views

urlpatterns = [
    # url('',views.home,name="home"),
    url('',views.HomePageView.as_view(),name="home"),
    # url('detail/<int:id>',views.detail,name="detail"),
    url('detail/<int:pk>',views.ProjectDetailView.as_view(),name="detail"),
    url('profile_detail/<int:pk>',views.ProfileDetailView.as_view(),name="profile_detail"),
    url('search/',views.search,name="search"),
    url('projects/create_profile',views.ProfileCreateView.as_view(),name="create_profile"),
    url('projects/profile_update/<int:pk>',views.ProfileUpdateView.as_view(),name="profile_update"),
    url('projects/profile_delete/<int:pk>',views.ProfileDeleteView.as_view(),name="profile_delete"),
    url('rating/',views.review_rating,name="review"),
    url('projects/create',views.ProjectCreateView.as_view(),name="create"),
    url('projects/update/<int:pk>',views.ProjectUpdateView.as_view(),name="update"),
    url('projects/delete/<int:pk>',views.ProjectDeleteView.as_view(),name="delete"),
    url('signup/',views.SignUpView.as_view(),name="signup"),
]