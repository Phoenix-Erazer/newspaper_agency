from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic

TOPIC_URL = reverse("newspaper:topic-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
REDACTOR_URL = reverse("newspaper:redactor-list")


class PublicTopicTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self) -> None:
        Topic.objects.create(name="test1")
        Topic.objects.create(name="test2")

        response = self.client.get(TOPIC_URL)
        topic = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topic)
        )
        self.assertTemplateUsed(response, "newspaper/topic_list.html")


class PublicNewspaperTests(TestCase):
    def test_login_required(self):
        res = self.client.get(NEWSPAPER_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicRedactorsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)

        self.assertNotEqual(res.status_code, 200)
