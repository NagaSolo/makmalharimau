from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CSVForm
from .models import Team, Game

def home(request):
    return render(request, 'rankings/home.html')


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['csv_file']
        
        if not uploaded_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("upload"))
        
        #if file is too large, return
        if uploaded_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (uploaded_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("upload"))

        file_data = uploaded_file.read().decode("utf-8")
        lines = file_data.split("\n")
        print(file_data)
        teams = {'test':'test1'}
        #loop over the lines and save them in db. If error , store as string and then display
        for row in lines:
        # for row in csv.reader(uploaded_file):
            line = row.split(',')
            if len(line) != 4:
                messages.error(request, 'Invalid CSV format.')
                return HttpResponseRedirect(reverse('upload'))
            team1_name, team1_score, team2_name, team2_score = line
            
            if team1_name == team2_name:
                messages.error(request, 'Team names cannot be the same.')
                return HttpResponseRedirect(reverse('upload'))
            
            try:
                team1_score = int(team1_score)
                team2_score = int(team2_score)
            except ValueError:
                messages.error(request, 'Scores must be integers.')
                return HttpResponseRedirect(reverse('upload'))
            
            # team1 = Team.objects.get_or_create(name=team1_name)
            # team2 = Team.objects.get_or_create(name=team2_name)
            
            # game = Game(team_1=team1, team_2=team2)
            # game.save()

            
        messages.success(request, 'Games uploaded successfully.')
        initial = {'body': file_data}
        form = CSVForm(request.POST or None, initial=initial)
        # return HttpResponseRedirect(reverse('update'), {"form": form})
        return render(request, 'rankings/list_update.html', context={"form":form})
    return render(request, 'rankings/form_upload.html')
    

def update(request):
    return render(request, 'rankings/list_update.html')