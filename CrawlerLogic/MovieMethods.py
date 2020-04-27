import MovieData
from RequestMethods import *
#from Queue import queue

def GetMovieNameAndUrl(month, year):
    url = FormUrlFromMonthAndYear(month,year)
    selectors = ["//td[@class='overview-top']/h4/a/text()", "//td[@class='overview-top']/h4/a/@href" ]
    selectorOutput = GetSelectorFromUrlResponse(selectors, url)
    MovieNameList = selectorOutput[0]
    MovieUrlList = selectorOutput[1]
    MovieNameUrlList = []
    for i in range(0,len(MovieNameList)):
        movieNameUrl = {}
        movieNameUrl["Name"] = MovieNameList[i]
        movieNameUrl["Url"] = MovieUrlList[i]
        MovieNameUrlList.append(movieNameUrl)
    return MovieNameUrlList

def GetRatingOfMoviesByMonthAndYear(month, year, movieQueue):
    MovieNameAndUrlList = GetMovieNameAndUrl(month, year)
    movieDataList = []
    for movieNameAndUrl in MovieNameAndUrlList:
        movieData = MovieData.MovieData()
        movieData.MovieName = movieNameAndUrl["Name"]
        movieData.MovieUrl = movieNameAndUrl["Url"]
        BindRatingsAndCertificates(movieData)
        movieDataList.append(movieData)
    return movieDataList

def MovieActorsList(movieLink):
    selector = ["//div[@id='titleCast']//td[@class='primary_photo']/a/img/@title", "//div[@id='titleCast']//td[@class='primary_photo']/a/@href"]
    url = "https://www.imdb.com/" + movieLink
    [ActorNameList, ActorUrlList] = GetSelectorFromUrlResponse(selector, url)
    ActorNameUrlList = []
    for i in range(0, len(ActorNameList)):
        ActorNameUrl = {}
        ActorNameList["Name"] = ActorNameList[i]
        ActorNameList["Url"] = ActorUrlList[i]
        ActorNameUrlList.append(ActorNameUrl)
    return ActorNameUrlList