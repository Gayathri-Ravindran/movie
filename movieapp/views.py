from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import Movie
from . forms import movieform
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,'index.html',context)
def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name1=request.POST.get('name',)
        desc1=request.POST.get('desc',)
        year1=request.POST.get('year',)
        img1=request.FILES['img']
        movie=Movie(name=name1,desc=desc1,year=year1,img=img1)
        movie.save()


    return render(request, 'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form1':form,'movie1':movie})

def delete(request,id):
    if request.method=="POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')




# def delete(request, id):
#     movie = Movie.objects.get(id=id)
#
#     if request.method == "POST":
#         if "yes" in request.POST:
#             movie.delete()
#             return redirect('/')
#         else:
#             return redirect('/')
#
#     return render(request, 'delete.html')
