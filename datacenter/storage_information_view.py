from datacenter.models import Passcard, get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_list = []

    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration = get_duration(visit)
        duration_str = format_duration(duration)

        if duration.total_seconds() > 600:
            is_strange = True
        else:
            is_strange = False

        non_closed_visits_list.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': duration_str,
            'is_strange': is_strange})

    context = {'non_closed_visits': non_closed_visits_list}
    return render(request, 'storage_information.html', context)
