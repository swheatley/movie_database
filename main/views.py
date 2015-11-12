from django.shortcuts import render, render_to_response
from django.http import JsonResponse  #HttpResponse

from django.template import RequestContext
from main.models import DVD

 
def dvd_list(request):

    dvds = DVD.objects.all()[:100]

    api_dict = {}
    dvd_list = []

    api_dict['dvds'] = dvd_list

    for dvd in dvds:
        dvd_list.append({'dvd_title': dvd.dvd_title, 
                         'price': dvd.price,
                         'genre': dvd.genre,
                         'year': dvd.year,
                         'rating': dvd.rating,
                         'release_date': dvd.release_date

                         })

    return JsonResponse(api_dict)


# #def main_page(request):
#     context = {}

#     return render_to_response('main_page.html', context, context_instance=RequestContext(request))

def dvd_detail(request, pk):
        dvds = DVD.objects.get(pk=pk)

        dvd_detail = {'dvd_title': dvd.dvd_title, 
                      'price': dvd.price,
                      'genre': dvd.genre,
                      'year': dvd.year,
                      'rating': dvd.rating,
                      'release_date': dvd.release_date

                      }

        return JsonResponse(dvd_detail)