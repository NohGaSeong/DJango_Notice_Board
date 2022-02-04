from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'),
    path('question/create/', views.question_create, name = 'question_create'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'),
=======
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
=======
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
]
