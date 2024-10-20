from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from pkg_helpers.enums.role import Roles
from pkg_helpers.enums.gender import Genders
from pkg_helpers.enums.user_account_status import AccountStatuses
from pkg_helpers.auth.user_dto import UserDTO

from django.contrib.auth.base_user import BaseUserManager

class User(AbstractBaseUser):
    class Meta:
        db_table = "users"
        app_label = "appbase"
        
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    gender = models.SmallIntegerField(choices=Genders.choices, default=Genders.PRIVATE)
    birthday = models.DateField(null=True)
    avatar_url = models.CharField(max_length=1500, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    status = models.CharField(max_length=50, choices=AccountStatuses.choices, null=False)
    role = models.CharField(max_length=20, choices=Roles.choices, null=False)

    USERNAME_FIELD = "email"

    objects = BaseUserManager()

    def to_dto(self) -> UserDTO:
        return UserDTO(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            gender=Genders(self.gender),
            birthday=self.birthday,
            avatar_url=self.avatar_url,
            phone_number=self.phone_number,
            status=AccountStatuses(self.status),
            role=Roles(self.role)
        )