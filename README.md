# Task7
# Task 7: Basic Sales Summary Using Python and SQLite

## Objective

This project showcases a simple Python program that interacts with a SQLite database to summarize product sales data and visualize revenue using a bar chart.

## Tools Used

- Python
- SQLite (`sqlite3`)
- Pandas
- Matplotlib

## Dataset

The script creates a local SQLite database file `sales_data.db` and populates it with a sample `sales` table. The table contains:

- `id` (INTEGER): Unique identifier for each sale
- `product` (TEXT): Name of the product (e.g., Laptop, Smartphone, Tablet)
- `quantity` (INTEGER): Quantity of items sold
- `price` (REAL): Price per unit

Sample data includes multiple sales entries for each product.

## Script Overview

The Python script performs the following steps:

1. Connects to `sales_data.db` (creates it if it doesn't exist)
2. Creates a `sales` table with predefined schema
3. Inserts sample product sales data
4. Executes a SQL query to:
   - Sum total quantity sold per product
   - Calculate total revenue (`quantity * price`) per product
5. Loads query results into a Pandas DataFrame
6. Prints the sales summary to the console
7. Plots a bar chart showing **Total Revenue by Product**
8. Saves the chart as `sales_chart.png`
9. Closes the database connection
