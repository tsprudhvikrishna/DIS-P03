#This code file is to write reducer function on our project data set.
#Reducer function will take intermediate key, value pairs as input to the function and summarizes the data and produces key, value pairs as output.
#Reducer input: a.  actor_1_name  number_of_movies_count b.  director_name movie_title
#Reducer output: a.	 Will Smith 10 b. James Cameron Avatar

sorted = open("mapper_sorted.txt","r")   
results = open("reducer_output.txt", "w")   

actorTotal = 0        
oldMovie = None    
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisActor, thisMovie = datalist  # read into variables
    if oldMovie and oldMovie != thisActor:        
        results.write("{0}\t{1}\n".format(oldMovie, actorTotal))
        oldMovie = thisActor;
        actorTotal = 0

    oldMovie = thisActor            
    actorTotal += 1   

if oldMovie != None: 
    results.write("{0}\t{1}\n".format(oldMovie, actorTotal))

sorted.close() 
results.close() 

