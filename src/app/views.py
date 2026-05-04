"""Views for the hello world app."""
from django.shortcuts import render


def hello_world(request):
    """
    Render the hello world page.
    
    Args:
        request: The HTTP request object
        
    Returns:
        Rendered template response
    """
    context = {
        'title': 'Django Hello World',
        'message': 'Welcome to Django!',
    }
    return render(request, 'index.html', context)
