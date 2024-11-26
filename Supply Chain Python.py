#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_excel(r"C:\Users\ff\Desktop\Intern Projects\Supply Chain Management Dashboard\Supply Chain Management.xlsx").set_index("Product type")


# In[3]:


data.head()


# In[4]:


total_revenue = round(data['Revenue generated'].sum(), 2)
print(total_revenue)


# In[5]:


high_selling_product = data.groupby('Product type')['Number of products sold'].sum().sort_values(ascending = False)
print(high_selling_product)


# In[6]:


total_production = data['Production volumes'].sum()
print(total_production)


# In[7]:


high_selling_customer = data.groupby('Customer demographics')['Number of products sold'].sum().sort_values(ascending = False)
print(high_selling_customer)


# In[8]:


avg_defect_rate = round(data.groupby('Product type')['Defect rates'].mean(), 2).sort_values(ascending = False)
print(avg_defect_rate)


# In[10]:


avg_manufacturing_cost = round(data['Manufacturing costs'].mean(), 2)
print(avg_manufacturing_cost)


# In[13]:


avg_lead_time = data['Manufacturing lead time'].mean()
print(avg_lead_time)


# In[17]:


sku_availability = data.groupby('SKU')['Availability'].sum().sort_values(ascending = False)
top_20 = sku_availability.head(20)
print(top_20)


# In[18]:


total_product_sold = data['Number of products sold'].sum()
print(total_product_sold)


# In[20]:


inspect_order = data.groupby('Inspection results')['Order quantities'].sum().sort_values(ascending = False)
print(inspect_order)


# In[21]:


sku_order = data.groupby('SKU')['Order quantities'].sum().sort_values(ascending = False)
top_20 = sku_order.head(20)
print(top_20)


# In[23]:


supply_revenue = round(data.groupby('Supplier name')['Revenue generated'].sum(), 2).sort_values(ascending = False)
print(supply_revenue)


# In[25]:


shipping_carrier_revenue = round(data.groupby('Shipping carriers')['Revenue generated'].sum(), 2).sort_values(ascending = False)
print(shipping_carrier_revenue)


# In[27]:


sku_stock = data.groupby('SKU')['Stock levels'].sum().sort_values(ascending = False)
top_20 = sku_stock.head(20)
print(top_20)


# In[30]:


sku_revenue = round(data.groupby('SKU')['Revenue generated'].sum(), 2).sort_values(ascending = False)
top_20 = sku_revenue.head(20)
print(top_20)


# In[32]:


product_revenue = round(data.groupby('Product type')['Revenue generated'].sum(), 2).sort_values(ascending = False)
print(product_revenue)


# In[34]:


location_revenue = round(data.groupby('Location')['Revenue generated'].sum(), 2).sort_values(ascending = False)
print(location_revenue)


# In[35]:


avg_lead = data['Lead time'].mean()
print(avg_lead)


# In[37]:


avg_shipping_cost = data['Shipping costs'].mean()
print(avg_shipping_cost)


# In[42]:


shipping_carrier_cost = round(data.groupby('Shipping carriers')['Shipping costs'].sum(),2).sort_values(ascending = False)
print(shipping_carrier_cost)


# In[43]:


transportation_defect = round(data.groupby('Transportation modes')['Defect rates'].sum(),2).sort_values(ascending = False)
print(transportation_defect)


# In[44]:


transportation_shipping_cost = round(data.groupby('Transportation modes')['Shipping costs'].sum(),2).sort_values(ascending = False)
print(transportation_shipping_cost)


# In[ ]:




