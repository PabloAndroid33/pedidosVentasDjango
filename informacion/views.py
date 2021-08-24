from django.shortcuts import render

# Create your views here.

def informacion(request):

    return render(request,"informacion/informacion.html")
  #  return HttpResponse("Inicio")

