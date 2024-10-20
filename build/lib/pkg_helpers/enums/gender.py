from django.db.models import IntegerChoices

class Genders(IntegerChoices):
    PRIVATE = -1
    FEMALE = 0
    MALE = 1