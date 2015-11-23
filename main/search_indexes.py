import datetime
from haystack import indexes
from main.models import DVD, MovieCas


class DVD(indexes.SearchIndex, indexes.Indexable):
    # convention to have one field named 'text' where document = true
    text = indexes.CharField(document=True, use_template=True)
    dvd_title = indexes.CharField(model_attr="dvd_title")
    year = indexes.CharField(model_attr="year")

    def get_model(self):
        return DVD

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())