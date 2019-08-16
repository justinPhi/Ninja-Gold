from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if 'goldTotal' not in request.session or 'activities' not in request.session:
        request.session['goldTotal'] = 0
        request.session['activities'] = []
        print(request.session['goldTotal'])
    return render(request, "ninjaGoldApp/index.html")

def processMoney(request):
    if request.method == "POST":
        if request.POST['places'] == 'farm':
            gold = random.randint(10,21)
            request.session['activities'].append('You earned ' +str(gold) + ' gold from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        
        elif request.POST['places'] == 'cave':
            gold = random.randint(5, 11)
            request.session['activities'].append('You earned ' +str(gold) + ' gold from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['places'] == 'house':
            gold = random.randint(2,6)
            request.session['activities'].append('You earned ' +str(gold) + ' gold from the ' + request.POST['places'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        elif request.POST['places'] == 'casino':
             gold = random.randint(-50, 51)
             if gold >= 0:
                request.session['activities'].append('Entered a casino and earned ' +str(gold) + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
             else:
                request.session['activities'].append('Entered a casino and lost ' +str(gold) + ' gold... Ouch... ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        request.session['goldTotal'] += gold
        print(request.session['goldTotal'])
    return redirect('/')

def resetGold(request):
    if request.method == "POST":
        request.session['goldTotal'] = 0
        request.session['activities'] =[]
    return redirect('/')
        
