# DIS-P03
DIS final project team P03
1.	Team Number: P05.
2.	Team Members: Krishna Teja, Samineni
                              Prudvi Krishna, Tarugu Subbaiah
3.	Summary: Our project is about metadata of the movies, it contains huge amount of data regarding movies like movie name, director of the movie, actors, budget, movie collections, year released and lot more.
4.	About Data Source: Our data source contains 1.5 Mega Bytes of information with more than 5000 records. The file extension is .txt and it is tab delimited. Format is structured.
5.	Link to data source: https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset (Links to an external site.)
6.	Volume and variety of our data source makes it a big data problem
7.	MapReduce problems: 
a.	Actor and number of movies he acted i.e. key is actor and value is number of movies he acted.
b.	For each director find the movie with highest imdb score
8.	Mapper input: color	director_name	num_critic_for_reviews	duration	director_facebook_likes	actor_3_facebook_likes	actor_2_name	actor_1_facebook_likes	gross	genres	actor_1_name	movie_title	num_voted_users	cast_total_facebook_likes	actor_3_name	facenumber_in_poster	plot_keywords	movie_imdb_link	num_user_for_reviews	language	country	content_rating	budget	title_year	actor_2_facebook_likes	imdb_score	aspect_ratio	movie_facebook_likes
9.	Mapper output/ Reducer input: 
a.  actor_1_name  number_of_movies_count
b.  director_name movie_title
       
10.	Example of Reducer output:  
a.	 Will Smith 10
b.	Hames Cameron Avatar
11.	Language: Python.
12.	Process: Our processing will be numeric.

Anyone can pull our reposiotry from GitHub by using the link https://github.com/tsprudhvikrishna/DIS-P03 It is a public repository.

