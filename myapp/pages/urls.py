from django.urls import path
from .views import index, UserView, AllUserView, logView
from .tests import TheModelView

urlpatterns = [
    path('', index, name='index'),
    path('all_users_list/', AllUserView.as_view()),
    path('all_log/', logView.as_view()),
    path('users_list/', UserView.as_view()),
    path('users_list/<int:id>', UserView.as_view()),
]
