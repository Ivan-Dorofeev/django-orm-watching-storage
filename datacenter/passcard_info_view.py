import datetime

from datacenter.models import Passcard, get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits_list = []

    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    now = datetime.datetime.now(datetime.timezone.utc)

    for visit in visits:
        # время входа
        entered_at = visit.entered_at

        # продолжительностьь
        duration = get_duration(visit)
        duration_str = format_duration(duration)

        # подозрительность
        if visit.leaved_at is None and (now - visit.entered_at).total_seconds() > 3600:
            is_strange = True
        elif (visit.leaved_at - visit.entered_at).total_seconds() > 3600:
            is_strange = True
        else:
            is_strange = False

        this_passcard_visits_list.append({
            'entered_at': entered_at,
            'duration': duration_str,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_list
    }
    return render(request, 'passcard_info.html', context)
