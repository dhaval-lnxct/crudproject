
from django.urls import path
from enroll import views

urlpatterns = [
    
    path('1',views.index,name='home'),
    path('',views.addshow,name='show'),
    path('update/',views.update,name='update'),

    
]
