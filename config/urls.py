
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1ck -> 2차 -> 3차
    # http://127.0.0.1/bookmark/?
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
