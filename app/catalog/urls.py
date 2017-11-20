from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'versions', views.VersionViewSet)
router.register(r'apps', views.AppViewSet)
router.register(r'pools', views.PoolViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'contexts', views.ContextViewSet)

app_name = 'catalog'
urlpatterns = [
	url(r'^api/', include(router.urls, namespace='api')),
    url(r'^$', views.BaseView.as_view(), name='base'),
    url(r'^environment/(?P<env>[a-z]+)/$', views.EnvironmentView.as_view(), name='environment'),
    url(r'^versions/(?P<app>[\w-]+)/$', views.VersionView.as_view(), name='versions'),
]
