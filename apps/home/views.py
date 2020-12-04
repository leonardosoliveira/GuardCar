from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import UserForm
from .models import Estacionamentos, Cliente
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
    estacionamentos = Cliente.objects.filter(user=request.user)

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
         cliente = Cliente()
         cliente.vagas = 1
         cliente.user_id = request.user.id
         cliente.save()
    return render(request, 'pagamento.html')
        
def cadastro_usuario(request):
    if request.method == 'POST':
        usuarioDja = UserForm(request.POST)
        if usuarioDja.is_valid():
            usuarioDja.save()
            return redirect('../account/login/')
    else:
        usuarioDja = UserForm()
    return render(request, 'cadastro.html', {"usuarioDja":usuarioDja})




    
    
        




