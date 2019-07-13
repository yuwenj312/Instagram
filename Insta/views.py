from django.views.generic import TemplateView

class HelloDjango(TemplateView): #class-based 
    template_view = 'home.html'

