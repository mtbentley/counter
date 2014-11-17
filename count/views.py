from django.http import HttpResponse
from count.models import Inc

# Create your views here.

def hi(request):
    try:
        inc = Inc.objects.all()[0]
        inc.number += 1
        inc.save()
    except IndexError:
        inc = Inc(number=1)
        inc.save()
    try:
        request.session['count'] += 1
    except KeyError:
        request.session['count'] = 1

    to_return = "Total: %s\n<br />\nSession: %s" % (inc.number,
                                                    request.session['count'])

    return HttpResponse(to_return)
