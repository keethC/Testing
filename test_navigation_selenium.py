# Simple test: check HTML file content for expected title and links

file_path = r"C:\Users\user\Desktop\Test02\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check title
assert "<title>Home - My Demo Website</title>" in content
print("[PASS] Title is present")

# Check navigation links
assert 'href="index.html"' in content
assert 'href="about.html"' in content
assert 'href="contact.html"' in content
print("[PASS] Navigation links are present")
