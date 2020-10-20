from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='REFUGIO API')

urlpatterns = [
    path('docs/', schema_view),
    #path('markdownx/', include('markdownx.urls')),

    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('api/', include('rest_api.urls')),
    path('watchman/', include('watchman.urls')),

    
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
