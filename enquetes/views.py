from django.shortcuts import render
from django.http import HttpResponse
from enquetes.models import Enquete


def bemvindo(request):
    return render(request, 'bemvindo.html')


def enquete(request, enquete_id):
    enquete = Enquete()

    if enquete_id == 1:
        enquete = Enquete("Qual o seu nome?",
                          "Em qual cidade voce nasceu?",
                          "Qual a sua faculdade que voce cursa?",
                          "2020-08-25")

    if enquete_id == 2:
        enquete = Enquete("Quantas horas por semana voce usa redes sociais?",
                          "Quantas horas por semana voce passa jogando?",
                          "Quantas horas por semana voce passa estudando?",
                          "2020-08-26")

    if enquete_id == 3:
        enquete = Enquete("Qual linguagem de programacao voce esta estudando?",
                          "Quando voce iniciou os estudos nessa linguagem?",
                          "Por qual meio voce esta estudando? (livro, youtube, cursos, etc)",
                          "2020-08-27")
    return render(request, 'enquete.html', {"enquete": enquete})
