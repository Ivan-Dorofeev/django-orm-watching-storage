import datetime
import zoneinfo

from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    """рассчитывает длительность визита"""
    now_time = datetime.datetime.now(datetime.timezone.utc)
    times_diff = now_time - visit.entered_at
    return times_diff


def format_duration(duration):
    """Превращает длительность визита в строку, готовит к выводу на страницу."""
    hours, rem = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f'{hours}:{minutes}:{seconds}'

