from datetime import datetime, date, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from notation.models import NotationTable, NotesCategories, Note


# Create your views here.


@login_required
def index(request):
    return render(request, "notation/index.html")


@login_required
def notes(request):
    if NotationTable.objects.filter(user=request.user, date=date.today()):
        return redirect('notation-profile')
    return render(request, "notation/notation.html")


@login_required
def note_jours(noteTable):
    # Pour récuperer la note moyenne
    note_moyenne = 0
    notes = Note.objects.filter(table=noteTable)
    date_du_jour = noteTable.date

    for note in notes:
        note_moyenne += note.valeur

    note_moyenne = round(note_moyenne / 4)
    note_moyenne = {
        'moyenne': note_moyenne,
        'date': noteTable.date
    }

    return note_moyenne


@login_required
def profile(request):
    # moyenne de toute les note

    # pour récupérer les notes des jours passé

    # time = datetime.datetime.now(timezone.utc) - datetime.timedelta(hours= 1)
    # query = Article.objects.filter(date_created__gt=time)
    notes = []
    length_notes = NotationTable.objects.filter(user=request.user).count()
    moyennes = []
    for noteTable in NotationTable.objects.filter(date__gt=(date.today() - timedelta(days=30)), user=request.user).order_by("-date"):
        moyennes.append(note_jours(noteTable))

    moyennesTabs = []
    if length_notes < 11:
        for i in range(0, length_notes):
            moyennesTabs.append(moyennes[i])
    else:
        for i in range(0, 11):
            moyennesTabs.append(moyennes[i])

    moyenne_productivity = 0
    moyenne_mood = 0
    moyenne_sociability = 0
    moyenne_sleep = 0

    for note in NotationTable.objects.filter(user=request.user):
        note_productivity = Note.objects.get(table=note, categories=1).valeur
        moyenne_productivity += note_productivity

        note_mood = Note.objects.get(table=note, categories=2).valeur
        moyenne_mood += note_mood

        note_sociability = Note.objects.get(table=note, categories=3).valeur
        moyenne_sociability += note_sociability

        note_sleep = Note.objects.get(table=note, categories=4).valeur
        moyenne_sleep += note_sleep

    moyenne_productivity = round(moyenne_productivity / length_notes, 1)
    moyenne_mood = round(moyenne_mood / length_notes, 1)
    moyenne_sociability = round(moyenne_sociability / length_notes, 1)
    moyenne_sleep = round(moyenne_sleep / length_notes, 1)

    context = {
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "note_jours": notes,
        "moyennes": moyennesTabs,
        "nb_notes": length_notes,
        "moyenne_productivity": moyenne_productivity,
        "moyenne_mood": moyenne_mood,
        "moyenne_sociability": moyenne_sociability,
        "moyenne_sleep": moyenne_sleep,
    }

    return render(request, "notation/profile.html", context)


@login_required
def post_note(request, *args, **kwargs):
    if not NotationTable.objects.filter(user=request.user, date=date.today()):


        notationTable = NotationTable()

        notationTable.user = request.user
        notationTable.date = date.today()
        notationTable.save()

        idNotationtable = NotationTable.objects.get(user=request.user, date=date.today())
        print(request.POST)

        for categorie in NotesCategories.objects.all():
            note = Note()

            note.valeur = request.POST.get(categorie.title)
            print(note.valeur)
            note.table = idNotationtable

            note.categories = categorie
            note.save()
    return redirect('notation-profile')


@login_required
def profile_modif(request):

    # pour récupérer les notes des jours passé

    # time = datetime.datetime.now(timezone.utc) - datetime.timedelta(hours= 1)
    # query = Article.objects.filter(date_created__gt=time)
    notes = []
    length_notes = NotationTable.objects.filter(user=request.user).count()
    moyennes = []
    for noteTable in NotationTable.objects.filter(date__gt=(date.today() - timedelta(days=30)),user=request.user).order_by("-date"):
        moyennes.append(note_jours(noteTable))

    moyennesTabs = []
    if length_notes < 11:
        for i in range(0, length_notes):
            moyennesTabs.append(moyennes[i])
    else:
        for i in range(0, 11):
            moyennesTabs.append(moyennes[i])

    moyenne_productivity = 0
    moyenne_mood = 0
    moyenne_sociability = 0
    moyenne_sleep = 0

    for note in NotationTable.objects.filter(user=request.user):
        note_productivity = Note.objects.get(table=note, categories=1).valeur
        moyenne_productivity += note_productivity

        note_mood = Note.objects.get(table=note, categories=2).valeur
        moyenne_mood += note_mood

        note_sociability = Note.objects.get(table=note, categories=3).valeur
        moyenne_sociability += note_sociability

        note_sleep = Note.objects.get(table=note, categories=4).valeur
        moyenne_sleep += note_sleep

    moyenne_productivity = round(moyenne_productivity / length_notes, 1)
    moyenne_mood = round(moyenne_mood / length_notes, 1)
    moyenne_sociability = round(moyenne_sociability / length_notes, 1)
    moyenne_sleep = round(moyenne_sleep / length_notes, 1)

    context = {
        "username": request.user.username,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "note_jours": notes,
        "moyennes": moyennesTabs,
        "nb_notes": length_notes,
        "moyenne_productivity": moyenne_productivity,
        "moyenne_mood": moyenne_mood,
        "moyenne_sociability": moyenne_sociability,
        "moyenne_sleep": moyenne_sleep,
    }

    return render(request, "notation/profile_modif.html", context)


@login_required
def post_profile(request, *args, **kwargs):
    user = User.objects.get(pk=request.user.id)

    new_last_name = request.POST.get('last_name')
    if new_last_name == "":
        user.last_name = user.last_name
    else:
        user.last_name = new_last_name

    new_first_name = request.POST.get('first_name')
    if new_first_name == "":
        user.first_name = user.first_name
    else:
        user.first_name = new_first_name

    new_email = request.POST.get('email')
    if new_email == "":
        user.email = user.email
    else:
        user.email = new_email

    new_username = request.POST.get('username')
    if new_username == "":
        user.username = user.username
    else:
        user.username = new_username

    user.save()

    return redirect('notation-profile')
