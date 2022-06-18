from django.shortcuts import render,redirect
from .models import *
from django.utils.text import slugify
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def home(request):
    categ = categories.objects.all()
    book = books.objects.all()
    return render(request,'index.html',{'books':book,'categ':categ})


def details(request, ct_slug, bk_slug=None):
    if bk_slug == None:
        bks = books.objects.filter(categ__slug=ct_slug)
        categ=categories.objects.all()
        return render(request, 'index.html', {'books': bks,'categ':categ})
    book = books.objects.get(slug=bk_slug,categ__slug=ct_slug)
    return render(request, 'detail.html', {'obj': book})

def adminpanel(request):
    cat = categories.objects.all()
    return render(request,'adminpanel.html',{'cat':cat})

def cat_delete(request,cat_id=None):
    if request.method == 'POST':
        d=categories.objects.get(id=cat_id)
        d.delete()
        return redirect('adminpanel')
    return render(request,'confirm.html')

def bk_delete(request,bk_id=None):
    if request.method == 'POST':
        d=categories.objects.get(id=bk_id)
        d.delete()
        return redirect('home')
    return render(request, 'confirm.html')

def add_book(request):
    if request.method == 'POST':
        try:
            name=request.POST.get('name')
            if books.objects.filter(name=name).exists():
                cate = categories.objects.all()
                return render(request, 'add.html', {'error': 'The name is alredy present', 'cat': cate})
            desc = request.POST.get('desc')
            categ = request.POST.get('categ')
            try:
                img = request.FILES['img']
            except MultiValueDictKeyError:
                img=None
            slug = slugify(name)
            author = request.POST['author']
        except:
            cate = categories.objects.all()
            return render(request,'add.html',{'error':'Fill all necessary fields then retry','cat':cate})
        cat=categories.objects.get(slug=categ)
        s= books.objects.create(name=name,slug=slug,categ=cat,desc=desc,img=img,author=author)
        s.save()
        return redirect('adminpanel')
    cat=categories.objects.all()
    return render(request,'add.html',{'cat':cat})

def add_cat(request):
    try:
        name = request.POST.get('name')
        if categories.objects.filter(name=name).exists():
            cat = categories.objects.all()
            return render(request, 'adminpanel.html', {'error': 'Category already exists','cat':cat})
        slug=slugify(name)
    except:
        return render(request, 'adminpanel.html', {'error': 'Fill the field then retry'})
    s=categories(name=name,slug=slug)
    s.save()
    return redirect('adminpanel')

class Edit(UpdateView):
    model = categories
    template_name = 'edit.html'
    fields = ('name','slug')
    def get_success_url(self):
        return reverse('adminpanel')

class Bkedit(UpdateView):
    model = books
    template_name = 'edit.html'
    fields = ('name','slug','author','desc','img')
    def get_success_url(self):
        return reverse_lazy('details',kwargs={'ct_slug':self.object.categ.slug,'bk_slug':self.object.slug})

def search(request):
    query=request.GET['search']
    categ = categories.objects.all()
    book = books.objects.filter(Q(name__contains=query)|Q(desc__contains=query)|Q(author__contains=query))
    return render(request, 'index.html', {'books': book, 'categ': categ})