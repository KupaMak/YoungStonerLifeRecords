import django
from django_filters import ChoiceFilter, CharFilter
import django_filters
from .models import *


class Studio_Filter(django_filters.FilterSet):


    studio_name = CharFilter( field_name='studio_name',lookup_expr='icontains', label='Search By Name')
    location = CharFilter( field_name='location',lookup_expr='icontains', label=' Search By Location')

    class Meta:
        model = Studio
        fields = ['studio_name', 'location']

class Studio_Session_Filter(django_filters.FilterSet):

    artist = CharFilter( field_name='artist',lookup_expr='icontains', label='Search By Artist')

    class Meta:
        model = StudioSession
        fields = ['artist']

