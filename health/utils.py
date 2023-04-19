import random
import string
from datetime import datetime, timedelta

from .models import *

# def deleteOldData():
#     weekAgo = datetime.today() - timedelta(days=7)
#     User.objects.filter(dateTimeActivity__lte=weekAgo).delete()

#
# def generateRandomData(length):
#     gender = ['Мужской', 'Женский']
#     letters = string.ascii_letters
#     for user_health in range(length):
#         rand_string = ''.join(random.choice(letters) for i in range(10))
#         user_health = Health(
#             email=rand_string,
#             gender=random.choice(gender),
#             age=random.randint(10, 80),
#             steps=random.randint(3000, 30000),
#             minutesWalk=random.randint(30, 500),
#             burnedEnergy=random.randint(1500, 20000),
#             dateTimeActivity=datetime.now()
#         )
#         user_health.save()
