## Python Custom Request mapper
import requests
from lxml import html
def GetSelectorFromUrlResponseSingle(selector, url):
    try:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        return tree.xpath(selector)
    except:
        pass
    return "Error"

def GetSelectorFromUrlResponse(selectorList, url):
    try:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        responseList = []
        for selector in selectorList:
            responseList.append(tree.xpath(selector))
        return responseList
    except Exception as ex:
        print (ex)
    return "Error"

def FormMovieUrl(url):
    return "https://www.imdb.com/" + url

def BindRatingsAndCertificates(movieData):
    url = FormMovieUrl(movieData.MovieUrl)
    selector = "//span[@itemprop='ratingValue']/text()"
    ratingValue = GetSelectorFromUrlResponseSingle(selector, url)
    if (len(ratingValue) != 0 and ratingValue[0] != None):
        movieData.MovieRating = ratingValue[0]


    
def FormUrlFromMonthAndYear(month, year):
    return "https://www.imdb.com/movies-coming-soon/" + year.strip() + "-" + month.strip() + "/"