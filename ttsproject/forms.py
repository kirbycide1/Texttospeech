from django.forms import ModelForm
from ttsproject.models import Paragraphs

class TextSaveForm(ModelForm):
    
    class Meta:
        model = Paragraphs
        fields = ['text']
    
    #insert Validator that checks if text contains <speak></speak> tags

  


