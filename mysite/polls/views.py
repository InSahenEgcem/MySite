from django.http import HttpResponse


def foo(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bar(request):
    return HttpResponse("This is The Bar page")