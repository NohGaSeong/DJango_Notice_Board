from django.contrib import admin
from django.urls import path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # pybo/ URL이 요청되면 views.index 를 호출하라는 매핑을 추가.
    # views.index 는 views.py 파일의 index 함수를 의미한다.
    path('pybo/', views.index),
    # pybo 라고 입력했을때 pybo/ 로 변환될텐데 이것은 URL을 정규화하는 장고의 기능이다.
]
