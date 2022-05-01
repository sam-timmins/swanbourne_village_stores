from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """ Order form """
    class Meta:
        """ Order form """
        model = Order
        fields = (
            'collection_day',
            'full_name',
            'email',
            'phone_number',
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form with placeholders and
        add extra styles to fields
        """
        super().__init__(*args, **kwargs)
        extra_attributes = {
                'class': 'text-xs p-3 my-3 my-md-4',
            }

        placeholders = {
            'collection_day': 'Collection Day',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone number',
        }

        self.fields[str('collection_day')].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs.update({
                'placeholder': placeholder,
            })
            self.fields[str(field)].widget.attrs.update(extra_attributes)
