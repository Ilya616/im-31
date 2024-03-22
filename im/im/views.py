from django.shortcuts import render

def list_products(request):
    return render(request, "list_products.html")
    