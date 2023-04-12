from rest_framework import routers
from .api import *
from .utils import *

router = routers.DefaultRouter()
router.register('api/usersHealth', UserHealthViewSet, 'usersHealth')
deleteOldData()
# generateRandomData(100)


urlpatterns = router.urls

