# Database Management Systems
Database management systems (DBMS) ar important, heavily used, and interesting!

A table is a collection of records, which are rows that have a value for each column

A table has columns and rows
A **row** has a value for each column
A **column** has a name and a type.

The structured query language (SQL) is perhaps the most widely used programming language
![[chrome_rEVFmc8Jk1.png]]
SQL is a *declarative* programming language

# Declarative Programming
In **declarative languages** such as SQL and Prolog
- A "program" is a description of the desired result
- The interpreter figures out how to **generate the result**

In **imperative languages** such as Python and Scheme:
- A "program" is a description of computational processes
- The interpreter **carries out execution/evaluation rules**

```Sql
create table cities as
	select 38 as laitude, 122 as longitude, "Berkeley" as name union
	select 42 , 71 , "Cambridge" union
	select 45, 93, "Minneapolis";
```

There has been a lot of **declarative languages** that are created just to implement/visualise/layout various programs. 

# SQL Overview

The SQL language is an ANSI and ISO standard, but DBMS's implement custom variants
- A **select** statement creates a new table, etiher from scratch or by projecting a table
- A **create table** statement gives a global name to a table
- Lots of other statements exist: **analyze, delete, explain, insert, replace, update, etc.** 
- Most of the important action is in the **select** statement

# Selecting Value Literals
- A **select** statmeent always includes a comma-separated list of column descriptions
- A column description is expression, optionally followed by **as** aand a column name

Selecting literals creates a one-row table

The union of two select statements is a table containing the rows of both of their results

```sql
select "delano" as parent, "herbert" as child union
```
![[chrome_tsduZ7WK5N.png]]

# Select Statements Project  Existing Tables
![[chrome_0OHis61tZw.png]]
- A **select** statement can specify an input table using a **from** clause
- A subset of the rows of the input table can be selected using a **where** clause
- An ordering over the remaining rows can be declared using an **order by** clause.
- Column descriptions determine how each input row is projected to a result row
```sql
select [expression] as [name], [expression] as [name], ...;
select [columns] from [table] where [condition] order by [order];
select child from parents where parent = "abraham"
```

**child**
barack 
clinton
