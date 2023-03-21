from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CSVForm
from .models import Team, Game

def home(request):
    """ This is home view """
    return render(request, 'rankings/home.html')


def upload(request):
    """ This view allows user to upload CSV """
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
        # print(file_data)
        # teams = {'test':'test1'}

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
    
        messages.success(request, 'CSV uploaded successfully.')

        # pass string to be edited
        return HttpResponseRedirect(reverse('update', kwargs={'data': file_data}))
    
    return render(request, 'rankings/form_upload.html')
    

def update(request, data):
    """ This view allow user to update uploaded CSV """
    if request.method == 'POST':

        ranks = {}
        
        # process data from updated CSV form
        form = CSVForm(request.POST)
        
        if form.is_valid():
            game_data = form.cleaned_data.get('content')
            lines = game_data.split("\n")

        for row in lines:
            line = row.split(',')
            if len(line) != 4:
                messages.error(request, 'Invalid CSV format.')
                return HttpResponseRedirect(reverse('upload'))
            team1_name, team1_score, team2_name, team2_score = [l.rstrip(' ').lstrip(' ') for l in line]
            
            if team1_name == team2_name:
                messages.error(request, 'Team names cannot be the same.')
                return HttpResponseRedirect(reverse('upload'))
            
            try:
                team1_score = int(team1_score)
                team2_score = int(team2_score)
            except ValueError:
                messages.error(request, 'Scores must be integers.')
                return HttpResponseRedirect(reverse('upload'))
            
            if team1_name not in ranks.keys():
                ranks[team1_name] = 0

            if team2_name not in ranks.keys():
                ranks[team2_name] = 0
            
            if team1_score == team2_score:
                ranks[team1_name] += 1
                ranks[team2_name] += 1
            elif team1_score < team2_score:
                ranks[team1_name] += 0
                ranks[team2_name] += 3
            elif team1_score > team2_score:
                ranks[team1_name] += 3
                ranks[team2_name] += 0    
        
        # sort by points, then by name if the points are similar
        sorted_team_rank = sorted(ranks.items(), key=lambda x: (-x[1],x[0]))
        converted_rank = '\n'.join(f'{val[0]},{val[1]}' for val in sorted_team_rank)
        # print(converted_rank)

        return HttpResponseRedirect(reverse('ranking', kwargs={'data': converted_rank}))
    
    context = {}
    initial_dict = {"content": data}
    form = CSVForm(request.POST or None, initial=initial_dict)
    context['form'] = form
    return render(request, 'rankings/list_update.html', context)


def ranking(request, data):
    """ This view just generate temporary ranking based on uploaded CSV """
    context, ranks = {}, {}
    
    lines = data.split("\n")

    for row in lines:
        line = row.split(',')
        ranks[line[0]] = line[1]
    
    context['ranks'] = ranks

    return render(request, 'rankings/temporary_ranking.html', context)


def savegame(request, data):
    """ [2nd Sprint] This view will enable user to save uploaded games from CSV to database """
    # team1 = Team.objects.get_or_create(name=team1_name)
    # team2 = Team.objects.get_or_create(name=team2_name)
            
    # game = Game(team_1=team1, team_2=team2)
    # game.save()

    pass