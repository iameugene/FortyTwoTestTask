from django.shortcuts import render

from apps.hello.models import ContactDetail

def contact_detail(request):
    cd_data = ContactDetail.objects.last()

    template = 'hello/contact_detail.html'
    return render(request, template, {'cd_data': cd_data})
