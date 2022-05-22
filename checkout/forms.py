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
        for field in self.fields:

            extra_attributes = {
                'class': 'text-xs p-3 my-3 my-md-4 rounded-0 border-0',
            }

            self.fields[str(field)].widget.attrs.update(extra_attributes)

        self.fields[str('collection_day')].widget.attrs['autofocus'] = True

        self.fields['full_name'].label = 'Full Name *'
        self.fields['full_name'].widget.attrs.update(
            placeholder='Full Name *'
            )
        self.fields['email'].label = 'Email *'
        self.fields['email'].widget.attrs.update(
            placeholder='Email *'
            )
        self.fields['phone_number'].label = 'Phone Number *'
        self.fields['phone_number'].widget.attrs.update(
            placeholder='Phone Number *'
            )
