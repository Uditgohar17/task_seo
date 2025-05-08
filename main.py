import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def scrape_trending_products():
    url = "https://www.ebay.com/deals"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    product_elements = soup.select(".ebayui-dne-item-featured-card .dne-itemtile-title")
    products = [product.get_text(strip=True) for product in product_elements[:3]]
    return products

def generate_blog_post(product_name, keywords):
    prompt = f"Write a 150-200 word SEO-friendly blog post about '{product_name}', incorporating the keywords: {', '.join(keywords)} naturally."
    response = model.generate_content(prompt)
    return response.text.strip()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    product = data.get("product")
    keywords = data.get("keywords", [])
    if not product or not keywords:
        return jsonify({"error": "Missing product name or keywords"}), 400
    blog_post = generate_blog_post(product, keywords)
    return jsonify({"blog_post": blog_post})

@app.route("/scrape", methods=["GET"])
def scrape():
    products = scrape_trending_products()
    return jsonify({"products": products})

if __name__ == "__main__":
    app.run(debug=True)
