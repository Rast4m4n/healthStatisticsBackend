from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/usersHealth', UserHealthViewSet, 'usersHealth')

urlpatterns = router.urls