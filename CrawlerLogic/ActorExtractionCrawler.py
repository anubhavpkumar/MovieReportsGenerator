from MovieMethods import *
from MySqlUtility import *
import threading

class ActorDetails():
    ActorName = ""
    ActorImdbId = ""

class ActorExtractor:
    MovieLinks= []
    ActorDetailsList = []
    def __init__(self,movieLinks):
        self.MovieLinks = movieLinks
    
    def GetActorList(self):
        selector = ["//div[@id='titleCast']//td[@class='primary_photo']/a/img/@title", "//div[@id='titleCast']//td[@class='primary_photo']/a/@href"]
        for link in self.MovieLinks:
            url = "https://www.imdb.com/" + link
            [ActorNameList, ActorUrlList] = GetSelectorFromUrlResponse(selector, url)
            for i in range(0,len(ActorNameList)):
                ActorDetail = ActorDetails()
                ActorDetail.ActorName = ActorNameList[i]
                ActorDetail.ActorImdbId = ActorUrlList[i].split("/")[2]
                self.ActorDetailsList.append(ActorDetail)

    def InsertIntoActorTable(self):
        while(1):
            if (len(self.ActorDetailsList) > 0):
                ActorDetail = self.ActorDetailsList.pop(0)
                InsertActorIntoDatabase(ActorDetail)

    def StartCrawling(self):
        x = threading.Thread(target=self.GetActorList)
        x.start()
        y = threading.Thread(target=self.InsertIntoActorTable)
        y.start()
