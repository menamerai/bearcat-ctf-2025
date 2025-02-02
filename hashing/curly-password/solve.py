import requests
from bs4 import BeautifulSoup
import re
from itertools import permutations
import hashlib

url = 'https://www.bearcatctf.io/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

text = soup.get_text()

words = re.findall(r'\b\w+\b', text)

unique_words = list(set(words))

target_hash = 'eb02e84ccdc45f873c633846efa027b4726a9552a7dad42927ec627e929a500d'

found = False
for perm in permutations(unique_words, 3):
    flag = f"BCCTF{{{perm[0]}_{perm[1]}_{perm[2]}}}"
    current_hash = hashlib.sha256(flag.encode()).hexdigest()
    if current_hash == target_hash:
        print(f"Flag found: {flag}")
        found = True
        break

if not found:
    print("No matching flag found.")