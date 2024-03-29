from django.shortcuts import render

def list_products(request):
    return render(request, "list_products.html")

def add_category(request):
    return render(request, "add_category.html")

def accept_category(request):  
    print(request)



    