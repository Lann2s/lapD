from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

'''
def index(request):
    return render(request , "deff/index.html")
'''
def calculate_tax(request, amount):
        amount = float(amount)
        total_with_tax = amount + (amount * tax_rate)
        return HttpResponse(f"Total price after tax: {total_with_tax:}")
    
def show_tax_rate(request):
    return HttpResponse(f"The current tax rate is {tax_rate * 100}")