"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page.index is our home page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,

        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



def consultation(request):
    """Renders the Consultation page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/consultation.html',
        {
            'title':'Consultation',
            'message':'Consultation page.',
            'year':datetime.now().year,
        }
    )

def clients(request):
    """Renders the Clients page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/clients.html',
        {
            'title':'Clients',
            'message':'Clients page.',
            'year':datetime.now().year,
        }
    )


def services(request):
    """Renders the Services page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
            'title':'Service',
            'message':'Service page.',
            'year':datetime.now().year,
        }
    )



def marketing(request):
    """Renders the Marketing page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/marketing.html',
        {
            'title':'Marketing',
            'message':'Marketing page.',
            'year':datetime.now().year,
        }
    )

def casestudy(request):
    """Renders the Case Studies page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/casestudy.html',
        {
            'title':'Case Studies',
            'message':'Case Studies page.',
            'year':datetime.now().year,
        }
    )