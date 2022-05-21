from django import forms
from products.widgets import CustomClearableFileInput
from products.models import Dishes, Wines


class DishForm(forms.ModelForm):
    """
    Form for creating a new dish
    """

    class Meta:
        """
        Form model and fields
        """
        model = Dishes
        fields = [
            'category',
            'name',
            'slug_name',
            'status',
            'price',
            'description',
            'image',
        ]

    image = forms.ImageField(
        required=False,
        widget=CustomClearableFileInput,
        )

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

        self.fields['image'].label = ''
        self.fields['description'].label = 'Description'
        self.fields['description'].widget.attrs.update(
            placeholder='Description'
            )
        self.fields['name'].label = 'Dish Name'
        self.fields['name'].widget.attrs.update(
            name_field,
            placeholder='Dish Name',
            id='dish-name',
            )
        self.fields['name'].error_messages.update({
            'unique': 'A dish with this name already exists',
        })
        self.fields['status'].label = 'Fresh or Frozen'
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


class WineForm(forms.ModelForm):
    """
    Form for creating a new wine
    """

    class Meta:
        """
        Form model and fields
        """
        model = Wines
        fields = [
            'category',
            'name',
            'slug_name',
            'price',
            'description',
            'image',
        ]

    image = forms.ImageField(
        required=False,
        widget=CustomClearableFileInput,
        )

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

        self.fields['image'].label = ''
        self.fields['description'].label = 'Description'
        self.fields['description'].widget.attrs.update(
            placeholder='Description'
            )
        self.fields['name'].label = 'Wine Name'
        self.fields['name'].widget.attrs.update(
            name_field,
            placeholder='Wine Name',
            id='dish-name',
            )
        self.fields['name'].error_messages.update({
            'unique': 'A wine with this name already exists',
        })
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