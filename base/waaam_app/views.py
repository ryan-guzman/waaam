from django.shortcuts import render, redirect

from .forms import VolunteerRecordForm, FilterForm, AddVolunteerForm
from .models import VolunteerRecord

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import csv

from django.contrib.auth.models import User


def export_csv(request, start_date, end_date):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="volunteer_history: {} to {}.csv"'.format(
        start_date, end_date)

    writer = csv.writer(response)
    writer.writerow(['Volunteer', 'Date', 'Hours',
                     'Description', 'Supervisor', 'Group'])

    if request.user.is_superuser:
        records = VolunteerRecord.objects.all().filter(
            date__range=[start_date, end_date])
    else:
        records = VolunteerRecord.objects.filter(
            owner=request.user, date__range=[start_date, end_date])

    records = list(records)
    records.sort(key=lambda rec: rec.date, reverse=True)

    for record in records:
        volunteer = record.owner.first_name + ' ' + record.owner.last_name
        date = record.date
        hours = record.hours
        desc = record.activity
        supervisor = record.supervisor
        group = record.owner.profile.group
        writer.writerow((volunteer, date, hours, desc, supervisor, group))

    return response


@login_required
def export(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            response = export_csv(request, start, end)
            return response
        else:
            print("form not valid")
    else:
        form = FilterForm()
    return render(request, 'export.html', {'form': form})


def add_volunteer(request):
    if request.method == "POST":

        form = AddVolunteerForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            uname = fname + "." + lname

            user = User(
                username=uname,
                first_name=fname,
                last_name=lname,
            )
            user.set_unusable_password()  # does not save...
            user.save()
            return redirect('/')
        else:
            print("form not valid")
    else:
        form = AddVolunteerForm()
    return render(request, "add_vol.html", {"form": form})


def success(request):
    return render(request, "success.html")


# @login_required
def add_individual_hours(request):
    if request.method == "POST":
        form = VolunteerRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            # record.owner = request.user
            record.save()

            return redirect('/success')
        else:
            print("form not valid")
    else:
        form = VolunteerRecordForm()

    return render(request, "add_individual_hours.html", {"form": form, "user": request.user})


# @login_required
def history(request):
    records = VolunteerRecord.objects.all()
    running_total = sum(rec.hours for rec in records)
    if records.count() > 10:
        records = records[records.count() - 10:]
    records = list(records)
    records.sort(key=lambda rec: rec.date, reverse=True)
    return render(request, "history.html", {"records": records, "running_total": running_total})


def json(request):
    from django.http import JsonResponse
    return JsonResponse([
        "Google Cloud Platform",
        "Amazon AWS",
        "Docker",
        "Digital Ocean"
    ])
