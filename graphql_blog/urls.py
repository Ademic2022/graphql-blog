"""
URL configuration for graphql_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth.views import LoginView
from graphene_django.views import GraphQLView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from core.views import PrivateGraphQLView
from .schema import schema

urlpatterns = [
    path('', RedirectView.as_view(url='/graphql/')),

    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('graphql/', PrivateGraphQLView.as_view(graphiql=True, schema=schema)),
]
