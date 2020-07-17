from django.http import HttpResponseRedirect
from .models import Link


def show(request, shortened):
    link = None

    try:
        link = Link.objects.get(hashed=shortened)
    except Exception:
        pass

    return HttpResponseRedirect('{}'.format(link.original))


def store(request):
    pass
