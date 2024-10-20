from django.db.models import TextChoices

class AccountStatuses(TextChoices):
    ACTIVATED = "ACTIVATED"
    UNVERIFIED = "UNVERIFIED"
    BLOCKED = "BLOCKED"