from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Notes,Student
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .forms import NewNotesForm, NewsLetterForm

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def courses_today(request):
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('courses_today')
    else:
        form = NewsLetterForm()
    return render(request, 'today-courses.html', {"date": date, "courses": courses,"letterForm":form})

# def convert_dates(dates):

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
    return render(request, 'profile/edit_profile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user)

    try:
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request, 'profile/profile.html', {'profile': prof, 'projects': projects})


def past_days_courses(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(courses_today)

    courses = Notes.days_courses(date)
    return render(request, 'past-courses.html', {"date": date, "courses": courses})


def search_results(request):

    if 'notes' in request.GET and request.GET["notes"]:
        search_term = request.GET.get("notes")
        searched_notes = Notes.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "notes": searched_notes})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def notes(request, notes_id):
    try:
        notes = Notes.objects.get(id=notes_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "notes.html", {"notes": notes})

@login_required(login_url='/accounts/login/')
def new_notes(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNotesForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.student = current_user
            notes.save()
        return redirect('welcome')

    else:
        form = NewNotesForm()
    return render(request, 'new_notes.html', {"form": form})