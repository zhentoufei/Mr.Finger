from django.shortcuts import render

# Create your views here.


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('error404.html',{})
    response.status_code=404
    return response