import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    url = input("Enter the URL of the image: ").strip()

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✅ Image saved as {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to fetch the image: {e}")

if __name__ == "__main__":
    fetch_image()
