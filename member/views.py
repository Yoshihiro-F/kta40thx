from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Memberlist

def index(request):
    noimage = "noimage.jpg"
    members = Memberlist.objects.order_by('orderid').all()
    return render_to_response('../templates/member/base_view.html', {'members': members, 'noimage':noimage}, context_instance = RequestContext(request))

