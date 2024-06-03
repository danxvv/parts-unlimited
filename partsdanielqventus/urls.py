from django.http import HttpResponseRedirect
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


def redirect_to_docs(request):
    return HttpResponseRedirect('/api/schema/swagger-ui/')


urlpatterns = [
    path('api/', include('parts_unlimited.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', redirect_to_docs),
]
