from datetime import timedelta, datetime
from .models import *

def deleteOldData():
    weekAgo = datetime.today() - timedelta(days=7)
    UserHealth.objects.filter(dateTimeActivity__lte=weekAgo).delete()


