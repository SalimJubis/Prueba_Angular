from django.views import View
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from django.http.response import  HttpResponseBase, JsonResponse
import json
# Create your views here.
class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,mail=""):
        if (len(mail)>0):
            usuario=list(Usuario.objects.filter(mail=mail).values())
            if len(usuario)>0:
                usuarios=usuario[0]
                datos={'message':"exito", 'usuario':usuarios}
            else:
                datos={'message':"usuarios no encontrados"}
            return JsonResponse(datos)
        else:
            usuario=list(Usuario.objects.values())
            if len(usuario)>0:
                datos={'message':"exito", 'usuario':usuario}
            else:
                datos={'message':"usuarios no encontrados"}
            return JsonResponse(datos)
        

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Usuario.objects.create(nombre=jd['nombre'],contrasena=jd['contrasena'],mail=jd['mail'])
        datos={'message': 'exito'}
        return JsonResponse(datos)


    def put(self, request,mail):
        jd=json.loads(request.body)
        usuario=list(Usuario.objects.filter(mail=mail).values())
        if len(usuario)>0:
            usuarios=Usuario.objects.get(mail=mail)
            usuarios.nombre=jd['nombre']
            usuarios.contrasena=jd['contrasena']
            usuarios.mail=jd['mail']
            usuarios.save()
            datos={'message': 'exito'}
        else:
            datos={'message':"usuarios no encontrados"}
        return JsonResponse(datos)


    def delete(self, request, mail):
        usuario = list(Usuario.objects.filter(mail=mail).values())
        if len(usuario) > 0:
            Usuario.objects.filter(mail=mail).delete()
            datos={'message': 'exito'}
        else:
            datos={'message':"usuarios no encontrados"}
        return JsonResponse(datos)

