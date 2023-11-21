from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from django.contrib import messages

from django.http import JsonResponse
from .models import Branch


# def customer_data(request):
#     return render(request, 'customer.html')

@login_required
def application_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted!')
            return redirect('customer:application_form')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
    else:
        form = ApplicationForm()

    return render(request, 'customer.html', {'form': form})


def get_branches(request, district_id):
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)