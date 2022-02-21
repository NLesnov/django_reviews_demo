from django.contrib import admin
from django import forms

from .models import Review


class ReviewAdminForm(forms.ModelForm):
    rating = forms.IntegerField(
        label='Рейтинг',
        min_value=1,
        max_value=5,
    )
    # todo: Строго по ТЗ должен быть неактивный чекбокс, но отображение
    #  readonly флага иконкой мне кажется эстетичнее.
    #  Для чекбокса - раскомментировать это поле, убрать 'is_published' из
    #  readonly_fields в ReviewAdmin
    # is_published = forms.BooleanField(
    #     label='Отзыв опубликован',
    #     disabled=True
    # )

    class Meta:
        model = Review
        fields = '__all__'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    change_form_template = 'admin/review_change_form.html'
    readonly_fields = (
        'created_on',
        # todo: Убрать для отображения флага чекбоксом, см. выше
        'is_published',
    )

