from multiprocessing import context
from django.shortcuts import render
from .models import Reporter, Article
from django.views.generic import View

import pdb
# Create your views here.

#query the Airticle which have reporter as forugn key 
# Article.objects.filter(reporter__pk=1)

# Article.objects.filter(reporter=1)

class Learn(View):
    
    def get(self,request):
        #looking up to only one pk airticle 
        # publish = Article.objects.filter(publisher__pk=1)

        # this is looking up to two id
        # publish = Article.objects.filter(publisher__in=[1,2])

        publish = Article.objects.filter(publisher__in=Reporter.objects.filter(last_name='olisa'))
        #counting how many result found on a lookup
        # aiticle = Reporter.objects.filter(article__pk=3).count()


        #query in opposit directions in djnago 
        aiticle = Reporter.objects.filter(article__pk=3)
        first = Reporter.objects.order_by('last_name')
       
        # pdb.set_trace()

        context = {
            'learn': publish,
             'write': aiticle
        }
        return render(request, 'learn.html',context)

    def post(self,request):
        return render(request, 'learn.html')





