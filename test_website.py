
import unittest
from pathlib import Path
from xmlrunner import XMLTestRunner


class WebsiteTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.html_file = Path("index.html")
        cls.content = (
            cls.html_file.read_text(encoding="utf-8")
            if cls.html_file.exists()
            else ""
        )

    def test_file_exists(self):
        self.assertTrue(self.html_file.exists(), "index.html not found")

    def test_doctype(self):
        self.assertIn("<!DOCTYPE html>", self.content)

    def test_page_title(self):
        self.assertIn("<title>Jenkins Docker CI</title>", self.content)

    def test_heading(self):
        self.assertIn(
            "Hello from Jenkins CI/CD - Version 999!",
            self.content
        )

    def test_paragraph(self):
        self.assertIn(
            "Docker image built automatically by Jenkins.",
            self.content
        )


if __name__ == "__main__":
    with open("junit-report.xml", "wb") as report:
        runner = XMLTestRunner(output=report)
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(WebsiteTests)
        result = runner.run(suite)

    if not result.wasSuccessful():
        raise SystemExit(1)