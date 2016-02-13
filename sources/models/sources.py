from django.db import models


class Sources(models.Model):
    class Meta():
        verbose_name = "shop source"
        verbose_name_plural = "shop sources"

    source = models.CharField("source for fetching shops",
                              max_length=50,
                              blank=False,
                              unique=True,
                              help_text=("Source from which shops with "
                                         "connected orders can be fetched"))

    description = models.CharField("short description for source",
                                   max_length=255,
                                   blank=True,
                                   help_text=("Short description of source "
                                              "from which shops with "
                                              "connected orders can be "
                                              "fetched"))

    logo = models.ImageField("source logo",
                             max_length=255,
                             blank=True,
                             upload_to="sources/",
                             help_text=("logo image"))

    def __str__(self):
        return "%s" % self.source
