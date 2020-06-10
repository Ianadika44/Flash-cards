from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
# Create your views here.


def welcome(request):
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
    projects = Project.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'projects':projects})


     