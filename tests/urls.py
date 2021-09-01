from django.urls import include, path

urlpatterns = [
    path("", include("pgallery.urls", namespace="pgallery")),
]
