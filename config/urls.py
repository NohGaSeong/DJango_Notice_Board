from django.contrib import admin
from django.urls import include, path
from pybo.views import base_views # views 대신 base_views
                                  # 이러한 방법을 이용하면 이미 views.py 모듈을 import 하여 사용하던 기존의 파이썬 프로그램을 
                                  # 모두 수정해야하는 불편함은 있지만 명확해지는 장점은 있다.

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]