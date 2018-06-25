from django.shortcuts import render
import datetime
from .forms import UrlForm
from .PythonFiles.bbc import get_rss_feed2
from .PythonFiles.basic import get_rss_feed1
from .PythonFiles.rss import MakeXml
from .PythonFiles.reddit import MakeXml2
import webbrowser

def enter(request):
    form=UrlForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        RssFeed=get_rss_feed1(instance.url)
        if RssFeed=="0":
            RssFeed=get_rss_feed2(instance.url)
        if RssFeed=="0":
            RssFeed=instance.url+".rss"
            MakeXml2(RssFeed)
        else:
            MakeXml(RssFeed)
        instance.save()
        webbrowser.open(RssFeed)
    context={"today" : datetime.datetime.now().date(),"form":form}
    return render(request, "EnterUrl.html", context)
