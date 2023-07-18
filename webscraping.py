
# Importing libraries

import requests
import  bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import matplotlib.pyplot as plt

# Scraping the data

def main():
    url= "https://news.ycombinator.com/item?id=36152014"
    response=requests.get(url)
    print(response)

    soup=BeautifulSoup(response.text,"html.parser")

    # print(soup.prettify())
    elements=soup.find_all(class_="ind",indent="0" )
    comments=[e.find_next(class_="comment")for e in elements]
    keywords={"python":0,"javascript":0,"typescript":0,"java":0,"c++":0}
    for comment in comments:
        comment_text=comment.get_text().lower()
        words=comment_text.split(" ")
        words=[w.strip(".,/:;!@")for w in words]
        print(words)

        for k in keywords:
            if k in words:
                keywords[k]+=1
    print(keywords)

    plt.bar(keywords.keys(),keywords.values())
    plt.xlabel("Language")
    plt.ylabel("No. of mentions")
    plt.show()


    


if __name__=="__main__":

    main()






