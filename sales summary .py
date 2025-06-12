#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3                
import pandas as pd           
import matplotlib.pyplot as plt 


# In[3]:


conn = sqlite3.connect('sales_data.db')  # Creates or opens 'sales_data.db'
cursor = conn.cursor()     


# In[4]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,    -- Unique ID for each sale
    product TEXT,              -- Product name
    quantity INTEGER,          -- Quantity sold
    price REAL                 -- Price per unit
)
''')


# In[6]:


sample_data = [
    ('Laptop', 5, 700.00),
    ('Smartphone', 10, 300.00),
    ('Tablet', 7, 250.00),
    ('Laptop', 3, 700.00),
    ('Smartphone', 6, 300.00),
    ('Tablet', 4, 250.00)
]


# In[7]:


cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit() 


# In[8]:


query = '''
SELECT product,
       SUM(quantity) AS total_qty,                      -- Total quantity of each product
       SUM(quantity * price) AS revenue                 -- Total revenue per product
FROM sales
GROUP BY product                                        -- Group by product to get separate values for each
'''


# In[9]:


df = pd.read_sql_query(query, conn)


# In[10]:


print("Sales:\n")  # Display title
print(df)  


# In[11]:


plt.figure(figsize=(8,5))                               
df.plot(kind='bar', x='product', y='revenue',          
        legend=False, color='skyblue')                  
plt.title('Total Revenue by Product')                   
plt.xlabel('Product')                                    
plt.ylabel('Revenue')                                 
plt.grid(axis='y', linestyle='--', alpha=0.7)            
plt.tight_layout()                                      
plt.savefig("sales_chart.png")                           
plt.show()    


# In[12]:


conn.close()


# In[ ]:




