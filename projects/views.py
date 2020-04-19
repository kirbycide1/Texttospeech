from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'texteditor_base.html'


class AboutPageView(TemplateView):
    template_name = 'texteditor_base.html'


