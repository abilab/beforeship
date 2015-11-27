from django import forms


class CSVInputForm(forms.Form):
    shop_name = forms.CharField(label="your shop name for this CSV file",
                                error_messages={"required":
                                                "please enter correct name of"
                                                " your shop"})
    csv_file = forms.FileField(label="path to CSV file with shop orders data",
                               error_messages={"required":
                                               "please define correct path to"
                                               "your CSV file"})
