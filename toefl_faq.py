#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs  # Correct the class name here
import pandas as pd


# In[4]:


response = requests.get('https://www.aeccglobal.com.np/english-proficiency-coaching/toefl/faqs')


# In[5]:


response


# In[6]:


soup = bs(response.content, 'html.parser')


# In[16]:


sc = soup.find('section', id='section-id-1616759359108')


# In[37]:


data = []
main_div = sc.find('div', class_='sppb-panel-group')
for div in main_div.find_all('div', class_='sppb-panel-default'):
    title = div.find('span', class_='sppb-panel-title')
    title = title.text.strip() if title is not None else "-"
    des_div = div.find('div', class_='sppb-addon-content')
    description_span = des_div.find('span')
    description_span= description_span.text.strip() if description_span is not None else "-"
    data.append({
        'title': title,
        'description': description_span
    })


# In[38]:


data


# In[ ]:

# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file
# df.to_csv('ielts_faqs.csv', index=False)

# # Print a message to confirm the save
# print("Data has been saved to 'toefl_faqs.csv'")



with open('toefl_faqs.txt', 'w', encoding='utf-8') as file:
    for entry in data:
        # Write the title and description to the text file
        file.write(f'Q: {entry["title"]}\n')
        file.write(f'A: {entry["description"]}\n\n')

# Print a message to confirm the save
print("Data has been saved to 'toefl_faqs.txt'")
