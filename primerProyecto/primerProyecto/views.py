from django.http import HttpResponse

#Funcion vista o función vista 
def greeting(request):

    return HttpResponse("Hola, priimera pagina con Django ;)")

def farewell(request):
    return HttpResponse("Hasta la próxima amigos")