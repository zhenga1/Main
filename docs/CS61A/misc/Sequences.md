**Sequences**
Sequences are ordered collections of values that supprot element-selection and have length. We've worked with lists, but other Python types are also sequences, such as strings

Since strings are sequences, we can do with strings many of same things we can do to lists. We can even loop through string just like we can with a list
```jupyter
x = 'I am not Oski.'
```
```jupyter
vowel_count=0
for i in range(len(x)):
	if x[i].lower() in 'aeiou':
		vowel_count+=1
```
```jupyter
vowel_count
```