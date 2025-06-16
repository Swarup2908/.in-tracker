import os
import requests

def download_pdf(url, save_dir="reports"):
    filename = url.split("/")[-1]
    filepath = os.path.join(save_dir, filename)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if os.path.exists(filepath):
        print(f"PDF already downloaded: {filename}")
        return filepath

    print(f"Downloading: {filename}")
    response = requests.get(url, stream=True)
    
    # Check if it's a PDF
    content_type = response.headers.get("Content-Type", "")
    if "pdf" not in content_type.lower():
        print(f"⚠️ Skipping: {filename} is not a real PDF (Content-Type: {content_type})")
        return None

    # Extra check to avoid HTML renamed as PDF
    if b"<html" in response.content[:100].lower():
        print(f"⚠️ Skipping: {filename} looks like an HTML file, not a real PDF.")
        return None
