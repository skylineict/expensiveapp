from ast import Try
from multiprocessing import context
import pdb
from unittest import result
from django.shortcuts import render
from django.views.generic import View
from .models import Resultstudent,Allstudent,Schoolstudent
# Create your views here.
from django.contrib import messages
import pdb
from django.core.exceptions import ObjectDoesNotExist






class Checker(View):
    def get(self,request):
        return render(request, 'result.html')
        
    def post(self,request):
        resulcheck = int(request.POST['checker'])
        try:
            resulbefore = Allstudent.objects.get(pk=resulcheck)
            results = Resultstudent.objects.filter(mystudentname__pk=resulcheck)
        except ObjectDoesNotExist:
            messages.error(request,'ooo!  your exam number is invalid try again')
            return render(request, 'result.html')
        
       
            
        
         # # pdb.set_trace()
        context = {
            'resultnow':results,
           'resulbefore': resulbefore
         }

        messages.success(request,'Exam number validated')
        return render(request, 'index.html',context)
     


        
        
       
        
        # resulbefore = Allstudent.objects.get(pk=8620877)

        # publisher = Resultstudent.objects.filter(school__pk=1)
        # # pdb.set_trace()
        # results = Resultstudent.objects.filter(mystudentname__pk=8620877)
        
        
        
        # # pdb.set_trace()
        # context = {
        #     'resultnow':results,
        #     'resulbefore': resulbefore
        # }

       
        

 



       

        # context = {
        #     'resultnow':results,
        #     'resulbefore': resulbefore
        # }

        # if resulcheck <2:
        #     messages.error(request,'Please filled above exam number')
        #     return render(request, 'result.html')

        # resulbefore = Allstudent.objects.get(pk=resulcheck)
        # results = Resultstudent.objects.filter(mystudentname__pk=resulcheck)
                # if resulcheck < 6:
        #      messages.error(request,'pin most be 8 charaters')
        #      return render(request, 'result.html')

        return render(request, 'result.html')
