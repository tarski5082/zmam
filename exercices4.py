
from bs4 import BeautifulSoup
import requests

"""
Header pour avoir une 
reponse à la requete
"""
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'}


url="https://www.imdb.com/search/title/?groups=top_1000&count=100&sort=user_rating,asc"

#
result = requests.get(url,headers=header)
htmlPage= result.text
content = BeautifulSoup(htmlPage,"html.parser")



#classement des films

movie_list=content.find_all("a",class_="ipc-lockup-overlay ipc-focusable")[0:10]
movie_title=[]

#Obtenir titre film
for i in movie_list:

	movie=str(i)
	movie=movie.split("View title page for")#precede le titre
	movie=movie[1].split("\" class") #suit le titre
	movie=movie[0] # Titre du film
	movie_title.append(movie)


#lien des dit films
link_tag=content.find_all("a",class_="ipc-title-link-wrapper")[0:10]
link_movie=[]

#lien à chaque fiche de film
for i in link_tag:
	link=str(i)
	link=link.split("href=\"")
	link=link[1].split("\" tabindex")
	link=link[0]
	link="https://www.imdb.com/fr"+link
	link_movie.append(link)

#Annee de sortie	

year_tag=content.find_all("span",class_="sc-f30335b4-7 jhjEEd dli-title-metadata-item")[0:30]
year_movie=[]
for i in range(0,30,3):
	year=str(year_tag[i])
	year=year.split("\">")
	year=year[1].split("</")
	year=year[0]
	year_movie.append(year)


#Note film
score_tag=content.find_all("span",class_="ipc-rating-star--rating")[0:10]
score_movie=[]
for i in score_tag:
	score=str(i)
	score=score.split("\">")
	score=score[1].split("</")
	score=score[0]
	score_movie.append(score)

#Description film
description_tag=content.find_all("div",class_="ipc-html-content-inner-div")[0:10]
description_movie=[]
for i in description_tag:
	description=str(i)
	description=description.split("\"presentation\">")
	description=description[1].split("</")
	description=description[0]
	description_movie.append(description)



movie_actor=[]
movie_director=[]
movie=genre=[]
for i in link_movie:
	response=requests.get(i,headers=header)
	soup=BeautifulSoup(response.text,"html.parser")
	actor=soup.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
	actor
	film_director=soup.find("li","ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
	genre=soup.find_all("a",class_="ipc-chip ipc-chip--on-baseAlt")

	print(film_director)
	print(actor)





	
	
	