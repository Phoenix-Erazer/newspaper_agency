from django.test import TestCase

from newspaper.forms import (
    RedactorLicenseUpdateForm,
    RedactorCreationForm,
    NewspaperSearchForm,
    TopicSearchForm, RedactorSearchForm
)


class FormTest(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "user_name1",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "test first name",
            "last_name": "test last name",
            "years_of_experience": 10,
        }

        form = RedactorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_topic_search_form(self):
        form_data = {"name": "test"}
        form = TopicSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form_data = {"title": "text"}
        form = NewspaperSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_redactor_search_form(self):
        form_data = {"username": "text"}
        form = RedactorSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
