from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def single(request):
    success_message = request.GET.get('success_message', '')
    return render(request, 'singlepage.html', {'success_message': success_message})