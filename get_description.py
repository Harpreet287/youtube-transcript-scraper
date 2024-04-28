import requests
from bs4 import BeautifulSoup
import re
video_url = 'https://www.youtube.com/watch?v=HaUzUwNBFcc'
response = requests.get(video_url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


video_id_match = re.search(r'v=([^&]+)', video_url)
if video_id_match:
    video_id = video_id_match.group(1)


published_date_element = soup.find('meta', itemprop='datePublished')

if published_date_element:
    published_date = published_date_element['content']
else:
    published_date = "Date not found"

print(f"Video ID: {video_id}")
print(f"Video Published At: {published_date}")
