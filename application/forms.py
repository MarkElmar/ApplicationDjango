from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    companyName = forms.CharField(
        max_length=100,
        label="Bedrijf's Naam ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'PixelDeluxe'
            }
        ),
        required=True
    )

    companyLocation = forms.CharField(
        max_length=100,
        label="Bedrijf's Locatie ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Rotterdam'
            }
        ),
        required=True
    )

    websiteLink = forms.URLField(
        label='Website Link ',
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'www.pixeldeluxe.nl/'
            }
        )
    )

    companyContact = forms.CharField(
        max_length=250,
        label="Contact Persoon ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Martijn La Feber'
            }
        )
    )

    # List For ChoiceField
    APPLICATION_WAY = [
        ('TE', 'Telefoon'),
        ('EM', 'E-mail'),
        ('PE', 'Persoonlijk')
    ]

    applicationWay = forms.ChoiceField(
        choices=APPLICATION_WAY,
        label='Sollicitatie Manier ',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    dateApplication = forms.DateField(
        label='Datum Sollicitatie ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    dateReaction = forms.DateField(
        required=False,
        label='Datum Reactie ',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': '09-30-2020'
            }
        )
    )

    dateFaceToFace = forms.DateField(
        label='Datum Sollicitatiegesprek ',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    accepted = forms.BooleanField(
        required=False,
        label='Aangenomen '
    )

    rejected = forms.BooleanField(
        required=False,
        label='Afgewezen '
    )

    reasonRejected = forms.CharField(
        required=False,
        label='Reden Afgewezen ',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5
            }
        )
    )

    class Meta:
        model = Application
        fields = [
            'companyName',
            'companyLocation',
            'companyContact',
            'websiteLink',
            'applicationWay',
            'dateApplication',
            'dateReaction',
            'dateFaceToFace',
            'accepted',
            'rejected',
            'reasonRejected'
        ]

    def clean_dateReaction(self, *args, **kwargs):
        reactionDate = self.cleaned_data.get('dateReaction')
        date = self.cleaned_data.get('dateApplication')
        if reactionDate is not None:
            if date > reactionDate:
                raise forms.ValidationError("Reaction date is earlier than actual date")
        return reactionDate
