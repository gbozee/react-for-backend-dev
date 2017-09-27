"""formset_in_react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django import forms

class EducationForm(forms.Form):
    school = forms.CharField()
    course = forms.CharField()

EducationFormset = forms.formset_factory(EducationForm,max_num=2)

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
       context = super(HomeView,self).get_context_data(**kwargs)
       if 'form' not in context:
           context['form'] = EducationFormset()
       return context

urlpatterns = [
    url(r'^$', HomeView.as_view(),name='index'),
    url(r'^admin/', admin.site.urls),
]
