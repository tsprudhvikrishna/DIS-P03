f = open("movie_metadata.txt","r")  # open file, read-only raw data
o = open("mapper2_output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t") 
    #print data
    print len(data)
    if len(data) == 28:
        color, director_name, num_critic_for_reviews, duration, director_facebook_likes, actor_3_facebook_likes, actor_2_name, actor_1_facebook_likes, gross, genres, actor_1_name, movie_title, num_voted_users, cast_total_facebook_likes, actor_3_name, facenumber_in_poster, plot_keywords, movie_imdb_link, num_user_for_reviews, language, country, content_rating, budget, title_year, actor_2_facebook_likes, imdb_score, aspect_ratio, movie_facebook_likes = data
        print "{0}\t{1}".format(director_name, movie_title)
        o.write("{0}\t{1}\n".format(director_name, movie_title))
f.close()
o.close()
n = open("mapper2_output.txt","r")  # open file, read-only
s = open("mapper2_sorted.txt", "w") # open file, write
lines = n.readlines()
lines.sort()
print(lines)
for line in lines:
	s.write(line)
n.close()
s.close()