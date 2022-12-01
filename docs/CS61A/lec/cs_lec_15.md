#r/lecture
- Lecture notes: link

# Lecture: 10/19
```jupyter
print("Hello world i am cool")
```
**Separation of Concerns**
- A design principle: Isolate different parts of a program that addresses different concerns
- A **modular component** can be developed and tested independently 

# Modular Design examples in the projects
**Hog**
Hog game simulator:
- Game rules
- Ordering of events
- State tracking to determine the winner
Game Commentary:
- Event descriptions
- User input
Player Strategies:
- Decision rules
- Strategy parameers(e.g. margins and number of dice)
**Ants:**
Ants game simulator
- Order of actions
- Food tracking
- Game ending conditions
Actions
- Characteristics of differnet ants and bees
Tunnel structure
- Entrances and exits 
- Locations of insectos

**Restaurant Search Data**
Given the following data, look up a restaurant by name and show related restaurants.
{"businesses_id": "lksajelk;r", "name":"Cafe 3", "stars":"2.0","price:":1,...}
{"businesses_id": "lksajelk;r", "name":"Cafe 3", "stars":"2.0","price:":1,...} etc
![[WhatsApp Image 2022-10-19 at 1.23.17 PM.jpeg]]
![[EpicPen_b443jd1Umu.png]]
**Discussion Question: Most similar Restaurants**
Implenet **similar**, a **Restaurant** method that takes a positive integer $k$ and a function **similarity** that takes two restuarants as arguments and returns a number. higher similarity values indicate more similar restaurants. The **similar** method returns a list contianing the k most similar restaurants according to the **similarity** function, but not containing **self**


