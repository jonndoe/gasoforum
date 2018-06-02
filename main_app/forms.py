from django import forms

from .models import GasTheme,\
    GasThemeText,\
    GasThemeComment,\
    GasTopic,\
    GasTopicText,\
    GasTopicComment,\
    Photo, \
    PhotoAlbum, \
    GasThemeCommentReply

class GasThemeForm(forms.ModelForm):
    class Meta:
        model = GasTheme
        fields = ['text','order', 'photo']
        #labels = {'text':''}


class GasTopicForm(forms.ModelForm):
    class Meta:
        model = GasTopic
        fields = ['text', 'avatar']
        #labels = {'text':''}


class GasThemeTextForm(forms.ModelForm):
    class Meta:
        
        model = GasThemeText
        fields = ['order', 'title','subtitle','text','photo','photo_text','photo2','photo2_text','photo3','photo3_text']
        #fields = ['order', 'title','subtitle','text','photo','photo2','photo3']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # overrrides the default django text widget width


class GasTopicTextForm(forms.ModelForm):
    class Meta:
        model = GasTopicText
        fields = ['order', 'title', 'subtitle', 'text', 'photo', 'photo_text', 'photo2', 'photo2_text', 'photo3',
                  'photo3_text']
        # fields = ['order', 'title','subtitle','text','photo','photo2','photo3']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # overrrides the default django text widget width


class PhotoAlbumForm(forms.ModelForm):
    class Meta:
        model = PhotoAlbum
        fields = ['avatar', 'text']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['picture', 'text']


class GasThemeCommentForm(forms.ModelForm):
    class Meta:
        model = GasThemeComment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # overrrides the default django text widget width


class GasThemeCommentReplyForm(forms.ModelForm):
    class Meta:
        model = GasThemeCommentReply
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # overrrides the default django text widget width


class GasTopicCommentForm(forms.ModelForm):
    class Meta:
        model = GasTopicComment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # overrrides the default django text widget width

