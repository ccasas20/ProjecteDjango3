from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from .models import *
# Create your views here.

def index(request):

    return render(request,"index.html")

def preguntes(request):
    Questions=Question.objects.all()
    Choices=Choice.objects.all()
    QuestionsAndChoices= []
    
    for q in Questions:
        qchoices = Choice.objects.filter(question_id=q).order_by('choice_id')
        QuestionContent={'id':q.question_id,  'text':q.question_text}
        ChoicesContent = {}
        
        for qc in qchoices:
            ChoicesContent.update({qc.choice_id: qc.choice_text} )
            
        QuestionsAndChoices.append({'Question':QuestionContent, 'Choices':ChoicesContent})
    
    
    return render(request,"preguntes.html", {"QuestionsAndChoices": QuestionsAndChoices} )
    
def resultats(request):
    if request.method=='GET':
      nom = request.GET.get('nom', '')
      results=[0,0,0,0]
      Choices=Choice.objects.all()
      rol=""
      roldesc=""
      for q in Choices:
        idchoice = request.GET.get(q.question_id.question_id , '')
        if idchoice == q.choice_id:
          results[0]+=q.value1
          results[1]+=q.value2
          results[2]+=q.value3
          results[3]+=q.value4
      if results[0] == max(results):
         rol="Coordinador"
         roldesc="Hauràs de revisar la feina, designar tasques i revisar que cadascú desenvolupi la seva part del treball. Hauràs de resoldre els possibles conflictes que sorgeixen entre els membres del grup."
      elif results[1] == max(results):
         rol="Supervisor"
         roldesc="Hauràs de revisar els criteris de correcció i revisar la feina de la resta de membres del grup per assegurar-te que s'ajusten als criteris de correcció donats pel professor per assegurar la nota més alta possible."
         
      elif results[2] == max(results):
         rol="Expert"
         roldesc="Si un membre del grup no pot resoldre un problema, hauràs d'investigar com resoldre aquest problema a nivell tècnic per ajudar-lo a resoldre la seva tasca. No hauràs de resoldre el seu problema, però si hauràs de donar-li suport."
         
      elif results[3] == max(results):
         rol="Secretari"         
         roldesc="Revisa el material de l'assignatura, l'aspecte ofimàtic del treball que s'entregarà. Faràs les actes de les reunions i portaràs un registre dels acords realitzats."         
         
      dataresultats={'nom':nom, 'results':results,'rol':rol,'roldesc':roldesc}
      
      
      return render(request,"resultats.html", {'dataresultats':dataresultats})
    else:
      return render(request,"resultatsnull.html")



    
