from MovieMethods import *
from MySqlUtility import *
import threading

class ActorDetails():
    ActorName = ""
    ActorImdbId = ""

class ActorExtractor:
    MovieLinks= []
    ActorDetailsList = []
    AllMoviesListed = False
    def __init__(self):
        self.MovieLinks = GetListOfMovieUrlsToCrawlActors()

    
    def GetActorList(self):
        selector = ["//div[@id='titleCast']//td[@class='primary_photo']/a/img/@title", "//div[@id='titleCast']//td[@class='primary_photo']/a/@href"]
        print (str(self.MovieLinks))
        for link in self.MovieLinks:
            url = "https://www.imdb.com/" + link[0]
            [ActorNameList, ActorUrlList] = GetSelectorFromUrlResponse(selector, url)
            for i in range(0,len(ActorNameList)):
                ActorDetail = ActorDetails()
                ActorDetail.ActorName = ActorNameList[i]
                ActorDetail.ActorImdbId = ActorUrlList[i].split("/")[2]
                self.ActorDetailsList.append(ActorDetail)
        self.AllMoviesListed = True
        print ("All Actors pushed to Queue")

    def InsertIntoActorTable(self):
        while(1):
            if (len(self.ActorDetailsList) > 0):
                ActorDetail = self.ActorDetailsList.pop(0)
                print ("Inserting Actor = " + ActorDetail.ActorName)
                InsertActorIntoDatabase(ActorDetail)
                continue
            if (self.AllMoviesListed):
                break
        print ("Crawling Actors Successful")

    def StartCrawling(self):
        x = threading.Thread(target=self.GetActorList)
        x.start()
        y = threading.Thread(target=self.InsertIntoActorTable)
        y.start()
