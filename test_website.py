
from pathlib import Path

# Website file
html_file = Path("index.html")

# Test 1: Check file exists
assert html_file.exists(), "FAIL: index.html not found"

# Read HTML content
content = html_file.read_text(encoding="utf-8")

# Test 2: Check HTML document declaration
assert "<!DOCTYPE html>" in content, "FAIL: DOCTYPE missing"

# Test 3: Check page title
assert "<title>Jenkins Docker CI</title>" in content, "FAIL: Page title incorrect"

# Test 4: Check heading
assert "Hello from Jenkins CI/CD - Version 3!" in content, "FAIL: Heading missing"

# Test 5: Check paragraph
assert "Docker image built automatically by Jenkins." in content, "FAIL: Paragraph missing"

print("PASS: All 5 website tests passed!")
