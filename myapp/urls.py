from django.conf.urls import url
import views

urlpatterns = [ 
    url(r'^hello0/', views.hello0, name = 'hello0'),
    url(r'^hello1/', views.hello1, name = 'hello1'),
    url(r'^hello2/(\d+)/', views.hello2, name = 'hello2'),
    url(r'^hello3/(\d{2})/(\d{4})', views.hello3, name = 'hello3')
]