from django.shortcuts import render

# Create your views here.
from .models import City, House
from .serializers import CitySerializer, HouseSerializer
import django_filters
from rest_framework import (authentication,
                            filters,
                            permissions,
                            viewsets)


class DefaultsMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )


class CityViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = City.objects.order_by('created')
    serializer_class = CitySerializer
    ordering_fields = ('created', )

    def get_queryset(self):
        return self.queryset.all()


class HouseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = House.objects.order_by('created')
    serializer_class = HouseSerializer
    ordering_fields = ('created', )
    filter_fields = ('city', 'name',)

    def get_queryset(self):
        return self.queryset.all()
