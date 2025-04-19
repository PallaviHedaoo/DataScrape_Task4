import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.flipkart.com/search?q=lapotp&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"

# Send a GET request to the URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all laptop containers
laptops = soup.find_all("div", class_="tUxRFH")

# Extract data for each laptop
for laptop in laptops:
    try:
        # Laptop Image URL
        image_tag = laptop.select_one("img.DByuf4")
        image_url = image_tag["src"] if image_tag else "N/A"

        # Laptop Product Name
        name_tag = laptop.select_one("div.tUxRFH div.yKfJKb div.KzDlHZ")
        product_name = name_tag.text.strip() if name_tag else "N/A"

        # Laptop Product Rating
        rating_tag = laptop.select_one("div.yKfJKb div._5OesEi div.XQDdHH")
        product_rating = rating_tag.text.strip() if rating_tag else "N/A"

        # Laptop Product Review Count
        review_tag = laptop.select_one("div._5OesEi span.Wphh3N")
        review_count = review_tag.text.strip() if review_tag else "N/A"

        # Laptop Product Information
        info_tag = laptop.select_one("div._6NESgJ ul.G4BRas")
        product_info = [li.text.strip() for li in info_tag.find_all("li")] if info_tag else "N/A"

        # Laptop Original Price
        original_price_tag = laptop.select_one("div.BfVC2z div.ZYYwLA")
        original_price = original_price_tag.text.strip() if original_price_tag else "N/A"

        # Laptop Discounted Price
        discounted_price_tag = laptop.select_one("div.BfVC2z div._4b5DiR")
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else "N/A"

        # Laptop Discount
        discount_tag = laptop.select_one("div.cN1yYO div.UkUFwK")
        discount = discount_tag.text.strip() if discount_tag else "N/A"

        # Is Bank Offer
        bank_offer_tag = laptop.select_one("div.M4DNwV div.O5Fpg8")
        is_bank_offer = "Yes" if bank_offer_tag else "No"

        # Print the extracted data
        print(f"Image URL: {image_url}")
        print(f"Product Name: {product_name}")
        print(f"Rating: {product_rating}")
        print(f"Review Count: {review_count}")
        print(f"Product Info: {product_info}")
        print(f"Original Price: {original_price}")
        print(f"Discounted Price: {discounted_price}")
        print(f"Discount: {discount}")
        print(f"Bank Offer: {is_bank_offer}")
        print("-" * 50)

    except Exception as e:
        print(f"Error extracting data for a laptop: {e}")