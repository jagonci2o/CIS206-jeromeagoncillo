import re

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

def extractYrMthDt(url):
    pattern = r'(\d{4})/(\d{2})/(\d{2})'
    match = re.search(pattern, url)
    if match:
        year, month, date = match.groups()
        return f"Year: {year} \nMonth: {month} \nDate: {date}"
    return None


print("Here is the url: " + url)
print("\n" + extractYrMthDt(url)) 
