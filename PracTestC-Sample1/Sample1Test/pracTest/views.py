from django.shortcuts import render, get_object_or_404
from .models import Customer, Purchase

def index(request):
    return render(request, 'instructions.html')

def question1(request):
    customer_id = None
    order_shipped = None
    order_not_shipped = None
    message = ''
    
    if request.method == 'POST':
        
        print("Hello Nam")
        customer_id = request.POST.get('customer_id')
        
        customer = get_object_or_404(Customer, pk = customer_id)
        print('======', customer)
        order_shipped = Purchase.objects.filter(customer = customer).exclude(shipping_date = None)
        order_not_shipped = Purchase.objects.filter(customer = customer, shipping_date = None)
        
        if not order_shipped.exists() and not order_not_shipped.exists():
            message = f"No orders were found for customer {customer_id}."
            
        
    
    return render(request, 'Question1.html')
