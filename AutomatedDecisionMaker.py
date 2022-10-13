from random import choice

def food():
    speed = input("How fast do you want to eat? ")
    style = input("Do you want to sit down or take out? ")
    fast_takeout_restaurants = ['Panda', 'McDonalds', 'Wendys', 'Sheetz','Arbys','KFC', 
    'Popeyes','Burger King', 'Subway', 'Jersey Mikes', 'Dairy Queen', 'Taco Bell', 'Chic Fil A'
    , 'Jimmy Johns', 'Texas Hot Dogs']
    slow_takeout_restaurants = ['Five Guys', 'Best Food in Town', 'Jaidee Thai', 'Chipotle', 'Tims', 
    'All Star Pizza', 'Papa Johns', 'OIP']
    sitdown_restaurants = ['OG', 'J&G', 'Champs', 'Champs', 'La Fiesta', 'Roadhouse', 
    'Outback', 'Als', 'Zachs', 'Primantis', 'Stone Cellar', 'Lenas', 'Red Lobster', 'El Camp'
    , 'Longhorn', 'Red Robin', 'Dennys', 'Applebees', 'Aki', 'Hoss.s', 'Mamas']

    if speed == "fast":
        print(choice(fast_takeout_restaurants))
    if speed == "slow" and style == "takeout":
        print(choice(slow_takeout_restaurants))
    if speed == "slow" and style == "sitdown":
        print(choice(sitdown_restaurants))

def tv():
    style = input("what genre of TV show? ")
    funny = ['Big Bang', 'Cobra Kai', 'Ted Lasso', 'Rick and Morty', 'Spongebob', 'Family Guy',
    'Futurama', 'Aqua Teen Hunger Force', 'The Boys', 'The Office', 'Parks and Rec', 'Young Sheldon',
    'Shameless', 'Brooklynn Nine-Nine', 'Friends']
    action = ['Game of Thrones', 'Cobra Kai', 'House of the Dragon', 'The Mandalorian', 'NCIS'
    , 'CSI', 'Lucifer', 'The Witcher', 'Vikings', 'Squid Game', 'Attack on Titan', 'Reacher',
     'Chicago Fire', 'The Terminal List', 'The Grey Man']
    drama = ['The Good Doctor', 'Better Call Saul', 'Breaking Bad', 'Stranger Things', 'Succession',
     'The Walking Dead', 'Yellowstone', 'Euphoria', 'Peaky Blinders', 'Greys', 'Sopranos', 'NCIS']
    
    if style == "funny":
        print(choice(funny))
    if style == "drama":
        print(choice(drama))
    if style == "action":
        print(choice(action)) 

def movie():
    style = input("What genre of movie? ")
    funny = ['Step Brothers', 'White Chicks', 'Wedding Crashers', 'Bad Teacher', 'The Other Guys', 'Due Date'
    , 'Role Models', 'Jackass', 'Lets Be Cops', 'The Interview', 'Just Go With It', 'Grown Ups',
     '21 Jump Street', 'American Pie', 'Death at a Funeral', 'Fired Up', 'Tyler Perry', 'Ted', 'Rush Hour'
     , 'Talladega Nights']
    action = ['Top Gun', 'Thor', 'Iron Man', 'Avengers', 'The Woman King', 'Expendables', 'Jason Bourne'
    , 'John Wich', 'Fast and Furious', 'Jurassic', 'Batman', 'The Gray Man', 'Dr Strange', 'Uncharted', 
    'Prince of Persia', 'Interstellar', 'The Mummy', 'IT', 'Jason', 'Freddy Krueger', 'Mike Myers']
    sports = ['Remember The Titans', 'Rocky', 'Creed', 'Friday Night Lights', 'The Woman King'
    , 'Invincible', 'Never Back Down', 'Hustle', 'Warrior', 'Dodgeball', 'Waterboy', 'King Richard'
    , 'Blindside', 'Sandlot', 'Major League', 'Rush', 'Longest Yard', 'Happy Gilmore', 'Moneyball']

    if style == "funny":
        print(choice(funny))
    if style == "sports":
        print(choice(sports))
    if style == "action":
        print(choice(action)) 

thing = input("What topic do you need help with? ")
if thing == "food":
     food()
if thing == "tv":
    tv()
if thing == "movie":
    movie()