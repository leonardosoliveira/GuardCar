from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import UserForm
from .models import Estacionamentos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class HomeView(View):
    cliente_class = UserForm
    initial = {'key': 'value'}

    def get(self, request):

        dados = {}
        cliente = self.cliente_class(initial=self.initial)
        dados['cliente'] = cliente
        return render(request, 'home.html', dados)
        
    def post(self, request):
        pass

    
def list_todas_reservas(request):
        estacionamentos = Estacionamentos.objects.filter(active=True)
        return render(request, 'list.html', {'estacionamentos': estacionamentos})

@login_required
def list_user_reservas(request):
    estacionamentos = Estacionamentos.objects.filter(active=True, user=request.user)

    return render(request, 'list.html', {'estacionamentos': estacionamentos})

@login_required       
def reserva_detalhes(request, id):
    estacionamentos = Estacionamentos.objects.get(active=True, id=id)
    print(estacionamentos.id)
    return render(request, 'reserva.html', {'estacionamentos': estacionamentos})

@login_required
def reserva_agendamento(request, id):
    estacionamentos = Estacionamentos.objects.get(id=id)
    if(estacionamentos.vagas > 0):
         estacionamentos.vagas -= 1
         estacionamentos.save()
    return render(request, 'pagamento.html')
        
def cadastro_usuario(request):
    print("teste\n\n")
    if(request.method == 'POST'):
        usuarioDja = UserForm(request.POST)
        print("teste2\n\n",usuarioDja)
        user = User()
        user.first_name= request.POST['first_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password1 = request.POST['password1']
        user.password2 = request.POST['password2']
        
        user.save()
        return render(request, 'login.html')
    usuarioDja = UserForm()
    return render(request, 'cadastro.html', {"usuarioDja":usuarioDja})





    
    
        




