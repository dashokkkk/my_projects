from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def get_queryset(self, category=None):
        queryset = super().get_queryset().select_related(
            'category',
            'location',
            'author',
        ).filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
