from django.shortcuts import render, HttpResponse
from .form import Signupform
from .models import Register


# Create your views here.


def contactus(request):
    if request.method == 'POST':
        form = Signupform(request.POST or None, request.FILES or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            fullname = form.cleaned_data['full_name']
            fullname = form.cleaned_data['uplaod_img']

            form.save()

            return HttpResponse("<h2> my contactus save to my database sucessfully</h2>")

    form = Signupform()
    context = {'form': form}
    return render(request, 'contactus/inex.html', context=context)
