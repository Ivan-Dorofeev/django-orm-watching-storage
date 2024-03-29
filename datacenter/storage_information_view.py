from datacenter.models import get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    serialized_non_closed_visits = []

    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
        duration = get_duration(visit)
        duration_str = format_duration(duration)

        is_strange = duration.total_seconds() > 600

        serialized_non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': duration_str,
            'is_strange': is_strange})

    context = {'non_closed_visits': serialized_non_closed_visits}
    return render(request, 'storage_information.html', context)
