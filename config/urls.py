from django.contrib import admin
from django.urls import path, include

from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request):
        return Response({"message": "ok"}, 200)


urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('admin/', admin.site.urls),
    
    path("test/", TestView.as_view()),
]