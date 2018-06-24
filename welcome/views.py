from django.shortcuts import render
import datetime
from .forms import UrlForm

def enter(request):
    form=UrlForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=True)
    context={"today" : datetime.datetime.now().date(),"form":form}
    return render(request, "EnterUrl.html", context)
