from rest_framework import routers

from .utils import *
from .views import *

router = routers.DefaultRouter()
router.register('api/health', HealthViewSet, 'health')
router.register('api/user', UserViewSet, 'user')

# deleteOldData()
# generateRandomData(100)


urlpatterns = router.urls

