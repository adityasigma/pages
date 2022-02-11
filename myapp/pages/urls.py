from django.urls import path
from .views import index, UserView
from .tests import TheModelView

urlpatterns = [
    path('', index, name='index'),
    path('themodel/', TheModelView),
    path('users_list/', UserView.as_view()),
    path('users_list/<int:id>', UserView.as_view()),
]
