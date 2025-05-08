# task_seo
seo
# SEO Blog Post Creation Tool

## 📌 Overview
This tool scrapes trending products from eBay and uses Google's Gemini AI to generate SEO-optimized blog content.

## 🚀 How to Use

### 1. Setup Environment

```bash
conda env create -f environment.yml
conda activate seo-blog-tool
```

### 2. Configure API Key

Create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your-api-key-here
```

### 3. Run the Server

```bash
python main.py
```

## 🔧 API Endpoints

- `GET /scrape` – Scrapes trending product names.
- `POST /generate` – JSON body with `"product"` and `"keywords"` list to get blog content.
