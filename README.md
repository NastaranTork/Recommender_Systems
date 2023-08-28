# Recommender_Systems
What are recommender systems? it actually will recommend things that you might be interested in purchasing based on your past behavior on the site. And that might include things that you rated or things that you bought.

## One technique is called user-based collaborative filtering:
* Build a matrix of things each user bought/viewed/rated
* Compute similarity scores between users
* Find users similar to you
* Recommend stuff they bought/viewed/rated that you haven't yet.
### Problems of user-based collaborative filtering:
1. Tasted of people can change overtime
2. People are more than things
3. There are some people that try to game the system that called shillling attacks.
## Second technique is the item-based collaborative filtering: 
* Find every pair of movies that were watched by the same person
* Measure the similarity of their ratings across all users who watched both
* Sort by movie, then by similarity strength
### Advantages of item-based collaborative filtering:
1. A movie doesn't change overtime
2. There are always more items than people
3. Harder to manipulate system
### Implementing an rating movies recommender
Look at the main.py file. I used MovieLens dataset.
   
   
#### (Note: Make sure that the behavior that you're considering is based on people actually spending money. So, you'll get more reliable results.)


  
