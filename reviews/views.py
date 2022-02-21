import requests

from django.conf import settings
from django.shortcuts import get_object_or_404

from django.contrib.admin.views.decorators import staff_member_required

from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(
    ModelViewSet,
):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@staff_member_required
def publish_review_view(request, object_id):
    """
    View публикации отзыва из админки
    todo: Переход по ссылке и переадресация назад выглядит как костыль
    """
    obj = get_object_or_404(Review, pk=object_id)
    obj.is_published = True
    obj.save()
    requests.post(
        url=f'{settings.REVIEW_PUBLISH_HOST}{settings.REVIEW_PUBLISH_KEY}',
        json={
            'author': obj.author.id,
            'rating': obj.rating,
            'review': obj.comment,
        }
    )
    messages.info(request, 'Отзыв опубликован')
    return HttpResponseRedirect(
        reverse(
            f'admin:'
            f'{obj._meta.app_label.lower()}_'
            f'{obj._meta.object_name.lower()}_'
            f'change',
            kwargs={'object_id': object_id}
        )
    )

