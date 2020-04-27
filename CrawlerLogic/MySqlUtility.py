## Insert into MySql
import mysql.connector
from MovieData import *

def ExecuteStatement(sqlStatement):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="manipal1234",
    database="datascience"
    )
    mycursor = mydb.cursor()
    mycursor.execute(sqlStatement)
    mydb.commit()

def InsertMovieIntoDatabase(movieData, month, year):
    sqlString = "INSERT into movie (Name, URL, Rating, Month, Year) VALUES ('" + movieData.MovieName.replace("'","") + "','" + movieData.MovieUrl + "','" + str(movieData.MovieRating) + "','" + str(month) + "','" + str(year) + "');"
    ExecuteStatement(sqlString)
    