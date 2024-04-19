from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import Test
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
has_ownership = [account_ownership_required, login_required]


@login_required
def hello_peter(request):

    if request.method == "POST":

        temp = request.POST.get('hello_peter_input')

        new_test = Test()
        new_test.text = temp
        new_test.save()

        return HttpResponseRedirect(reverse('accountapp:hello_peter'))
    else:
        test_list = Test.objects.all()
        return render(request, 'accountapp/hello_peter.html', context={'test_list': test_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_peter')    ## reverse_lazy = 클래스형 view 에서 사용 // reverse = 함수형 view 에서 사용
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_peter')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'







