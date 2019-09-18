from django.shortcuts import render
from BRMapp import models
from BRMapp.forms import NewBookForm,SearchForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/BRMapp/login/')
def editBook(request):
    b=models.book.objects.get(id=request.GET['bookid'])
    fields={'title':b.title,'author':b.author,'price':b.price,'publisher':b.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'b':b})
    return res
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/BRMapp/view-book/')
        else:
            data['error']="incorrect username or password"
            return render(request,'BRMapp/user_login.html',data)
    else:
        return render(request,'BRMapp/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMapp/login/')

@login_required(login_url='/BRMapp/login/')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        b=models.book()
        b.id=request.POST['bookid']
        b.title=form.data['title']
        b.author=form.data['author']
        b.price=form.data['price']
        b.publisher=form.data['publisher']
        b.save()
    return HttpResponseRedirect('BRMapp/view-book')

@login_required(login_url='/BRMapp/login/')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-book')

@login_required(login_url='/BRMapp/login/')
def searchBook(request):
    form=SearchForm()
    return render(request,'BRMapp/search_book.html',{'form':form})

@login_required(login_url='/BRMapp/login/')
def search(request):
    form=SearchForm(request.POST)
    books=models.book.objects.filter(title=form.data['title'])
    return render(request,'BRMapp/search_book.html',{'form':form,'books':books})

@login_required(login_url='/BRMapp/login/')
def viewbook(request):
    books=models.book.objects.all()
    username=request.session['username']
    return render(request,'BRMapp/view_book.html',{'books':books,'username':username})

@login_required(login_url='/BRMapp/login/')
def newbook(request):
    f=NewBookForm()
    return render(request,'BRMapp/new_book.html',{'f':f})

@login_required(login_url='/BRMapp/login/')
def add(request):
    if request.method=='POST':
        f=NewBookForm(request.POST)
        b=models.book()
        b.title=f.data['title']
        b.author=f.data['author']
        b.price=f.data['price']
        b.publisher=f.data['publisher']
        b.save()
    s="record stored <br> <a href='/BRMapp/view-book'>view all books</a>"
    return HttpResponse(s)
