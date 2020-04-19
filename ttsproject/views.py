
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect


from ttsproject.forms import TextSaveForm
from ttsproject.models import Paragraphs

def TextEditorView(request):
    paragraph = get_object_or_404(Paragraphs, pk=pk)
    if request.method == 'POST':
        form = TextSaveForm(request.POST, instance=paragraph)
        
        if form.is_valid():
            paragraph = form.save()

            # Change URL and map to urls.py later.
            return redirect('audiodownload.html')

    template = 'texteditor_base.html'
    template_vars = { } #Enter template vars when necessary

return render(request, template, template_vars)
