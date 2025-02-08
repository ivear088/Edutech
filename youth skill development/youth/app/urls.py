from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home' ),
    path('sas_view',views.sas_view,name='sas_view'),
    path('analysis',views.analysis,name='analysis'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    

]
