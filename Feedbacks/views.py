from django.shortcuts import render


# Create your views here
def contacts(request):
    return render(request, 'feedback/contacts.html')
