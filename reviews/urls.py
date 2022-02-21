from django.urls import path
from rest_framework import routers
from .views import (
    publish_review_view,
    ReviewViewSet,
)

review_router = routers.SimpleRouter()
review_router.register(r'', ReviewViewSet)

urlpatterns = review_router.urls
urlpatterns += [
    path('<int:object_id>/publish', publish_review_view, name='publish-review')
]
