## Python File to Details from URL
from MovieDetailsCrawler import *
from ActorExtractionCrawler import *


#MonthsArray = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
MonthsArray = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
YearsArray = ["2020"]

#MDC = MovieDetailsCrawler(MonthsArray, YearsArray)
#MDC.StartCrawling()


AEC = ActorExtractor()
AEC.StartCrawling()

