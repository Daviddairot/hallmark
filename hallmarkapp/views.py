from django.contrib import admin
from django.urls import path
from django.db.models import Q
from .models import Item
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail


# Create your views here.
def index(request):
    query = request.GET.get('q')
    items = Item.objects.all()

    if query:
        items = items.filter(Q(product_name__icontains=query))

    return render(request,  'index.html', {'items': items})

def cart(request, item_id):
    items = get_object_or_404(Item, id=item_id)
    return render(request, 'cart.html', {'items' : items})

def term1(request, term1):
    items = Item.objects.filter(term=term1)
    context = {
        'term1': term1,
        'items': items,
    }
    return render(request, 'term1.html', context)

def term2(request, term2):
    items = Item.objects.filter(term=term2)
    context = {
        'term2': term2,
        'items': items,
    }
    return render(request, 'term2.html', context)

def term3(request, term3):
    items = Item.objects.filter(term=term3)
    context = {
        'term3': term3,
        'items': items,
    }
    return render(request, 'term3.html', context)

def contact(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = 'Contact Us Form Submission'
        from_email = email  # Use the user's provided email as the sender
        recipient_email = 'dairotemitopedavid@gmail.com'  # Replace with the recipient's email address

        email_message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}'

        try:
            send_mail(subject, email_message, from_email, [recipient_email], fail_silently=False)
            return redirect('success_page')  # Redirect to a success page
            print("success")
        except Exception as e:
             error_message = f'An error occurred: {str(e)}'
             print(error_message)
        items = Item.objects.all()


    return render(request, 'index.html', {'items': items})