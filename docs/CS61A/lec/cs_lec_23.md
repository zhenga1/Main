# Create Table
```sql
CREATE TABLE expression syntax:
```
And then you can define columns using the:
`column-def` and the `column-constraint`
```sql
CREATE TABLE numbers(n, note);
CREATE TABLE numbers(n UNIQUE, note);
CREATE TABLE numbers(n, note DEFAULT "No comment");
```
![[chrome_odJjmHPhXv.png]]
This will take an existing table (say, with two columns...)
- To insert into one column:
	- `INSERT INTO t VALUES (value)`;
- To insert into both columns:
	- `INSERT INTO t VALUES (values1,values2)`
We see that the values are the respective **values** of the various columns of the rows. The above commands adds a new **row** to the existing table `t`.

![[chrome_PCVNlkR1OY.png]]
```sql
UPDATE ints SET prime=0 WHERE n > 2 AND n%2=0 AND n%3=0 AND n%5=0
```
This effectively makes numbers that divide either $2,3,5$ not a prime anymore. 

![[chrome_UXdk5Da22W.png]]
Example codes:
```sql
DELETE FROM ints WHERE prime=0;
```
This will `DELETE` from the table `ints`, the rows where the column `prime=0`
```python
import sqlite3

db = sqlite3.Connection('db')
db.execute('CREATE TABLE nums AS SELECT 2, 3 UNION SELECT 4, 5')
db.execute('INSERT INTO nums VALUES (?, ?), (?, ?):', range(6, 10))
print(db.execute('SELECT * FROM nums:*').fetchall())
db.command()
```
We see that, using **python**, we can use the $?$ notation to get the string. The `db.execute` takes a string which uses the $?$ notation for the formatting, whereby the $?$ represents a variable which is given later . 

This is the example code, a python implementation of the **blackjack** game:

```python
import random
import readline
import sqlite3

# SQL Intro

# The number.db file can be made on the spot, as a text file
# However, the file likely must exist, otherwise the python cannot 
# connect to the database.
db = sqlite3.Connection('number.db')
db.execute('CREATE TABLE nums AS SELECT 2, 3 UNION SELECT 4, 5;')
db.execute('INSERT INTO nums VALUES (?, ?), (?, ?);', range(6, 10))
print(db.execute('SELECT * FROM nums;').fetchall())
db.commit()

# SQL Injection

db = sqlite3.Connection(":memory:")
db.execute("CREATE TABLE Students(name);")
db.execute("INSERT INTO Students VALUES ('John');")

def add_name(name):
    cmd = "INSERT INTO Students VALUES ('" + name + "');"
    print("Executing:", cmd)
    db.executescript(cmd)
    print("Students:", db.execute("select * from Students").fetchall())

def add_name_safe(name):
    db.execute("INSERT INTO Students VALUES (?)", [name])
    print("Students:", db.execute("select * from Students").fetchall())

add_name_safe("Jack")
add_name_safe("Jill")
add_name_safe("Robert'); DROP TABLE Students; --");

# Blackjack

points = {'A': 1, 'J': 10, 'Q': 10, 'K':10}
points.update({n: n for n in range(2, 11)})

def hand_score(hand):
    """Total score for a hand."""
    total = sum([points[card] for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

db = sqlite3.Connection('cards.db')
sql = db.execute
sql('DROP TABLE IF EXISTS cards')
sql('CREATE TABLE cards(card, place);')

def play(card, place):
    """Play a card so that the player can see it."""
    sql('INSERT INTO cards VALUES (?, ?)', (card, place))
    db.commit()

def score(who):
    """Compute the hand score for the player or dealer."""
    cards = sql('SELECT * from cards where place = ?;', [who])
    return hand_score([card for card, place in cards.fetchall()])

def bust(who):
    """Check if the player or dealer went bust."""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck):
    """Play a hand of Blackjack."""
    play(deck.pop(), player)
    play(deck.pop(), dealer)
    play(deck.pop(), player)
    hidden = deck.pop()

    while 'y' in input("Hit? ").lower():
        play(deck.pop(), player)
        if bust(player):
            print(player, "went bust!")
            return

    play(hidden, dealer)

    while score(dealer) < 17:
        play(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, "went bust!")
            return

    print(player, score(player), "and", dealer, score(dealer))

deck = list(points.keys()) * 4
random.shuffle(deck)
while len(deck) > 10:
    print('\nDealing...')
    play_hand(deck)
    sql('UPDATE cards SET place="Discard";')

```
# SQL Injection attack
This is an example using SQL Injection 
![[WhatsApp Image 2022-11-28 at 1.52.36 PM.jpeg]]
When you are creating a sql string using other people's / user inputs, sometimes you can get some unexpected behaviours. 