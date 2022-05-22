from django import forms

from checkout.models import Order, CollectionDays, COMPLETED, COLLECTED_ORDER


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

        self.fields['status'].widget = forms.RadioSelect(choices=COMPLETED)
        self.fields['status'].label = ''


class UpdateCollectionStatusForm(forms.ModelForm):
    """ Update status of an order form """
    class Meta:
        """ Update status of an order form """
        model = Order
        fields = (
            'collected_order',
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form with placeholders and
        add extra styles to fields
        """
        super().__init__(*args, **kwargs)

        self.fields['collected_order'].widget = forms.RadioSelect(
            choices=COLLECTED_ORDER
            )
        self.fields['collected_order'].label = ''


class CreateCollectionDayForm(forms.ModelForm):
    """ Form for admin to create a collection day """
    class Meta:
        """ Form for admin to create a collection day """
        model = CollectionDays
        fields = (
            'day',
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

        placeholders = {
            'day': 'Add a day'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs.update({
                'placeholder': placeholder,
            })
            self.fields[str(field)].widget.attrs.update(extra_attributes)
            self.fields[str(field)].label = ''
