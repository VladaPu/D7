from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post
from django import forms


# Создаем свой набор фильтров для модели Post.

class PostsFilter(FilterSet):
    created_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'postCategory': ['exact']}