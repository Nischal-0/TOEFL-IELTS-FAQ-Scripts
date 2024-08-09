import requests
from bs4 import BeautifulSoup as bs  # Correct the class name here
import pandas as pd



response = requests.get('https://www.aeccglobal.com.np/english-proficiency-coaching/ielts/faqs')


response


soup = bs(response.content, 'html.parser')


sc = soup.find('section', id='section-id-1616759359108')


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


data


with open('ielts_faqs.txt', 'w', encoding='utf-8') as file:
    for entry in data:
        # Write the title and description to the text file
        file.write(f'Q: {entry["title"]}\n')
        file.write(f'A: {entry["description"]}\n\n')

# Print a message to confirm the save
print("Data has been saved to 'ielts_faqs.txt'")
