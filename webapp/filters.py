import django_filters
from django_filters import CharFilter
from .models import *

class CustomerFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains', label='Username')
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='First Name')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Last Name')

    class Meta:
        model = WardrobePost
        fields = ('username','first_name','last_name')
        exclude = ('email','phone','profile_pic', 'date_created','image',)

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Style Title')
    caption = CharFilter(field_name='caption', lookup_expr='icontains', label='Caption')

    class Meta:
        model = WardrobePost
        fields = '__all__'
        exclude = ('date_created','tags','customer','image',)