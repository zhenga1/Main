Iterable to linked list:
```python
def it_to_link(lis):
	if lis == []:
		return Link.empty
	link = Link(lis[0])
	iterate = link
	for i in range(1,len(lis)):
		iterate.rest = Link(lis[i])
		iterate = iterate.rest
	return link
```
