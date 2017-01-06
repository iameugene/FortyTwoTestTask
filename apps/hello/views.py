from django.shortcuts import render


def contact_detail(request):
    template = 'hello/contact_detail.html'
    return render(request, template, {})
