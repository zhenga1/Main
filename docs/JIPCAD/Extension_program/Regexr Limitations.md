HTML **==cannot be parsed==** using Regexr.

Reason why most langauges cannot be parsed using Regexr:
1) The most obvious is the lack of recursion: you cannot find a (regular) expression inside another one, unless you code it by hand for each level. Something that quickly became unmaintainable. But the larger problem is that it is not really scalable: if you are going to put together even just a few regular expressions, you are going to create a fragile mess that would be hard to maintain.
