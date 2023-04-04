from rest_framework import routers
from .api import *
from .utils import deleteOldData

router = routers.DefaultRouter()
router.register('api/usersHealth', UserHealthViewSet, 'usersHealth')
deleteOldData()

urlpatterns = router.urls

