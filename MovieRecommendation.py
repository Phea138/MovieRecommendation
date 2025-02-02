import pandas as pd
import numpy as np
from scipy.linalg import svd
import os
top_movie=20

def selectGenre():
    print("1.Action         2. Romance        3.Thriller")
    print("4.War            5.Animation       6.Crime   ")
    print("7.Horror         8.History         9.Adventure")
    print("10.Sport")
    genre=int(input("Select Your Genre of Movie that are Highly Rating: "))
    if(genre==1):
        Genre='Action'
        file='Action.csv'
    elif(genre==2):
        Genre='Romance'
        file='Romance.csv'
    elif(genre==3):
        Genre='Thriller'
        file='Thriller.csv'
    elif(genre==4):
        Genre='War'
        file='War.csv'
    elif(genre==5):
        Genre='Animation'
        file='Animation.csv'
    elif(genre==6):
        Genre='Crime'
        file='Crime.csv'
    elif(genre==7):
        Genre='Horror'
        file='Horror.csv'
    elif(genre==8):
        Genre='History'
        file='History.csv'
    elif(genre==9):
        Genre='Adventure'
        file='Adventure.csv'
    elif(genre==10):
        Genre='Sport'
        file='Sport.csv'
    else:
        print("Select Genre You want to Recommend")
        exit()
    os.system('cls')
    print(f"Top 20 {Genre} Movies are:  ")
    SVD(file)
    
    
    
def select_movie():
    movie = {
        'Animation': {'The Lion King', 'Spider-Man', 'The Bad Guys', 'Strange World', 'Inside Out'},
        'Action': {'Fast X', 'Shotgun Wedding', 'Plane', 'Avatar', 'John Wick'},
        'Romance': {'The Lost City', 'The King', 'West Side Story', '10 Things I Hate About You', 'The Lobster'},
        'Thriller': {'Glass Onion', 'Black Panther', 'M3GAN', 'Bullet Train', 'Blood'},
        'Adventure': {'True Spirit', 'The Super Mario', 'Black Adam', 'Harry Potter', 'The Hunger Games'},
        'History': {'The Woman King', 'Amsterdam', 'Mission Majnu', 'Argentina 1985', 'Kingdom of Heaven'},
        'Crime': {'The Batman', 'The Dark Knight', 'Killers of the Flower Moon', 'The Gentlemen', 'Nobody'},
        'War': {'Devotion', 'Official Secrets', 'Fury', 'Operation Mincemeat', 'The King'},
        'Sport': {'Cars', 'Rocky II', 'The Karate Kid', 'Ski School', 'The Survivor'},
        'Horror': {'Smile', 'Nope', 'Scream', 'The Black Phone', 'White Noise'}
    }
    count=0
    for movies in movie.values():
        for item in movies:
            print(f'{count}.{item}')
            count+=1
    all_movies = [movie for genre_movies in movie.values() for movie in genre_movies]
    
    m=int(input("Select Your Movie Above from 0 to 49: "))
    os.system('cls')
    print(f"You Seleted {all_movies[m]}")
    if(m>=0&m<=4):
        file='Animation.csv'
    elif(m>=5&m<=9):
        file='Action.csv'
    elif(m>=10&m<=14):
        file='Romance'
    elif(m>=15&m<=19):
        file='Thriller.csv'
    elif(m>=20&m<=24):
        file='Adventure.csv'
    elif(m>=25&m<=29):
        file='History.csv'
    elif(m>=30&m<=34):
        file='Crime.csv'
    elif(m>=35&m<=39):
        file='War.csv'
    elif(m>=40&m<=44):
        file='Sport.csv'
    elif(m>=45&m<=49):
        file='Horror.csv'
    print("The Top 20 Movies That are related: ")
    SVD(file)


def SVD(file):
    df = pd.read_csv(file, encoding='ISO-8859-1')
    rating=df.filter(like='User-').values
    U,S,Vt=svd(rating,full_matrices=False)
    diagonalMatrices=np.diag(S)
    A=np.dot(np.dot(U,diagonalMatrices),Vt)
    Average=A.mean(axis=1)
    SortValue=pd.Series(Average,index=df.index).sort_values(ascending=False).head(top_movie)
    Recommend=df.loc[SortValue.index,['Movie','Director','Runningtime','Year']]
    Recommend['Rating']=SortValue.values
    print(Recommend.to_string(index=False,header=True))



print("=============================================")
print("=            WELCOME TO CINEMA              =")
print("=============================================")
print("Press 1 to select movie")
print("Press 2 to find the top genre recommend")
select=int(input())

if(select==1):
    os.system('cls')
    print("Select Your Favourite Movie Below: ")
    select_movie()
elif(select==2):
    selectGenre()








