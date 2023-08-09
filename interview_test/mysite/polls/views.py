from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Interview
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

# Create your views here.
@csrf_protect
def index(request):
    if request.method == "POST":
        new = Interview(
            text=request.POST['inputText'],
        )
        new.save()
        return HttpResponseRedirect(reverse('index'))
    data = Interview.objects.all()
    context = {
        'data':data
    }
    return render(request, 'polls/registration_view.html', context)

@csrf_protect
def edit(request,id):
    if request.method == "POST":
        new = Interview.objects.filter(pk=id)
        new[0].text = request.POST['inputText']
        new[0].save()
        return HttpResponseRedirect(reverse('index'))