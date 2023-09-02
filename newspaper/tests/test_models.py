from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper


class ModelsTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test first name",
            last_name="Test last name",
        )
        self.topic = Topic.objects.create(name="test")

    def test_topic_str(self):
        self.assertEqual(str(self.topic), f"{self.topic.name}")

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} "
            f"({self.redactor.first_name} "
            f"{self.redactor.last_name})",
        )

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.create(
            title="test car",
            context="context",
            published_date="2022-05-05",
            topic=self.topic,
        )

        self.assertEqual(str(newspaper), f"{newspaper.title}")

    def test_redactor_get_absolute_url(self):
        self.assertEquals(self.redactor.get_absolute_url(), "/redactors/1/")
