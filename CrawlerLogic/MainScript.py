## Python File to Details from URL
from MovieDetailsCrawler import *
from ActorExtractionCrawler import *

MonthsArray = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
YearsArray = ["2017"]

# MDC = MovieDetailsCrawler(MonthsArray, YearsArray)
# MDC.StartCrawling()

AEC = ActorExtractor(["/title/tt5886046/","/title/tt6022946/"])
AEC.StartCrawling()
