from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Cards,Profile

# Create your views here.


def home(request):
    return render(request, 'index.html')


def notes_of_day(request):
   # date = dt.date.today()
    #html = f'''
        #<html>
           # <body>
                #<h1>Notes for {day} {date.day}-{date.month}-{date.year}</h1>
            #</body>
        #</html>
      #'''
    #return HttpResponse(html)


#def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    Cards = Cards.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'cards':cards})


     
def search_results(request):
    
    if 'card' in request.GET and request.GET["card"]:
        search_term = request.GET.get("card")
        searched_cards = Card.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"cards": searched_cards})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')    
def card(request,card_id):
    try:
        card = Card.objects.get(id = card_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"card.html", {"card":card})

@login_required(login_url='/accounts/login/')
def new_card(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = current_user
            card.save()
        return redirect('home')
    else:
        form = NewArticleForm()
    return render(request, 'new_card.html', {"form": form})
