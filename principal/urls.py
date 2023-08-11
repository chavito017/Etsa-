from django.urls import path
from principal.views import *

urlpatterns = [
    
    path('parametros/',Parametros, name='leerpar'),
#--------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
    
path('Categoriataller/', ListadoCategoriataller.as_view(template_name = "crud/Categoriataller/tables.html"), name='leerre'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Categoriataller/detalle/<int:pk>',CategoriatallerDetalle.as_view(template_name = "crud/Categoriataller/detalle.html"), name='detallesre'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Categoriataller/editar/<int:pk>', CategoriatallerActualizar.as_view(template_name = "crud/Categoriataller/actualizar.html"), name='actualizarre'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Categoriataller/eliminar/<int:pk>', CategoriatallerEliminar.as_view(), name='crud/Categoriataller/eliminar.html'),     
 #---------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
 

# --------------------------------------------------------------------URL Empresa ---------------------------------------------------------------#
    
path('Empresa/', ListadoEmpresa.as_view(template_name = "crud/Empresa/tables.html"), name='leerem'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "crud/Empresa/detalle.html"), name='detallesem'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud/Empresa/actualizar.html"), name='actualizarem'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='crud/Empresa/eliminar.html'),     
# -------------------------------------------------------------------URL Empresa ---------------------------------------------------------------#


#--------------------------------------------------------URL Usuario ------------------------------------------------------------------------#
    
path('Usuario/', ListadoUsuario.as_view(template_name = "crud/Usuario/tables.html"), name='leerru'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Usuario/detalle/<int:pk>',UsuarioDetalle.as_view(template_name = "crud/Usuario/detalle.html"), name='detallesru'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "crud/Usuario/actualizar.html"), name='actualizarru'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='crud/Usuario/eliminar.html'),     
 #---------------------------------------------------URL Usuario ------------------------------------------------------------------------#

path('usuarioC/', ListadoUsuario.as_view(template_name = "tienda/principal.html"), name='tienda1'),
path('usuarioC/tienda/<int:pk>', UsuarioDetalle.as_view(template_name = "tienda/producto.html"), name='tienda'),


#------------------------------------------------------URL Departamento ------------------------------------------------------------------------#   
path('Departamento/', ListadoDepartamento.as_view(template_name = "crud/Departamento/tables.html"), name='leerdep'),

# La ruta 'Departamento' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Departamento/detalle/<int:pk>',DepartamentoDetalle.as_view(template_name = "crud/Departamento/detalle.html"), name='detallesdep'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "crud/Departamento/actualizar.html"), name='actualizardep'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Departamento/eliminar/<int:pk>',DepartamentoEliminar.as_view(), name='crud/Departamento/eliminar.html'),     
#---------------------------------------------------URL Departamento ------------------------------------------------------------------------#

#----------------------------------------------------URL Municipio ------------------------------------------------------------------------#
    
path('Municipio/', ListadoMunicipio.as_view(template_name = "crud/Municipio/tables.html"), name='leermun'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "crud/Municipio/detalle.html"), name='detallesmun'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "crud/Municipio/actualizar.html"), name='actualizarmun'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name='crud/Municipio/eliminar.html'),     
# --------------------------------------------URL Municipio ------------------------------------------------------------------------#

# ---------------------------------------------------URL Categoria Servicio------------------------------------------------------------------------#
path('Categoriaservicio/', ListadoCategoriaservicio.as_view(template_name = "crud/Categoriaservicio/tables.html"), name='leercser'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Categoriaservicio/detalle/<int:pk>', CategoriaservicioDetalle.as_view(template_name = "crud/Categoriaservicio/detalle.html"), name='detallescser'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Categoriaservicio/editar/<int:pk>', CategoriaservicioActualizar.as_view(template_name = "crud/Categoriaservicio/actualizar.html"), name='actualizarcser'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Categoriaservicio/eliminar/<int:pk>', CategoriaservicioEliminar.as_view(), name='crud/Categoriaservicio/eliminar.html'),   
# ---------------------------------------------------URL Categoria Servicio------------------------------------------------------------------------#


#--------------------------------------------------URL tipo empresario ------------------------------------------------------------------------#

path('Tpempresario/', ListadoTpempresario.as_view(template_name = "crud/Tpempresario/tables.html"), name='leertiemp'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Tpempresario/detalle/<int:pk>',TpempresarioDetalle.as_view(template_name = "crud/Tpempresario/detalle.html"), name='detallestiemp'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Tpempresario/editar/<int:pk>', TpempresarioActualizar.as_view(template_name = "crud/Tpempresario/actualizar.html"), name='actualizartiemp'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Tpempresario/eliminar/<int:pk>', TpempresarioEliminar.as_view(), name='crud/Tpempresario/eliminar.html'),     
#---------------------------------------------------URL tipo empresario ------------------------------------------------------------------------#


#-----------------------------------------------------URL servicio ---------------------------------------------------------------------------#

path('Servicio/', ListadoServicio.as_view(template_name = "crud/Servicio/tables.html"), name='leerser'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Servicio/detalle/<int:pk>',ServicioDetalle.as_view(template_name = "crud/Servicio/detalle.html"), name='detallesser'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Servicio/editar/<int:pk>', ServicioActualizar.as_view(template_name = "crud/Servicio/actualizar.html"), name='actualizarser'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Servicio/eliminar/<int:pk>', ServicioEliminar.as_view(), name='crud/Servicio/eliminar.html'),     
#---------------------------------------------------URL servicio ------------------------------------------------------------------------#


#--------------------------------------------------URL agendamiento ------------------------------------------------------------------------#

path('Agendamiento/', ListadoAgendamiento.as_view(template_name = "crud/Agendamiento/tables.html"), name='leerag'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Agendamiento/detalle/<int:pk>',AgendamientoDetalle.as_view(template_name = "crud/Agendamiento/detalle.html"), name='detallesag'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Agendamiento/editar/<int:pk>', AgendamientoActualizar.as_view(template_name = "crud/Agendamiento/actualizar.html"), name='actualizarag'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Agendamiento/eliminar/<int:pk>', AgendamientoEliminar.as_view(), name='crud/Agendamiento/eliminar.html'),     
 #---------------------------------------------------URL agendamiento ------------------------------------------------------------------------#
]
