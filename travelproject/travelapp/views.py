from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def demo(request):
    return render(request,"index.html")

def calculate(request):
    if request.method == 'GET':
        n1=float(request.GET['n1'])
        n2=float(request.GET['n2'])
        addition      = n1+n2
        subtraction   =n1-n2
        multiplication =n1*n2
        division      = n1/n2

        dictionary = {
                'num1':n1,
                'num2':n2,
                'addition':addition,
                'subtraction':subtraction,
                'multiplication':multiplication,
                'division':division
              }

        return render(request,"result.html",dictionary)










