from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ UserProfile form """
    class Meta:
        """ UserProfile form """
        model = UserProfile
        fields = (
            'default_phone_number',
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form with placeholders and
        add extra styles to fields
        """
        super().__init__(*args, **kwargs)

        extra_attributes = {
                'class': 'text-xs p-3 my-3 my-md-4 rounded-0 border-0',
            }

        placeholders = {
            'default_phone_number': 'Phone Number',
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

        self.fields['default_phone_number'].label = 'Your phone number'
