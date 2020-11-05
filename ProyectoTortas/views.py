from django.http import HttpResponse
from django.shortcuts import render  
from app.models import Producto, Tipo, Cliente


def inicio(request):
    prod = Producto.objects.filter(cod_tipo__lte=1)
    prod2 = Producto.objects.filter(cod_tipo=5)

    return render(request,'index.html', {"productos":prod, "productos2":prod2})

def productos(request):  
    Tip=Tipo.objects.all() 
    produ = Producto.objects.all()   
    return render(request,'productos.html', {"prod":produ,"tipo":Tip})


def registrate(request):             
    ext=True    
    if request.method == "POST": 
        t_doc=request.POST['documento']
        doc=request.POST['ru']
        nombre=request.POST['nombre']
        nac=request.POST['nacimiento']
        genero=request.POST['genero']
        fono=request.POST['telefono']
        email=request.POST['email']
        cont=request.POST['pasword']
        direc=request.POST['direccion']
        ofe = request.POST['acepta']        
        cli = Cliente(nro_doc=doc,tipo_doc=t_doc,nombre_completo=nombre,fecha_nac=nac,genero=genero,telefono=fono,email=email,pasword=cont,direccion=direc,ofertas=ofe)
        cli.save() 
    
    return render(request,'registrate.html', {"ext":ext})


       
def Buscar(request):
    if request.GET["correo"]:
        mensaje=request.GET["correo"]
        pasw =request.GET["pasw"]
        Cli =Cliente.objects.filter(email=mensaje)
        sms="* Correo no Existe, Recupera tu contraseña ingresando correo"
        for c in Cli:
            if c.pasword==pasw:
                sms="Bienvenido"  
            else:  sms="* Contraseña Invalida"   
    return render(request,'registrate.html', {"sms":sms,"Cli":Cli})  


obj=""
def Cambio(request):
    if request.method == "POST": 
        if request.POST['correoElec']:
            c_correo=request.POST['correoElec']
            c_clave1=request.POST['pasw1']            
            obj = Cliente.objects.filter(email=c_correo)
            for a in obj:   
                a.pasword=c_clave1
                a.save()
    return render(request,'registrate.html', {})
    
def carrito(request):
    return render(request,'Carrito.html', {"obj":obj})


