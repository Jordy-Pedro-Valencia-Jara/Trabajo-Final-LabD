from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from comelona.models import platillo
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
         return render(request,'login.html')   
         
def register (request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created') 
                return redirect('login')
        else:
            messages.info(request,'password not matching .. ')
            return redirect('register')
        return redirect('/')
    else:
        return render (request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def create_saucer(request):
    print('crear platillo')
    if request.method=='POST':
        print('creado con post')
        Name=request.POST['Name']
        Platillo_img=request.FILES['Platillo_img']
        Descripcion=request.POST['Descripcion']
        Breve=request.POST['Breve']
        Precio=request.POST['Precio']
        print(Name)
        print(Platillo_img)
        print(Descripcion)
        print(Breve)
        print(Precio)
        imgs=platillo.objects.create(name=Name,img=Platillo_img,desc=Descripcion,Brev=Breve,price=Precio)
        imgs.save()
        print('platillo agregado')
        platos=platillo.objects.all()
    return render (request,'create_saucer.html')
def eliminar(request,id):
    data=platillo.objects.get(id=id)
    data.delete()
    return redirect(to='listar')
def modificar(request,id):
    data=platillo.objects.get(id=id)
    if request.method=='POST':
        data=platillo()
        data.id=request.POST['textid']
        data.name=request.POST['Name']
        data.img=request.FILES['Direccion']
        data.desc=request.POST['Descripcion']
        data.price=request.POST['Precio']
        data.save()
        return redirect('listar')
    return render(request,'modificar.html',{'data':data,})
def listar(request):
    data=platillo.objects.all()
    return render(request,'listar.html',{'data':data,})
