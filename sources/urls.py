from django.conf.urls import include, url
from sources.views.sources import SourceAddView, SourceListView

urlpatterns = [
    url(r'^add$', SourceAddView.as_view(), name="source_add"),
    url(r'^list', SourceListView.as_view(), name="source_list")
               ]
