from board.models import Board
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PopupForm, FrontForm, MainBoardForm, EmailForm, ClubsForm, MaintenanceForm, TermsForm
from common.models import ClubInfo

def main(request):
    if request.user.is_superuser:
        return render(request, 'manager/main.html')
    else:
        return redirect('/')

def maintenance(request):
    if request.user.is_superuser:
        if request.method == "GET":
            maintenanceForm = MaintenanceForm()
            context = {'maintenanceForm':maintenanceForm}
            return render(request, 'manager/maintenance.html', context)
        elif request.method == "POST":
            maintenanceForm = MaintenanceForm(request.POST)
            if maintenanceForm.is_valid():
                maint = maintenanceForm.save(commit=False)
                maint.save()
                return redirect('/')
    else:
        return redirect('/')

def popup(request):
    if request.user.is_superuser:

        if request.method == "GET":
            popupForm = PopupForm()
            context = {'popupForm': popupForm}
            return render(request, 'manager/popup.html', context)

        elif request.method == "POST":
            popupForm = PopupForm(request.POST)
            if popupForm.is_valid():
                popup2 = popupForm.save(commit=False)
                popup2.file1 = request.FILES.get("file1")
                popup2.save()
                return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')


def terms(request):
    if request.user.is_superuser:

        if request.method == "GET":
            termsForm = TermsForm()
            context = {'termsForm': termsForm}
            return render(request, 'manager/terms.html', context)

        elif request.method == "POST":
            termsForm = TermsForm(request.POST)
            if termsForm.is_valid():
                terms2 = termsForm.save(commit=False)
                terms2.file1 = request.FILES.get("file1")
                terms2.file2 = request.FILES.get("file2")
                terms2.file3 = request.FILES.get("file3")
                terms2.save()
                return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')


def email(request):
    if request.user.is_superuser:
        if request.method == "GET":
            emailForm = EmailForm()
            context = {'emailForm': emailForm}
            return render(request, 'manager/email.html', context)

        elif request.method == "POST":
            emailForm = EmailForm(request.POST)
            if emailForm.is_valid():
                email2 = emailForm.save(commit=False)

                email2.save()
                return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')

def delete_club(request):
    if request.user.is_superuser:
        info = ClubInfo.objects.filter()

        context = {'clubs': info}
        return render(request, 'manager/delete_club.html', context)
    else:
        return redirect('/')


def delete(request, bid):
    post = get_object_or_404(ClubInfo, id=bid)

    if request.user.is_superuser:
        post = ClubInfo.objects.get(id=bid)
        post.delete()
        return redirect('/manager/delete_club')





def front(request):
    if request.user.is_superuser:
        if request.method == "GET":
            frontForm = FrontForm()
            context = {'frontForm': frontForm}
            return render(request, 'manager/front.html', context)

        elif request.method == "POST":
            frontForm = FrontForm(request.POST)
            if frontForm.is_valid():
                front2 = frontForm.save(commit=False)
                front2.file1 = request.FILES.get("file1")
                front2.file2 = request.FILES.get("file2")
                front2.file3 = request.FILES.get("file3")
                front2.save()
                return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')


def clubs(request):
    if request.user.is_superuser:
        if request.method == "GET":
            clubsForm = ClubsForm()
            context = {'clubsForm': clubsForm}
            return render(request, 'manager/clubs.html', context)

        elif request.method == "POST":
            clubsForm = ClubsForm(request.POST)
            if clubsForm.is_valid():
                clubs2 = clubsForm.save(commit=False)
                clubs2.file1_1 = request.FILES.get("file1-1")
                clubs2.file1_2 = request.FILES.get("file1-2")
                clubs2.file1_3 = request.FILES.get("file1-3")
                clubs2.file2_1 = request.FILES.get("file2-1")
                clubs2.file2_2 = request.FILES.get("file2-2")
                clubs2.file2_3 = request.FILES.get("file2-3")
                clubs2.file3_1 = request.FILES.get("file3-1")
                clubs2.file3_2 = request.FILES.get("file3-2")
                clubs2.file3_3 = request.FILES.get("file3-3")
                clubs2.file4_1 = request.FILES.get("file4-1")
                clubs2.file5_1 = request.FILES.get("file5-1")
                clubs2.save()
                return redirect('/')

        else:
            return redirect('/')
    else:
        return redirect('/')

def main_board(request):
    if request.user.is_superuser:
        if request.method == "GET":
            mainBoardForm = MainBoardForm()
            board_title = Board.objects.filter()
            context = {'mainBoardForm': mainBoardForm, 'Board': board_title}
            return render(request, 'manager/main_board.html', context)

        elif request.method == "POST":
            mainBoardForm = MainBoardForm(request.POST)
            if mainBoardForm.is_valid():
                board3 = mainBoardForm.save(commit=False)
                board3.save()
                return redirect('/')

        else:
            return redirect('/')

    else:
        return redirect('/')