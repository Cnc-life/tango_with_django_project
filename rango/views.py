from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    #context_dict = {'message': 'This tutorial has been put together by <Xiaoming Zhang>'}
    return render(request, 'rango/about.html')# "<a href='/rango/'>Index</a>")
