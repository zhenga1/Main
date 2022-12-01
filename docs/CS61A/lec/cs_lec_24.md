# Aggregation

`select count(*) from tables`
- just simply counts the number of rows that are within a table
- there is a special keyword called **distinct**, which you can put into the **count** parameter

# Mixing Aggregate Functions and Single Values
Aggregate function also selects row in table, which may be meaningful

**List of aggregate functions:**
- Max -> Selects max of the column specified as value, as well as selects the relevant row in which the column specified equals to the maximum
- Min -> Selects min of the column specified as value, as well as selects the relevant row in which the column specified equals to the minimum
- Avg -> Selects avg of the column specified as value, as well as selects some random row that is not meaningful. 

`select max(weight), kind from animals`
`select min(kind), kind from animals`
What the aggregate function `max, min` do is they not only compute the max of the weight column, they also select the **kind** column element from the table animals that corresponds to where the `max, min` evaluate to the correct values.


# Grouping Rows
Rows in a table can be grouped, and aggregation is performed on each group
`[expression]  as [name], []`

![[chrome_sNfi3DEdb1.png]]
What **Group By** does is it basically groups everything, calculates by the **expression values**. 

