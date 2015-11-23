from django.shortcuts import render, render_to_response
from django.http import JsonResponse  

from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import ListView
from main.models import DVD, MovieCas
import string


# def based view
def dvd_list_dbv(request):

    context = {}

    dvds = DVD.objects.filter(title__istartswith=letter)

    context['dvd_list'] = dvd_list

    paginator = Paginator(movie_list, 10)

    page = (request.GET.get("page", 1))

    # page = request.GET['page']  - You can use it but you will fail out!!!
      
    try:
        dvd_list = paginator.page(page)
    except(InvalidPage, EmptyPage):
        dvd_list = paginator.page(paginator.num_pages)

    context['dvd_list'] = dvd_list

    return render_to_respones('dvd_list_dbv.html', context, context_instance=RequestContext(request))


# Class based view
class DvdListView(ListView):
    model = DVD
    queryset = DVD.objects.all()[:100]
    template_name = "dvd_list_cbv.html"
    context_object_name = "dvd_list"
    paginate_by = 10


# HandleBars Based View
def dvd_list(request):

    page = int(request.GET.get("page", '1'))

    letter = request.GET.get('letter', 'A')

    api_dict = {}

    dvds = DVD.objects.filter(dvd_title__istartswith=letter)   

    print page 

    paginator = Paginator(dvds, 20)

    try:
        dvds = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvds = paginator.page(paginator.num_pages)    

    dvd_list = []

    for dvd in dvds:
        dvd_list.append({'title': dvd.dvd_title,
                           # 'studio': dvd.studio.studio,
                           'price': dvd.price,
                           'rating': dvd.rating,
                           'genre': dvd.genre.genre,
                           'pk': dvd.pk,
                           })

    api_dict['dvds'] = dvd_list

    try:
        api_dict['next_page'] = dvds.next_page_number()
    except:
        pass

    try:
        api_dict['previous_page'] = dvds.previous_page_number()
    except:
        pass

    api_dict['current_page'] = dvds.number

    api_dict['all_pages'] = dvds.paginator.num_pages

    api_dict['letters'] = list(string.ascii_uppercase)

    return JsonResponse(api_dict)

# Template


# def dvd_list(request):
#     dvds = DVD.objects.all()[:300]
#     api_dict = {}
#     dvd_list = []
#     api_dict['dvd_list'] = dvd_list

#     api_dict['letters'] = list(string.ascii_uppercase)

#     for dvd in dvds:
#         dvd_list.append({'dvd_title': dvd.dvd_title,
#                            # 'studio': dvd.studio.studio,
#                            'price': dvd.price,
#                            'rating': dvd.rating,
#                            'genre': dvd.genre.genre,
#                            'release': dvd.released,
#                            'pk': dvd.pk,
#                        })

#     return JsonResponse(api_dict)







# #for dvd in dvds:
    #     dvd_list.append({'dvd_title': dvd.dvd_title,
    #                      #'studio': dvd.studio,
    #                      'price': dvd.price,
    #                      'rating': dvd.rating,
    #                      'genre': dvd.genre,
    #                      'pk': dvd.pk,

    #                    })

    # api_dict['dvds'] = dvd_list

    # try:
    #   api_dict['next_page'] = dvds.next_page_number()
    # except:
    #   pass

    # try:
    #   api_dict['previous_page'] = dvds.previous_page_number()
    # except:
    #   pass

    # api_dict['current_page'] = dvds.number 

    # api_dict['all_pages'] = dvds.paginator.num_pages

    # letter = request.GET.get('letter', 'A')


    # api_dict['letters'] = list(string.ascii_uppercase)

    # return JsonResonse(api_dict)

    # return render_to_response('dvd_list_dbv.html',context context_instance=RequestContext(request))





# # # Def Based View
# def dvd_list(request):

#     api_dict = {}

#     movies = Movie.objects.all()   

#     page = int(request.GET.get("page", '1'))  

#     print page 

#     paginator = Paginator(movies, 10)

#     try:
#         movies = paginator.page(page)
#     except (InvalidPage, EmptyPage):
#         movies = paginator.page(paginator.num_pages)    

#     movie_list = []

#     for movie in movies:
#         movie_list.append({'title': movie.title,
#                            'studio': movie.studio,
#                            'price': movie.price,
#                            'rating': movie.rating,
#                            'genre': movie.genre,
#                            'pk': movie.pk,
#                            })


#     api_dict['movies'] = movie_list

#     try:
#         api_dict['next_page'] = movies.next_page_number()
#     except:
#         pass

#     try:
#         api_dict['previous_page'] = movies.previous_page_number()
#     except:
#         pass

#     api_dict['current_page'] = movies.number

#     api_dict['all_pages'] = movies.paginator.num_pages

#     api_dict['letters'] = list(string.ascii_uppercase)

#     return JsonResponse(api_dict)







#     dvds = DVD.objects.all()   

#     page = int(request.GET.get("page", '1'))  

#     print page 

#     paginator = Paginator(movies, 10)

#     try:
#         movies = paginator.page(page)
#     except (InvalidPage, EmptyPage):
#         movies = paginator.page(paginator.num_pages)    

#     movie_list = []

#     for movie in movies:
#         movie_list.append({'title': dvd.dvd_title,
#                           # 'studio': movie.studio.studio,
#                            'price': dvd.price,
#                            'rating': dvd.rating,
#                           # 'genre': movie.genre.genre,
#                            'pk': dvd.pk,
#                            })

#     api_dict['movies'] = movie_list

#     try:
#         api_dict['next_page'] = movies.next_page_number()
#     except:
#         pass

#     try:
#         api_dict['previous_page'] = movies.previous_page_number()
#     except:
#         pass

#     api_dict['current_page'] = movies.number

#     api_dict['all_pages'] = movies.paginator.num_pages

#     api_dict['letters'] = list(string.ascii_uppercase)

#     return JsonResponse(api_dict)


















# CASSANDRA  VIEW
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


#def dvd_list(request):
    context = {}

    return render_to_response('dvd_list.html', context, context_instance=RequestContext(request))

# #def main_page(request):
#     context = {}

#     return render_to_response('main_page.html', context, context_instance=RequestContext(request))


# DETAIL VIEWS
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
