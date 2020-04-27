## Python File to Details from URL
from RequestMethods import *
from MySqlUtility import *
from MovieMethods import *
import threading
#from queue import Queue



def PushRatingsToQueue(months):
    for year in YearList:
        for month in months:
            MovieNameAndUrlList = GetMovieNameAndUrl(month, year)
            for movieNameAndUrl in MovieNameAndUrlList:
                movieData = MovieData.MovieData()
                movieData.MovieName = movieNameAndUrl["Name"]
                movieData.MovieUrl = movieNameAndUrl["Url"]
                movieData.MovieMonth = month
                movieData.MovieYear = year
                BindRatingsAndCertificates(movieData)
                MovieQueue.append(movieData)
            print ("All pushed for month: " + month)

def InsertMovieIntoDatabaseFromQueue():
    while(1):
        if (len(MovieQueue) > 0):
            movieData = MovieQueue.pop(0)
            InsertMovieIntoDatabase(movieData, movieData.MovieMonth, movieData.MovieYear)




global MovieQueue
MovieQueue = []
MonthList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
YearList = ["2018"]

threadList = []
for month in MonthList:
    print ("Creating thread")
    threadList.append(threading.Thread(target=PushRatingsToQueue, args=([month], )))

for tds in threadList:
    print ("Starting thread")
    tds.start()

y = threading.Thread(target=InsertMovieIntoDatabaseFromQueue)
y.start()
    
            