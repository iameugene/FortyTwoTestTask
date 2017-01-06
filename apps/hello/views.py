from django.shortcuts import render


def contact_detail(request):
    cd_data = {
        "first_name": "Yauhen",
        "last_name": "Alkhouski",
        "birth_day": "1976-11-20",
        "bio": "some bio information",
        "email": "zzreklama@gmail.com",
        "skype": "i.eugene",
        "jabber": "iameugene@42cc.co",
        "other_contacts": "some other contact",
    }
    template = 'hello/contact_detail.html'
    return render(request, template, {'cd_data': cd_data})
