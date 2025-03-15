import requests
from bs4 import BeautifulSoup

def searchPaper(term, n=3):
    url = 'https://arxiv.org/search/?query='+''.join([x if x != ' ' else '+' for x in term])\
    +'&searchtype=all&source=header'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    search_res = []

    for i in range(n):
        resdict = {}
        _ = soup.select_one('#main-container > div.content > ol > li:nth-child('+str(i+1)+') > p.title.is-5.mathjax').get_text()

        Title = ''.join([x for x in _ if x != '\n']).strip()
        resdict["Title"] = Title
        # print(Title)

        author_index = 1
        author = []
        while(True):
            _ = soup.select_one('#main-container > div.content > ol > li:nth-child('+str(i+1)+') > p.authors > a:nth-child('+str(author_index+1)+')')
            if(_ == None): break
            else: _ = _.get_text()
            author_index+=1
            author.append(_)
        resdict["Author"] = author
        # print(author)

        Link = soup.select_one('#main-container > div.content > ol > li:nth-child('+str(i+1)+') > div > p > a').attrs['href']
        # print(Link)
        resdict["Link"] = Link
        

        Abstract = requests.get(Link).text.split("""<blockquote class="abstract mathjax">
            <span class="descriptor">Abstract:</span>""")[1].split("</blockquote>")[0].strip()
        resdict["Abstract"] = Abstract
        # Print(Abstract)

        search_res.append(resdict)
    return search_res
