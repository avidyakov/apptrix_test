from rest_framework import routers

from .views import UserViewSet

app_name = 'main_app'

router = routers.SimpleRouter()
router.register('clients', UserViewSet)

urlpatterns = router.urls
