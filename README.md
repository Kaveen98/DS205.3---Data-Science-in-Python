# 🐍 Python Data Analysis and Web Scraping Project

## 📌 Overview

This project demonstrates the integration of **data analytics**, **data visualization**, and **web scraping** using Python. It involves analyzing a simulated dataset of customer purchases and scraping product information from Amazon to enrich insights. Developed as part of coursework for the Data Science module (DS205.3), the project showcases real-world applications of pandas, matplotlib, and BeautifulSoup.

---

## 🧰 Features

### 1. 📊 Data Analysis
- Simulates and loads a CSV dataset (`purchase_data.csv`) of customer purchase activity.
- Handles missing values and ensures consistent formatting.
- Performs exploratory data analysis (EDA) to understand customer behavior and product trends.

### 2. 📈 Data Visualization
- **Line Chart**: Trends in total purchases over time.
- **Bar Chart**: Most popular product categories.
- **Pie Chart**: Revenue breakdown by category.
- **Scatter Plot**: Relationship between amount and time.

### 3. 🌐 Web Scraping (Amazon)
- Extracts product info using `requests` and `BeautifulSoup`:
  - Product title
  - Price
  - Rating
  - Review count
  - Availability
- Limits scrape to 50 products.
- Saves output as `amazon_products.csv`.

### 4. 🔗 Dataset Integration
- Merges scraped product data with original dataset.
- Aligns structure, normalizes fields, and supports joint analysis.

### 5. 🔍 Custom Analytics
- Query purchases by customer ID, category, or date range.
- Calculate total revenue by product.
- Export filtered results to Excel (`.xlsx`).
- Generate summary reports of top-performing products.

---

## 🛠️ Requirements

Make sure the following Python packages are installed:

```bash
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 openpyxl
```

---

## Setup

1. **Ensure Python 3.7+ is Installed**
   Download and install Python from [https://www.python.org/](https://www.python.org/).

2. **Install the Required Libraries**
   Run the following command in your terminal or command prompt:
   ```bash
   pip install pandas numpy matplotlib seaborn requests beautifulsoup4 openpyxl
   ```

3. **Run the Program**
   Execute the program using:
   ```bash
   python <filename>.py
   ```

---

📝 Usage Guide
- Load the purchase data and perform exploratory analysis.
- Visualize customer and product metrics using plots.
- Scrape Amazon product listings to collect item metadata.
- Integrate the scraped data with customer transactions.
- Analyze the enriched dataset for business insights.
- Export filtered or summarized results to Excel for sharing or reporting.

⚠️ Notes
- Scraping may take up to 4 minutes depending on page speed and connection.
- Headers are used to mimic browser behavior (ethical scraping).
- Always follow Amazon's terms of use while scraping.

🎓 Author & Acknowledgment
- Developed by OVDKR Weerasena
- Student ID: 27986
- This program is developed for coursework in Data Science, emphasizing practical applications of Python in data analysis and web scraping.
