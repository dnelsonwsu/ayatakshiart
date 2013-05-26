from django.shortcuts import render
from common.views import get_common_context


def contact(request):
    context = get_common_context(request)
    return render(request, 'contact/contact.html', context)

    