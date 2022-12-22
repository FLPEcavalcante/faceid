from django.contrib.messages import constants
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages, auth
from .models import Users as User


def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def register(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})


def validate_register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR,
                             'Email ou password não podem ficar vazior')
        return redirect('/auth/register/')

    if len(password) < 8:
        messages.add_message(request, constants.ERROR,
                             'Sua password deve ter no mínimo 8 caracteres')
        return redirect('/auth/register/')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR,
                             'Já existe um usuário com esse email')
        return redirect('/auth/register/')

    if User.objects.filter(username=name).exists():
        messages.add_message(request, constants.ERROR,
                             'Já existe um usuário com esse name')
        return redirect('/auth/register/')

    try:

        user = User.objects.create_user(
            username=name, email=email, password=password, rua=rua, numero=numero, cep=cep)
        user.save()

        messages.add_message(request, constants.SUCCESS,
                             'register realizado com sucesso')
        return redirect('/auth/register/')

    except:
        messages.add_message(request, constants.ERROR,
                             'Erro interno do sistema')
        return redirect('/auth/register/')

# teste123456


def validate_login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

    user = auth.authenticate(username=name, password=password)
    print(user)
    if not user:
        messages.add_message(request, constants.WARNING,
                             'Email ou password inválido')
        return redirect('/auth/login/')
    else:
        auth.login(request, user)
        return redirect('/plataforma/home')


def out(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING,
                         'Faça login antes de acessar a plataforma')
    return redirect('/auth/login/')
