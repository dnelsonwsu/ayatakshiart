from django.shortcuts import render
from common.views import get_common_context


def faq(request):
    context = get_common_context(request)
    return render(request, 'faq/faq.html', context)

    