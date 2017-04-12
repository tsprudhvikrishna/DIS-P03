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


# Steps to work on our MapReduce problem:
* Step1:- Go to the link provided, it takes to my repository. It is a public repository so anyone can access it.
* Step2:- Click on clone or download button. Its a green color button located at right side
* Step3:- Copy the web URL(link) to clone our MapReduce problems and all code files to your local machine.
* Step4:- On your local machine select a specific folder or location, example C:\Users\Prudvi Krishna.
* Step5:- Right click and you will get various options like view, sortBy, Open Git bash here, Git clone, Tortoise git etc.
* Step6:- Select and click on Git clone, a window will pop up. Paste the web URL copied (from Step3) on URL box and click OK.
* Step7:- Our MapReduce problem and all our code files are cloned or copied or downloaded into your local machine. Now run and see the output and play with our MapReduce problem.

# Steps to run MapReduce problem and check output:
* Step1:- My Mapper code is in mapper.py file, mapper output in mapper_output.txt file and you get sorted mapper output from mapper_sorted.txt file.
* Step2:- My Reducer code is in reducer.py file and you can get reducer output from reducer_output file.
* Step3:- Select the file which you want to work on.
* Step4:- Right click on that file and select open with Notepad++ or Notepad, you can see data. If you want to make some changes you can do.
* Step5:- Save the file.
* Step6:- After saving right click on foler and select Git bash here. A Git bash window will appear.
* Step7:- Type command "python fileName" and press enter to run that file, you can see output.
