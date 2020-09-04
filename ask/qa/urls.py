from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    # re_path(r'', views.test),
    path('', views.index, name='index'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.sign_up_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('question/<int:q_id>/', views.question_view, name='question'),
    path('ask/', views.ask_view, name='ask'),
    path('popular/', views.popular, name='test'),
    path('new/', views.test, name='test'),
]
