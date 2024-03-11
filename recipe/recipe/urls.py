"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as rviews

from recipes import views

router=SimpleRouter()
router.register('recipes',views.recipes),
router.register('indian',views.filterIndian),
router.register('italian',views.filterItalian)
router.register('chinese',views.filterChinese)
router.register('register',views.CreateUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('login/',rviews.obtain_auth_token),
    path('review/',views.AddReviews.as_view()),
    path('review/<int:id>',views.ViewRating.as_view()),
    path('search',views.Search.as_view())

]
