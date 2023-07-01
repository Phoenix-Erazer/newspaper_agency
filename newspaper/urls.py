from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from newspaper.views import (
    index,
    TopicListView)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "newspaper"
