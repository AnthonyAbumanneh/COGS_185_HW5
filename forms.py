from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "serial_number", "quantity", "expiry_date", "notes"]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # Don't override widgets we already set above (expiry_date, notes)
            if "class" not in field.widget.attrs:
                field.widget.attrs["class"] = "form-control"