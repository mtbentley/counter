from django.http import HttpResponse
from count.models import Inc
from django.db import transaction


@transaction.atomic
def hi(request):
    try:
        inc = Inc.objects.get(pk=1)
        inc.number += 1
        inc.save()
    except Inc.DoesNotExist:
        inc = Inc(number=1)
        inc.save()
    try:
        request.session['count'] += 1
    except KeyError:
        request.session['count'] = 1

    to_return = "Total: %s\n<br />\nSession: %s" % (inc.number,
                                                    request.session['count'])

    return HttpResponse(to_return)

def low(request):
    return HttpResponse("HI!")
