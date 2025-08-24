# with open('projectData.txt', 'r') as project_data:
    # print(project_data.read())
    # print(project_data.read(6))
    # project_data.seek(0)
    # print(project_data.read(6))
    # print(project_data.read(6))
    # print(project_data.read(4))
    # print(project_data.tell())
    # print(project_data.read(2))
    # print(project_data.read(2))
    # project_data.seek(10)
    # print(project_data.read(project_data.tell()))

########################################################################

# courses=['Python', "JS", "C++","Java", "Ruby"]

# with open("langs.txt", 'x') as langs:
#     for i in courses:
#         langs.write(i+'\n')
    
#################################################################

with open('movies.txt', 'r') as movies:
    listMovies=movies.read().split('\n')
    arrMovies=[]
    for movie in listMovies:
        arrMovies.append(movie)

    print("Movies Array - ",arrMovies)
