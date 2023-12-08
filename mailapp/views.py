from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
print(70)
print(10+20)
# Create your views here.
def home(request):
    return render(request, 'home.html')


def send(request):
    x = request.GET["fn"]
    y = request.GET["ln"]
    z = request.GET["em"]
    from_mail = settings.EMAIL_HOST_USER
    to_list = [z]
    subject='Hi'
    msg = "Hi" + x + " " + y + "Thank You For Contacting Us"
    send_mail(subject,msg, from_mail, to_list, fail_silently=False)
    return HttpResponse("check your mail once")
