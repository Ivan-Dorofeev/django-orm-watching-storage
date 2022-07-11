import datetime

from datacenter.models import Passcard, get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, get_passcode):
    visits = []

    passcard_from_passcode = Passcard.objects.get(passcode=get_passcode)
    serialized_visits = Visit.objects.filter(passcard=passcard_from_passcode)

    for visit in serialized_visits:
        entered_at = visit.entered_at

        duration = get_duration(visit)
        duration_str = format_duration(duration)

        is_strange = (not visit.leaved_at and duration.total_seconds() > 3600) or (
                    visit.leaved_at - visit.entered_at).total_seconds() > 3600

        visits.append({
            'entered_at': entered_at,
            'duration': duration_str,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard_from_passcode,
        'this_passcard_visits': visits
    }
    return render(request, 'passcard_info.html', context)
