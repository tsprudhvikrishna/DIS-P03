#This code file is to write mapper function on our project data set.
#Mapper function will take data set as input to the function and performs sort/shuffle and gives intermediate key, value pairs as output.
#Mapper input: color	director_name	num_critic_for_reviews	duration	director_facebook_likes	actor_3_facebook_likes	actor_2_name	actor_1_facebook_likes	gross	genres	actor_1_name	movie_title	num_voted_users	cast_total_facebook_likes	actor_3_name	facenumber_in_poster	plot_keywords	movie_imdb_link	num_user_for_reviews	language	country	content_rating	budget	title_year	actor_2_facebook_likes	imdb_score	aspect_ratio	movie_facebook_likes
#Mapper Output: a.  actor_1_name  number_of_movies_count b.  director_name movie_title

 
f = open("movie_metadata.txt","r")  # open file, read-only raw data
o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t") 
    #print data
    print len(data)
    if len(data) == 28:
        color, director_name, num_critic_for_reviews, duration, director_facebook_likes, actor_3_facebook_likes, actor_2_name, actor_1_facebook_likes, gross, genres, actor_1_name, movie_title, num_voted_users, cast_total_facebook_likes, actor_3_name, facenumber_in_poster, plot_keywords, movie_imdb_link, num_user_for_reviews, language, country, content_rating, budget, title_year, actor_2_facebook_likes, imdb_score, aspect_ratio, movie_facebook_likes = data
        print "{0}\t{1}".format(actor_1_name, movie_title)
        o.write("{0}\t{1}\n".format(actor_1_name, movie_title))
f.close()
o.close()
"""n = open("o.txt","r")  # open file, read-only
s = open("s.txt", "w") # open file, write
lines = n.readlines()
lines.sort()
print(lines)
for line in lines:
	s.write(line)
n.close()
s.close()"""
