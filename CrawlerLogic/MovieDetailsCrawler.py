## Python File to Details from URL
from RequestMethods import *
from MySqlUtility import *
from MovieMethods import *
import threading

class MovieDetailsCrawler:
    MovieQueue = []
    monthsArray = []
    yearsArray = []
    def __init__(self, monthsArray, yearsArray):
        self.monthsArray = monthsArray
        self.yearsArray = yearsArray

    def PushRatingsToQueue(self, month, year):
        MovieNameAndUrlList = GetMovieNameAndUrl(month, year)
        print (str(MovieNameAndUrlList))
        for movieNameAndUrl in MovieNameAndUrlList:
            movieData = MovieData.MovieData()
            movieData.MovieName = movieNameAndUrl["Name"]
            movieData.MovieUrl = movieNameAndUrl["Url"]
            movieData.MovieMonth = month
            movieData.MovieYear = year
            BindRatingsAndCertificates(movieData)
            self.MovieQueue.append(movieData)
        print ("All pushed for month: " + month)

    def InsertMovieIntoDatabaseFromQueue(self):
        while(1):
            if (len(self.MovieQueue) > 0):
                movieData = self.MovieQueue.pop(0)
                InsertMovieIntoDatabase(movieData, movieData.MovieMonth, movieData.MovieYear)

    def StartCrawling(self):
        threadList = []
        print (str(self.monthsArray))
        for year in self.yearsArray:
            for month in self.monthsArray:
                print ("Creating thread")
                threadList.append(threading.Thread(target=self.PushRatingsToQueue, args=(month,year,)))
        for tds in threadList:
            print ("Starting thread")
            tds.start()
        y = threading.Thread(target=self.InsertMovieIntoDatabaseFromQueue)
        y.start()