from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Planyear

def index(request):
    try:
        latestyears = Planyear.objects.order_by('-eve_year')[0:1].get()

        yearslist = []
        years = Planyear.objects.order_by('-eve_year').all()
        for lists in years.values('eve_year'):
            yearslist.append(lists['eve_year'])
        yearing = latestyears.eve_year
        monthlist = latestyears.planmonth_set.values('eve_month','evently')
    except UnboundLocalError:
        pass
    except:
        yearing = ""
        monthlist = ""
        yearslist = ""
    return render_to_response("../templates/planning/base_show.html", {'yearing': yearing, 'monthlist':monthlist,'yearslist':yearslist }, context_instance = RequestContext(request))


def lastyear(request, year):
    lastyears = Planyear.objects.get(eve_year=year)
    yearslist = []
    years = Planyear.objects.order_by('-eve_year').all()
    for lists in years.values('eve_year'):
        yearslist.append(lists['eve_year'])
    yearing = lastyears.eve_year
    monthlist = lastyears.planmonth_set.values('eve_month','evently')
    return render_to_response("../templates/planning/base_show.html", {'yearing': yearing, 'monthlist':monthlist, 'yearslist':yearslist}, context_instance = RequestContext(request))
