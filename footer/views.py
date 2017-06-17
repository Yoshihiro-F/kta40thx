from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Footer

def footering(request):
    footers = Footer.objects.all()
    return render_to_response('../templates/pages/menus/footerkai.html', {'footers': footers}, context_instance = RequestContext(request))
