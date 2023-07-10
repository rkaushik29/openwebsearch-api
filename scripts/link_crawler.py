from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

def crawl_link(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    f = open("./text.txt", "w")

    # kill all script and style elements
    for script in soup(["script", "style", "a"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if len(chunk) > 100)
    
    for line in chunks:
        if len(line) > 100:
            f.write(line)
    
    f.close()
    
    return text

if __name__=="__main__":
    text = crawl_link(sys.argv[1])
    print(text)
