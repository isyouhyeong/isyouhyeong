from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# URLs of the images to be combined
image_urls = {
    "JavaScript": "https://raw.githubusercontent.com/github/explore/main/topics/javascript/javascript.png",
    "Thymeleaf": "https://www.thymeleaf.org/images/thymeleaf.png",
    "Spring Boot": "https://raw.githubusercontent.com/github/explore/main/topics/spring-boot/spring-boot.png",
    "MySQL": "https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png",
    "DBeaver": "https://upload.wikimedia.org/wikipedia/commons/3/37/DBeaver_logo.png",
    "MySQL Workbench": "https://upload.wikimedia.org/wikipedia/commons/3/38/MySQL_Workbench_Logo.png",
    "Git": "https://raw.githubusercontent.com/github/explore/main/topics/git/git.png",
    "GitHub": "https://raw.githubusercontent.com/github/explore/main/topics/github/github.png",
    "Java": "https://raw.githubusercontent.com/github/explore/main/topics/java/java.png",
    "HTML": "https://raw.githubusercontent.com/github/explore/main/topics/html/html.png",
    "CSS": "https://raw.githubusercontent.com/github/explore/main/topics/css/css.png",
    "Notion": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg",
    "Gradle": "https://raw.githubusercontent.com/github/explore/main/topics/gradle/gradle.png"
}

# Load images from URLs
images = {}
for name, url in image_urls.items():
    response = requests.get(url)
    try:
        img = Image.open(BytesIO(response.content)).convert("RGBA").resize((150, 150), Image.LANCZOS)
        images[name] = img
        print(f"Loaded image from {url}")
    except Exception as e:
        print(f"Failed to load image from {url}: {e}")

# Define layout similar to the provided example
layout = [
    ["Java", "HTML", "CSS", "JavaScript"],
    ["Thymeleaf", "Spring Boot", "MySQL"],
    ["DBeaver", "MySQL Workbench", "Git", "GitHub"],
    ["Notion", "Gradle"]
]

# Calculate dimensions
padding = 20
rows = len(layout)
cols = max(len(row) for row in layout)
width = cols * 150 + (cols + 1) * padding
height = rows * 150 + (rows + 1) * padding

# Create blank image with white background
combined_image = Image.new('RGBA', (width, height), (255, 255, 255, 255))

# Draw images onto the blank image
x_offset = padding
y_offset = padding

for row in layout:
    for tech in row:
        if tech in images:
            img = images[tech]
            combined_image.paste(img, (x_offset, y_offset), img)
        x_offset += 150 + padding
    x_offset = padding
    y_offset += 150 + padding

# Save the combined image to a file in the current directory
combined_image_path = "combined_technology_stack_layout_final.png"
combined_image.save(combined_image_path)

print(f"Combined image saved at {combined_image_path}")
