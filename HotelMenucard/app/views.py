from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,"index.html")


def display(request):
    selected=request.POST.getlist("checks[]")
    for i in range(0,len(selected)):
        selected[i]=int(selected[i])
    s=0
    for i in selected:
        s+=i
    tax=0.18*s
    Total=s+tax
    dict={"message":{"sum":s,"tax":tax,"total":Total}}
    return render(request,"index.html",dict)