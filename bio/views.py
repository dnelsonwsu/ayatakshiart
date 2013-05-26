from django.shortcuts import render
from common.views import get_common_context


def bio(request):
    context = get_common_context(request)
    return render(request, 'bio/bio.html', context)

    