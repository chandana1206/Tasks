from bing_image_downloader import downloader
import os

def download_junk_food_images(categories, num_images_per_category, output_dir="junk_food_dataset"):

    os.makedirs(output_dir, exist_ok=True)
    
    for category in categories:
        print(f"Downloading {num_images_per_category} images for category: {category}")
        downloader.download(
            query=category,
            limit=num_images_per_category,
            output_dir=output_dir,
            adult_filter_off=True,
            force_replace=False,
            timeout=60
        )
        print(f"Completed downloading for: {category}")

junk_food_categories = ["Burgers", "Pizzas", "Fries", "Ice Creams", "Chocolate", "Soda", "Hot Dogs"]

download_junk_food_images(junk_food_categories, 50)
