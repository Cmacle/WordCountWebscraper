import requests
import operator
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter


def is_visible(element):
    #filter = ['meta']
    filter = ['style', 'script', 'head', 'title', 'meta', '[document']
    if element.parent.name in filter:
        return False
    if isinstance(element, Comment):
        return False
    return True

def split_sentences(wordlist):
    output = []
    for word in wordlist:
        output += word.split(' ')
    return output

def filter_text(wordlist):
    filtered = []
    symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
    wordlist = split_sentences(wordlist)
    for word in wordlist:
        word = word.replace('\n', '')
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            filtered.append(word)
    return filtered

def scrape_words(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    text = soup.findAll(text=True)
    visible_text = filter(is_visible, text)
    return filter_text(visible_text)

def num_words(url):
    wordList = scrape_words(url)
    return len(wordList)

url = input('Enter the url of the website:')
print(scrape_words(url))
print(f'Word Count: {num_words(url)}')