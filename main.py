import pandas as pd
users = ['user_id','movie_id','rating']
userdata = pd.read_csv('u.data', sep='\t', names= users, usecols= range(3))

movies = ['movie_id', 'title']
moviedata = pd.read_csv('u.item', sep='|', encoding='ISO-8859-1', names= movies, usecols=range(2))

CombinedData = pd.merge(moviedata, userdata)
Ratings = CombinedData.pivot_table(index='user_id', columns='title', values='rating')

# The amount of correlation among all of movies
SimilarMovies = Ratings.corr()

# Remove movies which have watched by less than 100 people
SimilarMovies = Ratings.corr(method='pearson', min_periods=100)

# Testing system as a recommender
test_user = Ratings.loc[0].dropna()
Candidates = pd.Series()
for i in range(0,len(test_user.index)):
    sim = SimilarMovies[test_user.index[i]].dropna()
    sim = sim.map(lambda x:x*test_user[i])
    Candidates = Candidates.append(sim)

Candidates.sort_values(inplace = True, ascending= False)
filteredSims = Candidates.drop(test_user.index)
print(filteredSims)
