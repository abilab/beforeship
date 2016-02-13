from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from sources.models.sources import Sources


class SourceAddView(CreateView):
    model = Sources
    fields = ['source', 'description', 'logo']
    success_url = reverse_lazy("user_home")
    template_name = "source_add.html"

class SourceListView(ListView):
    model = Sources
    template_name = "source_list.html"
