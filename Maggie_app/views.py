from .models import Contacts, Gallary
from .models import Post
from django.shortcuts import render
from django.utils import timezone


# Create your views here.


def index1(request):
    gallary = Gallary.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    posts = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    user = request.user
    context = {
        'gallary': gallary,
        'posts': posts,
        'user': user,
    }
    return render(request, 'cityblogs/home.html', context)



############################
# for post update

def partners(request):
    return render(request, 'partners.html')


def projects(request):
    user = request.user
    gallary = Gallary.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context = {
        'gallary': gallary,
        'user': user,
    }
    return render(request, 'projects.html', context)


def contactForm(request):
    if request.method == "GET":
        return render(request, 'cityblogs/contactpage.html')
    elif request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']
            contact = Contacts(user_name=name, email=email, mobile_number=mobile, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'cityblogs/contactpage.html', {'success': True})
        except Exception as e:
            print("error in request")
            return render(request, 'cityblogs/contactpage.html', {'success': False})




def mission(request):
    return render(request, 'mission.html')


def about(request):
    return render(request, 'abou.html')
# Create your views here.
