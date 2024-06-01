from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartViewSet, CommonWordsView

router = DefaultRouter()
router.register(r'parts', PartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('common-words/', CommonWordsView.as_view(), name='common-words'),

]
