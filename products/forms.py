from django import forms
from .widgets import CustomClearableFileInput
from .models import Wines, Bundle, DishesCategory, WineCategory


class WorksForm(forms.ModelForm):
    """
    Form for creating a new bundle
    """

    class Meta:
        """
        Form model and fields
        """
        model = Bundle
        fields = [
            'name',
            'slug_name',
            'dish',
            'wine',
            'price',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:

            extra_attributes = {
                'class': 'text-xs p-3 my-3 my-md-4',
            }

            slug_classes = {
                'class': 'invisible',
            }

            name_field = {
                'class': 'text-xs p-3 mt-3 mt-md-4',
            }

            self.fields[str(field)].widget.attrs.update(extra_attributes)

        self.fields['name'].label = 'Combination Name'
        self.fields['name'].widget.attrs.update(
            name_field,
            placeholder='Combination Name',
            id='dish-name',
            )
        self.fields['name'].error_messages.update({
            'unique': 'A combination with this name already exists',
        })
        self.fields['dish'].label = 'Dish*'
        self.fields['dish'].widget.attrs.update(required=True)
        self.fields['wine'].label = 'Wine*'
        self.fields['wine'].widget.attrs.update(required=True)
        self.fields['price'].widget.attrs.update(
            placeholder='Price',
            )

        self.fields['slug_name'].label = ''
        self.fields['slug_name'].widget.attrs.update(
            slug_classes,
            readonly=True,
            id='slug-name'
        )
        self.fields['slug_name'].error_messages.update({
            'unique': '',
        })


class DishCategoryForm(forms.ModelForm):
    """
    Form for creating a dish category
    """

    class Meta:
        """
        Form model and fields
        """
        model = DishesCategory
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