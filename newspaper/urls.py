from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    TopicCreateView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    RedactorListView,
    RedactorDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "newspaper"
