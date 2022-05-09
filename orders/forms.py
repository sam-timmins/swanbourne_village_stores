from django import forms

from checkout.models import Order


class UpdateStatusForm(forms.ModelForm):
    """ Update status of an order form """
    class Meta:
        """ Update status of an order form """
        model = Order
        fields = (
            'status',
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form with placeholders and
        add extra styles to fields
        """
        super().__init__(*args, **kwargs)
        extra_attributes = {
                'class': 'text-xs p-3 rounded-0 border-0',
            }

        self.fields['status'].widget.attrs.update(extra_attributes)
        self.fields['status'].label = ''
