# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "rankings/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Sports League</h1>")
        self.assertNotContains(response, "Not on the page")


class EditpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/update")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("update"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("update"))
        self.assertTemplateUsed(response, "rankings/list_update.html")

    def test_template_content(self):
        response = self.client.get(reverse("update"))
        self.assertContains(response, "<h1>Modify before saving</h1>")
        self.assertNotContains(response, "Not on the page")

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("update"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("upload"))
        self.assertTemplateUsed(response, "rankings/form_upload.html")

    def test_template_content(self):
        response = self.client.get(reverse("upload"))
        self.assertContains(response, "<h1>Proceed to Upload CSV</h1>")
        self.assertNotContains(response, "Not on the page")