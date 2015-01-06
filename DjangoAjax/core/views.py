# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

def hello(request):
    return HttpResponse('Olá Visitante')

def home(request):
    contexto = RequestContext(request)
    return render_to_response('index.html', {'nome':'Fernando Parreira', 'fones':[{'fixo':'111','celular':'222'}], 'cidade':'Votuporanga'}, contexto)    

def mensagem(request):
    return render(request, 'mensagem.html')