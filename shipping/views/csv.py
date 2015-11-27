from django.views.generic import FormView
from shipping.forms.csv import CSVInputForm


class CSVInputView(FormView):
    template_name = "csv/csv_input.html"
    form_class = CSVInputForm
    success_url = "user/home"
