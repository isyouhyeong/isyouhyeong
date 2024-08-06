# from PIL import Image
# import requests
# from io import BytesIO

# # URLs of the images to be combined
# image_urls = [
#     "https://raw.githubusercontent.com/github/explore/main/topics/java/java.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/html/html.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/css/css.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/javascript/javascript.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/thymeleaf/thymeleaf.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/spring-boot/spring-boot.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png",
#     "https://avatars.githubusercontent.com/u/24497451?s=200&v=4",
#     "https://raw.githubusercontent.com/github/explore/main/topics/mysql-workbench/mysql-workbench.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/git/git.png",
#     "https://raw.githubusercontent.com/github/explore/main/topics/github/github.png"
# ]

# # Load images from URLs
# images = [Image.open(BytesIO(requests.get(url).content)) for url in image_urls]

# # Resize images to the same height
# height = 150
# resized_images = [img.resize((int(img.width * height / img.height), height), Image.ANTIALIAS) for img in images]

# # Determine the total width of the final image
# total_width = sum(img.width for img in resized_images)

# # Create a blank image with the total width and desired height
# combined_image = Image.new('RGB', (total_width, height))

# # Paste each image into the combined image
# x_offset = 0
# for img in resized_images:
#     combined_image.paste(img, (x_offset, 0))
#     x_offset += img.width

# # Save the combined image to a file
# combined_image_path = "combined_image.png"
# combined_image.save(combined_image_path)

# combined_image_path



from PIL import Image, ImageDraw
import requests
from io import BytesIO

# URLs of the images to be combined
image_urls = {
    "JavaScript": "https://raw.githubusercontent.com/github/explore/main/topics/javascript/javascript.png",
    "Thymeleaf": "https://www.thymeleaf.org/images/thymeleaf.png",
    "Spring Boot": "https://raw.githubusercontent.com/github/explore/main/topics/spring-boot/spring-boot.png",
    "MySQL": "https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png",
    "DBeaver": "https://dbeaver.io/wp-content/uploads/2019/03/dbeaver-head.png",
    "MySQL Workbench": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/MySQLWorkBenchLogo.png/320px-MySQLWorkBenchLogo.png",
    "Git": "https://raw.githubusercontent.com/github/explore/main/topics/git/git.png",
    "GitHub": "https://raw.githubusercontent.com/github/explore/main/topics/github/github.png"
}

# Load images from URLs
images = {}
for name, url in image_urls.items():
    response = requests.get(url)
    try:
        img = Image.open(BytesIO(response.content)).resize((150, 150), Image.LANCZOS)
        images[name] = img
        print(f"Loaded image from {url}")
    except Exception as e:
        print(f"Failed to load image from {url}: {e}")

# Define layout similar to provided example
layout = [
    ["JavaScript", "Thymeleaf", "Spring Boot", "MySQL"],
    ["DBeaver", "MySQL Workbench", "Git", "GitHub"]
]

# Calculate dimensions
padding = 20
rows = len(layout)
cols = max(len(row) for row in layout)
width = cols * 150 + (cols + 1) * padding
height = rows * 150 + (rows + 1) * padding

# Create blank image with white background
combined_image = Image.new('RGB', (width, height), 'white')

# Draw images onto the blank image
x_offset = padding
y_offset = padding

for row in layout:
    for tech in row:
        if tech in images:
            img = images[tech]
            combined_image.paste(img, (x_offset, y_offset))
        x_offset += 150 + padding
    x_offset = padding
    y_offset += 150 + padding

# Save the combined image to a file
combined_image_path = "combined_technology_stack_layout_v2.png"
combined_image.save(combined_image_path)

print(f"Combined image saved at {combined_image_path}")
