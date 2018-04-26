# -*- encoding: utf-8 -*-
from rest_framework import routers

from . import views

router = routers.DefaultRouter()  # DefaultRouter会生成rootview

router.register(r'city', views.CityViewSet)
router.register(r'house', views.HouseViewSet)
