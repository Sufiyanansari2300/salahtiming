from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Masjid
# Create your views here.
def home(request):
    Masjids = Masjid.objects.all()
    n=len(Masjids)
    # no = [i for i in range(1,n+1)]
    l = []
    for i in range(1,n+1):
        d = {}
        d['sno'] = i
        d['name'] = Masjids[i-1].name
        l.append(d)

    return render(request, "salah/home.html",{'list': l})

def contact(request):
    return render(request, "salah/contact.html")

def display(request):
    num = int(request.GET['number'])
    Masjids = Masjid.objects.all()
    m = len(Masjids)
    if num >= 1 and num<=m:
        masjid = Masjids[num-1]
        return render(request, "salah/display.html",{'masjid':masjid})
    else:
        messages.info(request,'Invalid Input')
        return redirect('home')

def search(request):
    return render(request,"salah/search.html")

def searchdisplay(request):
    t = str(request.GET.get("time"))
    Masjids = Masjid.objects.all()
    m = len(Masjids)
    print(t)
    n = len(t)
    tmasjids = []
    if n == 6:
        if (t[4]=='A' or t[4]=='P') and t[5]=='M' and t[1]==':':
            for i in range(0, m):
                if Masjids[i].fazar == t:
                    tmasjids.append(Masjids[i].name)
                elif Masjids[i].zohar == t:
                    tmasjids.append(Masjids[i].name)
                elif Masjids[i].asar == t:
                    tmasjids.append(Masjids[i].name)
                elif Masjids[i].magrib == t:
                    tmasjids.append(Masjids[i].name)
                elif Masjids[i].isha == t:
                    tmasjids.append(Masjids[i].name)
                elif Masjids[i].juma_khutba == t:
                    tmasjids.append(Masjids[i].name)
            if len(tmasjids)==0:
                message = "No Masjids Available"
                return render(request, "salah/searchdisplay.html", {"message": message})
            else:
                return render(request, "salah/searchdisplay.html",{"tmasjids": tmasjids})
        else:
            messages.info(request, 'Invalid Input')
            return redirect('search')
    else:
        messages.info(request, 'Invalid Input')
        return redirect('search')

