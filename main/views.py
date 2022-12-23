from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .form.producto import ProductoForm
from .form.imagen import ImagenForm
from .form.user import UserForm
from .form.contact import FormContact
from main.models import Producto, Imagen, MyContact, Iteraciones


class LoginPage(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            obj = MyContact.objects.filter(have_contact=True)
            for i in obj:
                if i.user == request.user:
                    return redirect('index')
            return redirect('contact')
        form = UserForm()
        return render(request, 'login.html', {'form': form})


class RegisterPage(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm()
        context = {'form': formRegisterUser}
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm(request.POST)
        if formRegisterUser.is_valid():
            formRegisterUser.save()
            return redirect('login')
        return render(request, 'register.html', {'form': formRegisterUser})


class LogoutUser(ListView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class Index(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        imagen = Imagen.objects.all()
        producto = Producto.objects.all()
        contacto = MyContact.objects.all()
        eje = MyContact.objects.filter(have_contact=True)
        return render(request, 'index.html', {'imagen': imagen, 'producto': producto, 'contacto': contacto, 'eje': eje})


class Contact(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        contact = FormContact()
        return render(request, 'contact.html', {'contact': contact})

    def post(self, request, *args, **kwargs):
        contact = FormContact(request.POST)
        if contact.is_valid():
            name = contact.cleaned_data['name']
            email = contact.cleaned_data['email']
            phone = contact.cleaned_data['phone']
            user = request.user
            have_contact = True
            MyContact.objects.create(name=name, email=email, phone=phone, user=user, have_contact=have_contact)
            return redirect('index')
        contact = FormContact()
        return render(request, 'contact.html', {'contact': contact})


class Post(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'post.html')


class About(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class AddProducto(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        imagen = ImagenForm()
        producto = ProductoForm()
        context = {'producto': producto, 'imagen': imagen}
        return render(request, 'add_producto.html', context)

    def post(self, request, *args, **kwargs):
        producto = ProductoForm(request.POST)
        if producto.is_valid():
            nombre = producto.cleaned_data['nombre']
            prcio = producto.cleaned_data['precio']
            usuario = request.user
            categoria = producto.cleaned_data['categoria']
            obj = Producto.objects.create(nombre=nombre, precio=prcio, usuario=usuario, categoria=categoria)
            return redirect('add_imagen', pk=obj.pk)
        producto = ProductoForm()
        return render(request, 'add_producto.html', {'producto': producto})


class EDO(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        ite = Iteraciones.objects.all()
        return render(request, 'EDO.html', {'ite': ite})


class EcuacionDiferencial():
    def __init__(self, xf, h):
        self.xn = []
        self.yn = []
        # TODO: dominio del calculo de xn[0] hasta xf
        self.xf = xf
        # TODO: paso
        self.h = h

    def f(self, x, y):
        return x - y

    def metodoEuler(self, ci, cf):
        self.xn.append(ci)
        self.yn.append(cf)
        array = []
        n = 0
        while self.xn[n] < self.xf:
            x = self.xn[n] + self.h
            self.xn.append(x)
            y = self.yn[n] + self.h * self.f(self.xn[n], self.yn[n])
            self.yn.append(y)
            n += 1
        array.append(self.xn)
        array.append(self.yn)
        return array

    def RK2(self, ci, cf):
        self.xn.append(ci)
        self.yn.append(cf)
        array = []

        n = 0
        while self.xn[n] < self.xf:
            k1 = self.h * self.f(self.xn[n], self.yn[n])
            k2 = self.h * self.f(self.xn[n] + self.h, self.yn[n] + k1)
            y = self.yn[n] + 0.5 * (k1 + k2)
            self.yn.append(y)
            x = self.xn[n] + self.h
            self.xn.append(x)
            n += 1
        array.append(self.xn)
        array.append(self.yn)
        return array

    def RK4(self, ci, cf):
        self.xn.append(ci)
        self.yn.append(cf)
        array = []

        n = 0
        while self.xn[n] < self.xf:
            k1 = self.h * self.f(self.xn[n], self.yn[n])
            k2 = self.h * self.f(self.xn[n] + 1 / 2 * self.h, self.yn[n] + 1 / 2 * k1)
            k3 = self.h * self.f(self.xn[n] + 1 / 2 * self.h, self.yn[n] + 1 / 2 * k2)
            k4 = self.h * self.f(self.xn[n] + self.h, self.yn[n] + k3)
            y = self.yn[n] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            self.yn.append(y)
            x = self.xn[n] + self.h
            self.xn.append(x)
            n += 1
        array.append(self.xn)
        array.append(self.yn)
        return array


def calcular(request):
    ed = EcuacionDiferencial(4, 0.1)
    array = ed.RK4(0, 0.5)
    array_x = array[0]
    array_y = array[1]
    ite = Iteraciones.objects.all()
    if ite:
        obj = Iteraciones.objects.all()
        obj.delete()
        for i in range(0, len(array[0]) - 1):
            Iteraciones.objects.create(n=i, xn=array_x[i], yn=array_y[i])
    else:
        for i in range(0, len(array[0]) - 1):
            Iteraciones.objects.create(n=i, xn=array_x[i], yn=array_y[i])
    ite = Iteraciones.objects.all()
    return render(request, 'EDO.html', {'ite': ite})


def upload_images(request, pk):
    if request.method == 'POST':
        form = ImagenForm(data=request.POST, files=request.FILES, extra=pk)
        if form.is_valid():
            form.save()
    form = ImagenForm(extra=pk)
    array = Imagen.objects.filter(producto__id=pk)
    return render(request, 'add_imagen.html', {'form': form, 'array': array})
