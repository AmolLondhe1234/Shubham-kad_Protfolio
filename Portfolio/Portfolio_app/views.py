from django.shortcuts import render,HttpResponse
from .models import Projects,Certificate,Feedback
from django.contrib import messages
# Create your views here.
def home(request):
        fb=Feedback.objects.all()
        cert=Certificate.objects.all()
        prjt=Projects.objects.all()
        context={
        'fb':fb,
        'cert':cert,
        'prjt':prjt,
        }
        return render(request,'base.html',context)
    # elif request.method == 'POST':
    #     fname = request.POST['name']
    #     email= request.POST['email']
    #     phone = request.POST['phone']
    #     mess= request.POST['feedback_text']
    #     Feedback(F_name=fname,F_Email=email,F_mobile=phone,F_text=mess).save()
    #     messages.success(request,'FeedBack Submited Successfully')
    #     return render(request,'base.html')
# def aboutme(request):
#     return render(request,'aboutme.html')


def fb(request):
    if request.method == 'POST':
        fname = request.POST['name']
        email= request.POST['email']
        phone = request.POST['phone']
        mess= request.POST['feedback_text']
        Feedback(F_name=fname,F_Email=email,F_mobile=phone,F_text=mess).save()
        messages.success(request,'FeedBack Submited Successfully')
        fb=Feedback.objects.all()
        cert=Certificate.objects.all()
        prjt=Projects.objects.all()
        context={
        'fb':fb,
        'cert':cert,
        'prjt':prjt,
        }
    return render(request,'base.html',context)
    
    # return render(request,'feedback.html')
# def home(request):

#     return render(request,'home.html')


