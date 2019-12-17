from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Crown import views as local_views
from posts import views as posts_views


#importacion para rest framework
from rest_framework import routers
from licitaciones import views as licitaciones_views
from users import views as user_views

#registro de Routers
router = routers.DefaultRouter()
router.register(r'lici', licitaciones_views.LicitacionViewSet)
router.register(r'usersAPI', user_views.UserViewSet)
router.register(r'groupsAPI', user_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API..

urlpatterns = [
    path('', include(router.urls)),
    path ('hello_world', local_views.hello_world),
    path ('hi', local_views.hi),
    path ('posts/', posts_views.list_posts),



    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)