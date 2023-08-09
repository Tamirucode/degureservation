# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Table, Book
from django.contrib.auth.models import User
from decimal import Decimal


def home(request):
    return render(request, 'nesi/home.html')
  

def menu(request):
    return render(request, 'nesi/menu.html')
    

def about(request):
    return render(request, 'nesi/about.html')
    

def contact(request):
    if request.method == 'POST':
        print('Hello! is anybody there?')
    return render(request, 'nesi/contact.html')
    

def findtable(request):
    context = {}
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        reservt = request.POST.get('reservt')
        table_list = Table.objects.filter()
        if table_list:
            return render(request, 'nesi/table_list.html', locals())
        else:
            context["error"] = "Sorry table is not avilable"
            return render(request, 'nesi/failure.html', context)
    else:
        return render(request, 'nesi/findtable.html')


def bookings(request):
    context = {}
    if request.method == 'POST':
        id_table = request.POST.get('table_id')
        booked_table = int(request.POST.get('booked_table'))
        table = Table.objects.get(id=id_table)
        if table:
            if table.reservt >= int(booked_table):
                table_name = table.table_name
                date = table.date
                booked_table = table.booked_table
                time = table.time
                username = request.user.username 
                email = request.user.email
                user_id = request.user.id
                x = table.reservt - booked_table
                Table.objects.filter(id=id_table).update(reservt=x)
                book = Book.objects.create(name=username, email=email, tableid=id_table, userid=user_id,
                       table_name =table_name,  booked_table=booked_table, date=date, time=time)
                # if table:
                   # name= username
                   
                   # table = Table.objects.get(id=book.tableid)
                    
                   # name = book.id
                    #check_existing = Book.objects.filter(name=name).exists
                    
                    #print('------------name-----------', name)
                   # if check_existing:
                       # return HttpResponse('you already booked table!! try again with other username')
                        
                    
                print('------------book id-----------', book.id)
                book.save()
                
                return render(request, 'nesi/bookings.html', locals())
            else:
                context["error"] = "Sorry table is fullybooked"
                return render(request, 'nesi/error.html', context)

    else:
        return render(request, 'nesi/findtable.html')

    
def deleting(request):
    context = {}
    if request.method == 'POST':
        id_table = request.POST.get('table_id')
        booked_table = int(request.POST.get('booked_table'))

        try:
            book = Book.objects.get(id=id_table)
            table = Table.objects.get(id=book.tableid)
            x = table.reservt + book.booked_table
            Table.objects.filter(id=book.tableid).update(reservt=x)
            # reservt = table.reservt - booked_table
            Book.objects.filter(id=id_table).delete()
            Book.objects.filter(id=id_table).update(booked_table=0)
            return redirect('mybookings')
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that table, please try one more time with valid booking id "
            return render(request, 'nesi/error.html', context)
    else:
        return render(request, 'nesi/findtable.html')


def mybookings(request):
    context = {}
    id_table = request.user.id
    book_list = Book.objects.filter(userid=id_table)
    if book_list:
        return render(request, 'nesi/book_list.html', locals())
    else:
        context["error"] = "Sorry no table booked"
        return render(request, 'nesi/book_list.html', context)


