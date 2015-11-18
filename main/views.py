from django.shortcuts import render, render_to_response
from django.http import JsonResponse  

from django.template import RequestContext
from main.models import DVD, MovieCas
import string


def dvd_list_cas(request):

    context = {}

    dvd_list = MovieCas.objects.all()

    context['dvd_list'] = dvd_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request)) 


def dvd_list_temp(request):

    context = {}

    dvd_list = DVD.objects.all()[:10000]

    context['dvd_list'] = dvd_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request)) 


def dvd_list_mysql(request):

    context = {}

    dvd_list = DVD.objects.using('mysql').all()[:5000]

    context['dvd_list'] = dvd_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request)) 


def api_dvd_list(request):

    page_number = request.GET.get('page_number', 100)

    if page_number != 100:
        start_number = page_number + 100
    else:
        start_number = 0

    dvds = DVD.objects.all()[start_number:page_number]

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


def dvd_list(request):
    context = {}

    return render_to_response('dvd_list.html', context, context_instance=RequestContext(request))

# #def main_page(request):
#     context = {}

#     return render_to_response('main_page.html', context, context_instance=RequestContext(request))


def api_dvd_detail(request, pk):
        dvds = DVD.objects.get(pk=pk)

        dvd_detail = {'dvd_title': dvds.dvd_title, 
                      'price': dvds.price,
                      'genre': dvds.genre,
                      'year': dvds.year,
                      'rating': dvds.rating,
                      'release_date': dvds.release_date

                      }

        return JsonResponse(dvd_detail)


def dvd_detail(request):
    context = {}

    return render_to_response('api_dvd_detail.html', context, context_instance=RequestContext(request))
