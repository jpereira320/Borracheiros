from django.shortcuts import render, get_object_or_404
from bolao_bet.models import UserBet
from django.views.generic.edit import CreateView
from bolao_bet.forms import ProcessBetForm, ViewResultsForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from bolao_main.models import Blog
from bolao_main.views import next_gp, last_gp_results
from bolao_bet.process_bet_core import process_bet_core
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class BetCreate(CreateView):
    model = UserBet
    template_name = 'bolao_bet/userbet_form.html'
    fields = ['GPrix', 'pole', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BetCreate, self).form_valid(form)
    
    def get_initial(self):
        return {'GPrix': next_gp()}


@login_required
def make_post(request, bet_id):
    bet = get_object_or_404(UserBet, pk=bet_id)
    
    try:
        bet_user = ''
        
        try:
            bet_user = bet.user.get_short_name()
        
        except IOError:
            bet_user = ''
        
        if bet_user == '':
            bet_user = bet.user.username
        
        bet_gprix = bet.GPrix.__str__()
        bet_date = bet.date.__str__()
        
        bet_pole = bet.pole.name
        bet_p1 = bet.p1.name
        bet_p2 = bet.p2.name
        bet_p3 = bet.p3.name
        bet_p4 = bet.p4.name
        bet_p5 = bet.p5.name
        bet_p6 = bet.p6.name
        bet_p7 = bet.p7.name
        bet_p8 = bet.p8.name
        bet_p9 = bet.p9.name
        bet_p10 = bet.p10.name
    
    except (KeyError, UserBet.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bolao_bet:f1bet-add', {
            'error_message': "Invalid bet.",
        })
    else:
        
        post = Blog()
        post.title = 'Aposta de ' + bet_user + ' - ' + bet_gprix
        post.slug = slugify(post.title + bet_date)
        post.body = (bet_gprix + '\n\n' + 'Pole: ' + bet_pole + '\n' +
                     'P1: ' + bet_p1 + '\n' +
                     'P2: ' + bet_p2 + '\n' +
                     'P3: ' + bet_p3 + '\n' +
                     'P4: ' + bet_p4 + '\n' +
                     'P5: ' + bet_p5 + '\n' +
                     'P6: ' + bet_p6 + '\n' +
                     'P7: ' + bet_p7 + '\n' +
                     'P8: ' + bet_p8 + '\n' +
                     'P9: ' + bet_p9 + '\n' +
                     'P10: ' + bet_p10)
        
        post.save()

        messages.warning(request, 'Aposta para o ' + bet_gprix + ' realizada com sucesso!')
        
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('bolao_main:index'))


@staff_member_required
def process_bet(request):
    if request.method == 'POST':
        
        form = ProcessBetForm(request.POST)
        
        if form.is_valid():
            gp = form.cleaned_data.get('country')
            
            process_bet_core(gp)
            
            messages.warning(request, gp.__str__() + ' apurado com sucesso!')
            
            return HttpResponseRedirect(reverse('bolao_main:index'))
    
    else:
        form = ProcessBetForm()
    
    context = {'form': form,}
    
    return render(request, 'bolao_bet/process_bet.html', context)


@login_required
def view_bet(request):
    if request.method == 'POST':
        
        form = ProcessBetForm(request.POST)
        
        if form.is_valid():
            gp = form.cleaned_data.get('country')
            
            posts = Blog.objects.filter(title__contains=gp.__str__())
            posts = posts.filter(title__contains=request.user.get_short_name())
            context = {'posts': posts}
            
            return render(request, 'bolao_bet/view_bet_post.html', context)
    else:
        form = ProcessBetForm()
    
    context = {'form': form}
    
    return render(request, 'bolao_bet/view_bet.html', context)


@login_required
def view_results(request):
    if request.method == 'POST':
        
        form = ViewResultsForm(request.POST)
        
        if form.is_valid():
            gp = form.cleaned_data.get('country')
            list_user, list_points = last_gp_results(gp)
            
            context = {
                'gp': gp,
                'gp_results_user': list_user,
                'gp_results_points': list_points,
            }
            
            return render(request, 'bolao_bet/view_gp_results_post.html', context)
    else:
        form = ViewResultsForm()
    
    context = {'form': form}
    
    return render(request, 'bolao_bet/view_gp_results.html', context)
