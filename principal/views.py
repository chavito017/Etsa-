from django import forms 
from django.shortcuts import redirect, render
from principal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages 
from django.forms.models import modelform_factory


from django import forms 
from django.contrib.auth import authenticate,get_user_model,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .forms import *


class SignUpView(CreateView):
    model = AuthUser
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')





# Create your views here.
def Home(request):
    
    return render (request, "index.html")

def Parametros (request):
    return render (request, "crud/index.html")  

def Login(request):
    return render (request, "login.html")

#registro que guarde a la base de datos 
def usuarios (request):
    usuarioFormulario=modelform_factory(Usuario,exclude=['cotraseña','genero'])
    formulario=usuarioFormulario()
    data={
        'formulario':formulario
    }
    return render(request,'inicio.html', data)

#------------------------------------------------------------------------Categoriataller-----------------------------------------------------#
class ListadoCategoriataller(CreateView,ListView,SuccessMessageMixin):

    model = Categoriataller
    form = Categoriataller
    fields = "__all__"
    
    success_message ='Categoriataller creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class CategoriatallerDetalle (DetailView):
    model =Categoriataller

class CategoriatallerActualizar(SuccessMessageMixin,UpdateView):
    model =Categoriataller
    form = Categoriataller
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Categoriataller Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
class CategoriatallerEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriataller
    form = Categoriataller
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoriataller Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
#---------------------------------------------------------------------fin Categoriataller-----------------------------------------------------#

#------------------------------------------------------------------------Empresa--------------------------------------------------------------#
class ListadoEmpresa(CreateView,ListView,SuccessMessageMixin):

    model = Empresa
    form = Empresa
    fields = "__all__"
    
    success_message ='Empresa creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerem') # Redireccionamos a la vista principal 'leer' 
    
class EmpresaDetalle (DetailView):
    model =Empresa

class EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leeremem') # Redireccionamos a la vista principal 'leer'
    
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerem') # Redireccionamos a la vista principal 'leer'
#--------------------------------------------------------------------fin Empresa-------------------------------------------------------------#  


#----------------------------------------------------------------------usuario---------------------------------------------------------------#
class ListadoUsuario(CreateView,ListView,SuccessMessageMixin):

    model = Usuario
    form = Usuario
    fields = "__all__"
    
    success_message ='Usuario creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class UsuarioDetalle (DetailView):
    model =Usuario

class UsuarioActualizar(SuccessMessageMixin,UpdateView):
    model =Usuario
    form = Usuario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario
    form = Usuario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'

    
#-------------------------------------------------------------------fin usuario---------------------------------------------------------------#


#-----------------------------------------------------------------Departamento----------------------------------------------------------------#
class ListadoDepartamento(CreateView,ListView,SuccessMessageMixin):

    model = Departamento
    form = Departamento
    fields = "__all__"
    
    success_message ='Departamento creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerdep') # Redireccionamos a la vista principal 'leer' 
    
class DepartamentoDetalle (DetailView):
    model =Departamento

class DepartamentoActualizar(SuccessMessageMixin,UpdateView):
    model =Departamento
    form = Departamento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Departamento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerdep') # Redireccionamos a la vista principal 'leer'
    
class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento
    form = Departamento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Departamento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerdep') # Redireccionamos a la vista principal 'leer'
#---------------------------------------------------------------fin Departamento--------------------------------------------------------------#

#--------------------------------------------------------------------Municipio---------------------------------------------------------------#
class ListadoMunicipio(CreateView,ListView,SuccessMessageMixin):

    model = Municipio
    form = Municipio
    fields = "__all__"
    
    success_message ='Municipio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leermun') # Redireccionamos a la vista principal 'leer' 
    
class MunicipioDetalle (DetailView):
    model =Municipio

class MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model =Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leermun') # Redireccionamos a la vista principal 'leer'
    
class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leermun') # Redireccionamos a la vista principal 'leer'
    
#------------------------------------------------------------------fin Municipio--------------------------------------------------------------#


#---------------------------------------------------------------Categoriaservicio-------------------------------------------------------------#
class ListadoCategoriaservicio(CreateView,ListView,SuccessMessageMixin):

    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"
    
    success_message ='Categoriaservicio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leercser') # Redireccionamos a la vista principal 'leer' 
    
class CategoriaservicioDetalle (DetailView):
    model =Categoriaservicio

class CategoriaservicioActualizar(SuccessMessageMixin,UpdateView):
    model =Categoriaservicio
    form = Categoriaservicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Categoriaservicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercser') # Redireccionamos a la vista principal 'leer'
    
class CategoriaservicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoriaservicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercser') # Redireccionamos a la vista principal 'leer'
    
#-------------------------------------------------------------fin Categoriaservicio-----------------------------------------------------------#

#-----------------------------------------------------------------Tipo  Empresario------------------------------------------------------------#
class ListadoTpempresario(CreateView,ListView,SuccessMessageMixin):

    model = Tpempresario
    form = Tpempresario
    fields = "__all__"
    
    success_message ='Tpempresario creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leertiemp') # Redireccionamos a la vista principal 'leer' 
    
class TpempresarioDetalle (DetailView):
    model =Tpempresario

class TpempresarioActualizar(SuccessMessageMixin,UpdateView):
    model =Tpempresario
    form = Tpempresario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Tpempresario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leertiemp') # Redireccionamos a la vista principal 'leer'
    
class TpempresarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Tpempresario
    form = Tpempresario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tpempresario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertiemp') # Redireccionamos a la vista principal 'leer'
    
#--------------------------------------------------------------fin Tipo  Empresario-----------------------------------------------------------#

#----------------------------------------------------------------------servicio---------------------------------------------------------------#

class ListadoServicio(CreateView,ListView,SuccessMessageMixin):

    model = Servicio
    form = Servicio
    fields = "__all__"
    
    success_message ='Servicio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerser') # Redireccionamos a la vista principal 'leer' 
    
class ServicioDetalle (DetailView):
    model =Servicio

class ServicioActualizar(SuccessMessageMixin,UpdateView):
    model =Servicio
    form = Servicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'servicio' de nuestra Base de Datos 
    success_message = 'Servicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerser') # Redireccionamos a la vista principal 'leer'
    
class ServicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Servicio
    form = Servicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerser') # Redireccionamos a la vista principal 'leer'
    
#--------------------------------------------------------------------fin servicio-------------------------------------------------------------#

#--------------------------------------------------------------------Agendamiento-------------------------------------------------------------#

class ListadoAgendamiento(CreateView,ListView,SuccessMessageMixin):

    model = Agendamiento
    form = Agendamiento
    fields = "__all__"
    
    success_message ='Agendamiento creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerag') # Redireccionamos a la vista principal 'leer' 
    
class AgendamientoDetalle (DetailView):
    model =Agendamiento

class AgendamientoActualizar(SuccessMessageMixin,UpdateView):
    model =Agendamiento
    form = Agendamiento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'servicio' de nuestra Base de Datos 
    success_message = 'Agendamiento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerag') # Redireccionamos a la vista principal 'leer'
    
class AgendamientoEliminar(SuccessMessageMixin, DeleteView): 
    model = Agendamiento
    form = Agendamiento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Agendamiento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerag') # Redireccionamos a la vista principal 'leer'
    
#--------------------------------------------------------------------Agendamiento-------------------------------------------------------------#


#---------------------------------------------------------------CategoriaServicio-----------------------------------------------------#
class ListadoCategoriaservicio(CreateView,ListView,SuccessMessageMixin):

    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"
    
    success_message ='Categoriaservicio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer' 
    
class CategoriaservicioDetalle (DetailView):
    model =Categoriaservicio

class CategoriaservicioActualizar(SuccessMessageMixin,UpdateView):
    model =Categoriaservicio
    form = Categoriaservicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'municipio' de nuestra Base de Datos 
    success_message = 'Categoriaservicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer'
    
class CategoriaservicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoriaservicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer'
    
#     #-----------------------------------------------------------servisio-----------------------------------------------------#

#--------------------------------------------------Contrato-----------------------------------------------------#
class ListadoContrato(CreateView,ListView,SuccessMessageMixin):

    model = Contrato
    form = Contrato
    fields = "__all__"
    
    success_message ='Contrato creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer' 
    
class ContratoDetalle (DetailView):
    model =Contrato

class ContratoActualizar(SuccessMessageMixin,UpdateView):
    model =Contrato
    form = Contrato
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Contrato Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer'
    
class ContratoEliminar(SuccessMessageMixin, DeleteView): 
    model = Contrato
    form = Contrato
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Contrato Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer'
    
 #----------------------------------------------fin Contrato-----------------------------------------------------#
