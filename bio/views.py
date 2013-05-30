from django.template import RequestContext
from django.shortcuts import render_to_response
from common.views import get_common_context


def bio(request):
    context = get_common_context(request)
    
    return render_to_response('bio/bio.html', context, context_instance=RequestContext(request))
