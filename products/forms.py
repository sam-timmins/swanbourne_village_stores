from django import forms
from .widgets import CustomClearableFileInput
from .models import WineCategory


class WineCategoryForm(forms.ModelForm):
    """
    Form for creating a dish category
    """

    class Meta:
        """
        Form model and fields
        """
        model = WineCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:

            extra_attributes = {
                'class': 'text-xs p-3 my-3 my-md-4',
            }

            self.fields[str(field)].widget.attrs.update(extra_attributes)

        slug_classes = {
                'class': 'invisible',
            }

        self.fields['origin'].label = 'Origin'
        self.fields['origin'].widget.attrs.update(
            placeholder='Origin'
            )
        self.fields['variety'].label = 'Variety'
        self.fields['variety'].widget.attrs.update(
            placeholder='Variety'
            )
        self.fields['name'].label = 'Category'
        self.fields['name'].widget.attrs.update(
            placeholder='Category',
            id='dish-name',
            )
        self.fields['friendly_name'].label = ''
        self.fields['friendly_name'].widget.attrs.update(
            slug_classes,
            readonly=True,
            id='slug-name'
        )
        self.fields['friendly_name'].error_messages.update({
            'unique': '',
        })