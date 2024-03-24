from django import forms

class SurveyForm(forms.Form):
    MEMORY_SIZE_CHOICES = [
        ('8GB', '8GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
    ]

    PROCESSOR_CHOICES = [
        ('AMD', 'AMD'),
        ('Intel', 'Intel'),
        ('M-series', 'M-series chip'),
    ]

    BRAND_CHOICES ={
        ('APPLE', 'APPLE'),
        ('DELL', 'DELL'),
        ('LENOVO', 'LENOVO'),
        ('ASUS', 'ASUS'),
        ('HP', 'HP'),
        ('SAMSUNG', 'SAMSUNG'),
        ('INTEL', 'INTEL'),
        ('GOOGLE', 'GOOGLE')
    }

    SCREEN_SIZE = {
        ('11.6', '11.6'),
        ('12.5', '12.5'),
        ('13.3', '13.3'),
        ('14', '14'),
        ('15.6', '15.6'),
        ('17.3', '17.3')
    }

    PRICE = {
        ('300', '300'),
        ('600', '600'),
        ('1200', '1200'),
        ('1800', '1800'),
        ('2400', '2400')

    }

    TOUCHSCREEN = {
        ('YES', 'YES'),
        ('NO', 'NO')
    }




    # Update question1 to use ChoiceField for memory size
    memorySize = forms.ChoiceField(
        label='What memory size would you need?',
        choices=MEMORY_SIZE_CHOICES
    )

    # Update question2 to use ChoiceField for processor type
    processor = forms.ChoiceField(
        label='What processor would you prefer?',
        choices=PROCESSOR_CHOICES
    )

    # Assuming question3 and question4 are similar to the first two,
    # replace them with appropriate ChoiceFields and choices.
    # For example:
    brand = forms.ChoiceField(
        label='Do you have a brand preference?',
        choices=BRAND_CHOICES  # Replace with actual choices
    )
    screen = forms.ChoiceField(
        label='Do you want a particular screen size?',
        choices=SCREEN_SIZE  # Replace with actual choices
    )

    price = forms.ChoiceField(
        label='Which of these numbers is closest to your price range?',
        choices=PRICE  # Replace with actual choices
    )

    touch = forms.ChoiceField(
        label='Is having a touchscreen important to you?',
        choices=TOUCHSCREEN  # Replace with actual choices
    )
