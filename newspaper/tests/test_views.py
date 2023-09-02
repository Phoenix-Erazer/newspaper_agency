from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from newspaper.models import Topic, Newspaper

TOPIC_URL = reverse("newspaper:topic-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
REDACTOR_URL = reverse("newspaper:redactor-list")


class PublicTopicTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password12345")
        self.client.force_login(self.user)

    def test_retrieve_topic(self) -> None:
        Topic.objects.create(name="test1")
        Topic.objects.create(name="test2")

        response = self.client.get(TOPIC_URL)
        topic = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topic))
        self.assertTemplateUsed(response, "newspaper/topic_list.html")


class PublicNewspaperTests(TestCase):
    def test_login_required(self):
        res = self.client.get(NEWSPAPER_URL)

        self.assertNotEqual(res.status_code, 200)


class NewspaperUpdateRedactorViewTests(TestCase):
    def setUp(self):
        self.redactor_user = get_user_model().objects.create_user(
            username="redactor", password="password"
        )
        self.client.login(username="redactor", password="password")
        self.topic = Topic.objects.create(name="Test")
        self.newspaper = Newspaper.objects.create(
            title="Test",
            context="Test context",
            published_date="2023-09-02",
            topic=self.topic,
        )

    def update_redactor(self):
        response = self.client.post(
            reverse(
                "newspaper:newspaper-update-redactor", kwargs={"pk": self.newspaper.pk}
            )
        )
        return response

    def test_add_publisher(self):
        response = self.update_redactor()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("newspaper:newspaper-detail", kwargs={"pk": self.newspaper.pk}),
        )
        self.assertTrue(self.redactor_user in self.newspaper.publishers.all())

    def test_remove_publisher(self):
        self.newspaper.publishers.add(self.redactor_user)

        response = self.update_redactor()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("newspaper:newspaper-detail", kwargs={"pk": self.newspaper.pk}),
        )
        self.assertTrue(self.redactor_user not in self.newspaper.publishers.all())

    def test_access_without_authentication(self):
        self.client.logout()

        response = self.update_redactor()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("login")
            + "?next="
            + reverse(
                "newspaper:newspaper-update-redactor", kwargs={"pk": self.newspaper.pk}
            ),
        )


class PublicRedactorsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)

        self.assertNotEqual(res.status_code, 200)
