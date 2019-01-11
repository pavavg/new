from django.conf.urls import include, url

urlpatterns = ['', url(r'^hello/', 'myapp.views.hello', name = 'hello'),]
