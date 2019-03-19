from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from bolao_info.forms import SelectGP2UpdateForm, UpdateGpResultsForm


@staff_member_required
def select_gp_2_update(request):
    if request.method == 'POST':
        
        form = SelectGP2UpdateForm(request.POST)
        
        if form.is_valid():
            gp = form.cleaned_data.get('country')
            
            form_u = UpdateGpResultsForm(initial={
                'country': gp,
                'pole': gp.pole,
                'p1': gp.p1,
                'p2': gp.p2,
                'p3': gp.p3,
                'p4': gp.p4,
                'p5': gp.p5,
                'p6': gp.p6,
                'p7': gp.p7,
                'p8': gp.p8,
                'p9': gp.p9,
                'p10': gp.p10,
                'DoD': gp.DoD,
                'BestLap': gp.BestLap
            })
            
            context_u = {'form': form_u}
            
            return render(request, 'bolao_info/update_gp.html', context_u)
    
    else:
        form = SelectGP2UpdateForm()
    
    context = {'form': form}
    
    return render(request, 'bolao_info/select_gp.html', context)


@staff_member_required
def update_gp(request):
    if request.method == 'POST':
        
        form = UpdateGpResultsForm(request.POST)
        
        if form.is_valid():
            # import pdb;
            # pdb.set_trace()
            
            gp = form.cleaned_data.get('country')
            gp.pole = form.cleaned_data.get('pole')
            gp.p1 = form.cleaned_data.get('p1')
            gp.p2 = form.cleaned_data.get('p2')
            gp.p3 = form.cleaned_data.get('p3')
            gp.p4 = form.cleaned_data.get('p4')
            gp.p5 = form.cleaned_data.get('p5')
            gp.p6 = form.cleaned_data.get('p6')
            gp.p7 = form.cleaned_data.get('p7')
            gp.p8 = form.cleaned_data.get('p8')
            gp.p9 = form.cleaned_data.get('p9')
            gp.p10 = form.cleaned_data.get('p10')
            gp.DoD = form.cleaned_data.get('DoD')
            gp.BestLap = form.cleaned_data.get('BestLap')
            gp.save()

            messages.warning(request, gp.__str__() + ' atualizado com sucesso!')

        return HttpResponseRedirect(reverse('bolao_main:index'))

    messages.warning(request, 'GPrix não atualizado!')
    return HttpResponseRedirect(reverse('bolao_main:index'))
