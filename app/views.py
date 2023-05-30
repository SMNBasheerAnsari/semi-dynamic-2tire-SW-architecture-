from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name1':'BASHEER ANSARI','age1':23,'name2':'imran','age2':21,'name3':'irfan','age3':19}
    return render(request,"wish.html",context=d)