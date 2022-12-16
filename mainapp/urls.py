from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("news.html/", views.NewsPageView.as_view()),
    path("courses_list.html/", views.CoursePageView.as_view()),
    path("contacts.html/", views.ContactPageView.as_view()),
    path("doc_site.html/", views.DocSitePageView.as_view()),
    path("login.html/", views.LoginPageView.as_view()),
]
