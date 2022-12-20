from django import forms
from .models import Collection, Item

class CollectionForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'border', 'placeholder': 'Collection Name'}
	), max_length=150, required=True)

	description = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'border', 'placeholder': 'Description'}
	), max_length=150, required=True)
	image = forms.ImageField(widget=forms.FileInput(
		attrs={'class': 'border', 'accept':"image/*"}
	), required=True)
	
	class Meta:
		model = Collection
		fields = ('name', 'description', 'image',)

class ItemForm(forms.ModelForm):
	
	class Meta:
		model = Item
		fields = ('collection', 'image')