import pandas as pd                    # Used for data manipulation and analysis.
import numpy as np                     # Used for scientific computing and handling numerical data efficiently.
import matplotlib.pyplot as plt        # A plotting library for creating static, animated, and interactive visualizations in Python.
import seaborn as sns                  # Provides high-level abstractions for complex visualizations
import requests                        # Retrieves the HTML content from the web page
from bs4 import BeautifulSoup          # Parses and extracts specific data from that HTML content.
import openpyxl                        # library used for reading, writing, and manipulating Excel files in the .xlsx and .xlsm formats.



# Creating a dictionary using the given example dataset and add more random data into it.

dictionary = {
    "Customer_ID": [
        "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C004", "C005",
        "C009", "C010", "C001", "C003", "C001", "C006", "C007", "C007", "C001", "C002"
    ],
    "Product_Category": [
        "Electronics", "Clothing", "Home Appliances", "Books", "Groceries", "Electronics",
        "Clothing", "Furniture", "Electronics", "Sports", "Books", "Home Appliances", "Electronics",
        "Electronics", "Home Appliances", "Electronics", "Electronics", "Travel", "Clothing", "Movies"
    ],
    "Purchase_Amount": [
        250.75, 45.00, 120.00, 15.99, 89.50, 320.10, 60.75, 450.00, 25.00, 75.99,
        100.00, 45.50, 250.00, 199.99, 55.60, 30.25, 40.00, 700.00, 15.00, 25.00
    ],
    "Timestamp": [
        "2024-01-15 14:30:00", "2024-01-15 16:00:00", "2024-01-16 10:15:00", "2024-01-16 12:00:00",
        "2024-01-16 13:45:00", "2024-01-16 14:30:00", "2024-01-16 15:00:00", "2024-01-16 16:30:00",
        "2024-01-16 17:00:00", "2024-01-16 18:30:00", "2024-01-16 19:00:00", "2024-01-16 20:00:00",
        "2024-01-16 21:15:00", "2024-01-16 22:00:00", "2024-01-17 09:00:00", "2024-01-17 10:30:00",
        "2024-01-17 11:15:00", "2024-01-17 12:45:00", "2024-01-17 14:00:00", "2024-01-17 15:30:00"
    ]
}

# Create a DataFrame
df = pd.DataFrame(dictionary)

# Save to CSV
df.to_csv("purchase_data.csv", index=False)
print("")
print("")
print(df)
print("")
print("")



                                                        # Data Loading and Preprocessing

# Load the dataset
data = pd.read_csv("purchase_data.csv")

# Handle missing data
data.fillna({'Purchase_Amount': 0, 'Product_Category': 'Unknown'}, inplace=True)
# '0' will be placed if nothing is purchased, 'unkonwn' will be placed instead of a blank space in product_category.

# Convert 'Timestamp' column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# format numerical columns properly
data['Purchase_Amount'] = pd.to_numeric(data['Purchase_Amount'], errors='coerce')
# If a value cannot be converted to a numeric type, it is replaced with NaN (Not a Number).
# Without errors='coerce' argument, an invalid value would raise an error.  

print(data)
print("")
print("")



                                                        # Exploratory Data Analysis
# Summary statistics
print("Summary statistics:")
print(data.describe())
print("")
print("")


# Total purchases over time
total_purchases = data.groupby(data['Timestamp'].dt.date)['Purchase_Amount'].sum()
# .dt.date: extracts only the date from the Timestamp column, discarding the time.
print("Total purchases over time:")
print(total_purchases)
print("")
print("")


# Most popular product categories
popular_categories = data['Product_Category'].value_counts()
# .value_counts(): counts the occurrences of each unique value in the Customer_ID column.
print("Most popular product categories:")
print(popular_categories)
print("")
print("")


# Average spending per customer
avg_spending = data.groupby('Customer_ID')['Purchase_Amount'].mean()
print("Average spending per customer:")
print(avg_spending)
print("")
print("")


# Most active customer
most_active_customer = data['Customer_ID'].value_counts().idxmax()
# .idxmax(): finds the index of the maximum value in the resulting Series from .value_counts()
print(f"Most Active Customer: {most_active_customer}")
print("")
print("")




                                                        # Data Visualization


# Line Chart: Sales trends over time
plt.figure(figsize=(10, 5))            # plt.figure(figsize=(10, 5)): Sets the figure size to 10 inches wide and 5 inches tall.
total_purchases.plot(kind='line')      # total_purchases.plot(kind='line'): Creates a line chart from the total_purchases Series.
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Purchase Amount")
plt.show()
print("")


# Bar Chart: Most purchased product categories
plt.figure(figsize=(10, 5))
popular_categories.plot(kind='bar')    # popular_categories.plot(kind='bar'): Creates a bar chart from the popular_categories Series.
plt.title("Most Purchased Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Number of Purchases")
plt.show()
print("")


# Pie Chart: Revenue percentage by product category
category_revenue = data.groupby('Product_Category')['Purchase_Amount'].sum()
plt.figure(figsize=(7, 7))
category_revenue.plot(kind='pie', autopct='%1.1f%%')    # autopct='%1.1f%%': Displays percentages on the pie chart with 1 decimal place.
plt.title("Revenue Percentage by Product Category")
plt.show()
print("")


# Scatter Plot: Relationship between purchase amount and time
plt.figure(figsize=(10, 5))
sns.scatterplot(x=data['Timestamp'], y=data['Purchase_Amount'])    # sns.scatterplot(x=data['Timestamp'], y=data['Purchase_Amount']): Creates a scatter plot.
plt.title("Purchase Amount vs Time")
plt.xlabel("Time")
plt.ylabel("Purchase Amount")
plt.show()
print("")




                                                        # Web Scraping

print("")
print("")
print("                    Please wait while the program scrapes the required data from the website.....")
print("                    Being thorough... This might take upto 4 minutes.")
print("")
print("")


# Using request library to make HTTP requests to fetch data from the web.
# Websites like Amazon utilize various methods to prevent bot requests, therefore using headers we can mimic our requests as it came frome a browser.
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
URL = "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292110011&s=featured-rank&ds=v1%3Ap%2Bcgl4L%2BsS6k2CP0uYuJZxai9WsP5wOhIw%2BNE9zZVFM&qid=1734168416&ref=sr_st_featured-rank"
webpage = requests.get(URL, headers=HEADERS)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

# Fetch all the links of products using Anchor tags.
links = soup.find_all("a", attrs={"class":'a-link-normal s-line-clamp-4 s-link-style a-text-normal'})

# Initialize the DataFrame to store the scraped data
df2 = pd.DataFrame(columns=["product_title", "price", "rating", "review_count", "availability"])





                                    # Scraping begins....................

# Since scraping all the search results is time consuming, and the project only required at least 50 items, decided to only scrape 50 items.
while True:
    # Scrape the current page
    links = soup.find_all("a", attrs={"class": 'a-link-normal s-line-clamp-4 s-link-style a-text-normal'})

    # Iterate through all the links and scrape data
    for link in links:
        # Construct the full product URL
        product_url = "https://amazon.com" + link.get('href')

        try:
            # Get the content of the product page
            product_page = requests.get(product_url, headers=HEADERS)
            product_soup = BeautifulSoup(product_page.content, "html.parser")

            # Extract product details
            product_title = product_soup.find("span", attrs={"id": 'productTitle'}).text.strip()

            # Handle cases where price might not be available
            price_tag = product_soup.find("span", attrs={"class": 'a-offscreen'})
            price = price_tag.text.strip().replace('$', '') if price_tag else None
            # if price_tag else None: Handles cases where the price_tag is not found. In such cases, price is set to None instead of causing an error.

            # Handle cases where rating might not be available
            rating_tag = product_soup.find("span", attrs={"class": 'a-icon-alt'})
            rating = rating_tag.text if rating_tag else None
            # if rating_tag else None: Handles cases where the rating_tag is not found. In such cases, rating is set to None.

            # Handle cases where review_count might not be available
            review_count_tag = product_soup.find("span", attrs={"id": "acrCustomerReviewText"})
            review_count = review_count_tag.text.strip() if review_count_tag else None

            # Handle cases where availability might not be available
            availability_tag = product_soup.find("span", attrs={"class": "a-size-medium a-color-success"})
            availability = availability_tag.text.strip() if availability_tag else None

            # Add the data to the DataFrame
            df2.loc[len(df2)] = [product_title, price, rating, review_count, availability]

            # Stop if the program reached 50 products
            if len(df2) >= 50:
                break

        except Exception as e:
            print(f"Error scraping {product_url}: {e}")
            # Logs the URL of the product where the error occurred and the specific error message (e) for debugging purposes.

    if len(df2) >= 50:
        break

    # Amazon website uses a "Next" button for pagination.
    # Therefore, scrape items until the next button is found and, then use that link to get to the next page.
    # Find the "Next" button
    next_button = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator'})
    if next_button and 'href' in next_button.attrs:
        URL = "https://www.amazon.com" + next_button['href']
        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
    else:
        break  # Exit the loop when no "Next" button is found

# Save the results to a CSV file
df2.to_csv("amazon_products.csv", index=False)

# Display the scraped data that was integrated into the dataframe.
print(df2)
print("")
print("")




       # Integrate the scraped data into the existing dataset by creating a new dataframe with column names of both original dataframes.

# Combine column names from both DataFrames
combined_columns = list(set(df.columns).union(set(df2.columns)))  # Convert set to list

# Create an empty DataFrame with combined columns
combined_df = pd.DataFrame(columns=combined_columns)

# Add rows from df to the combined DataFrame
for _, row in df.iterrows():
    combined_row = {col: row[col] if col in df.columns else "Unknown" for col in combined_columns}
    # Convert the row to a DataFrame
    combined_row_df = pd.DataFrame([combined_row])
    combined_df = pd.concat([combined_df, combined_row_df], ignore_index=True)

# Add rows from df2 to the combined DataFrame
for _, row in df2.iterrows():
    combined_row = {col: row[col] if col in df2.columns else "Unknown" for col in combined_columns}
    # Convert the row to a DataFrame
    combined_row_df = pd.DataFrame([combined_row])
    combined_df = pd.concat([combined_df, combined_row_df], ignore_index=True)

# Convert 'Timestamp' column in combined_df to datetime
combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'], errors='coerce')

# Convert 'Purchase_Amount' column in combined_df to numeric
combined_df['Purchase_Amount'] = pd.to_numeric(combined_df['Purchase_Amount'], errors='coerce')

# Display the combined DataFrame
print(combined_df)
print("")
print("")



                                                        # Custom Analytics Features


# 1. Search purchases by a specific customer
def search_purchases_by_customer(customer_id):
    return combined_df[combined_df['Customer_ID'] == customer_id]


# 2. Filter purchases by date range or amount
def filter_purchases(start_date=None, end_date=None, min_amount=None):
    filtered_df = combined_df.copy()
    if start_date:
        filtered_df = filtered_df[filtered_df['Timestamp'] >= pd.to_datetime(start_date)]
    if end_date:
        filtered_df = filtered_df[filtered_df['Timestamp'] <= pd.to_datetime(end_date)]
    if min_amount:
        filtered_df = filtered_df[filtered_df['Purchase_Amount'] >= min_amount]
    return filtered_df


# 3. Calculate total revenue by product category
def calculate_revenue_by_category():
    return combined_df.groupby('Product_Category')['Purchase_Amount'].sum()


# 4. Summary report of top-performing products
def summary_report():
    top_products = combined_df.groupby('Product_Category')['Purchase_Amount'].sum().sort_values(ascending=False)
    return top_products


# 5. Export data to Excel (Bonus Challenge)
def export_to_excel(dataframe, filename):
    dataframe.to_excel(filename, index=False)
    print(f"Exported to {filename}")



                                                        # Usage examples

# Search purchases by customer 'C001'
customer_purchases = search_purchases_by_customer('C001')
print("Purchases by C001:")
print(customer_purchases)
print("")
print("")


# Filter purchases from 2024-01-16 with a minimum amount of 100
filtered_data = filter_purchases(start_date='2024-01-16', min_amount=100)
print("Filtered by date:")
print(filtered_data)
print("")
print("")


# Calculate revenue by category
revenue_by_category = calculate_revenue_by_category()
print("Revenue by category:")
print(revenue_by_category)
print("")
print("")


# Generate a summary report
report = summary_report()
print("Summary Report:")
print(report)
print("")
print("")


# Export filtered data to Excel (Bonus Challenge)
export_to_excel(filtered_data, "filtered_data.xlsx")

