# Joining Two Tablees
Two tables $A$ and $B$ are joined by a comma to yield all combos of a row from A and a row from B.
```sql
CREATE TABLE dogs AS
	SELECT "abraham" AS name, "long" AS fur UNION
	
```

Example: Grandparents

# String Expressions
String values can be combined to form longer strings
```sql
sqlite> SELECT "hello," || "world";
hello, world
```
Basic Sring Manipulation is built into SQL, but differs from Python
```SQL
sqlite> CREATE TABLE phrase AS SELECT "hello, world" AS s;
sqlite> SELECT substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) FROM phrase;
low
```
Strings can be used to represent structured values, but doign so is rarely a good idea

# Cartesian Product of Two Tables
- We pair up every **row** within a table to every **row**  within the other table, such that each table's row is matched 1-to-1 with each other table's row.
- Essentially, if we have the first table with $a$ rows, and another table with $b$ rows, then our final **cartesian product table** would have $a\times b$ rows.