#Regex 
 - all characters that are not word characters

old codes:
```json
{
	"name": "keyword.control.nome",
	"match": "\\b(point ([a-zA-Z0-9]+) ([\( \)]) endpoint)\\b"
},
```

```json
"\\bpoint ([a-zA-Z0-9]+) (\\([\\d*[.,]?\\d*] [\\d*[.,]?\\d*] [\\d*[.,]?\\d*]\\) endpoint)"
```

```json
\\bpoint ([a-zA-Z0-9]+) (\\([\\s0-9.,]\\)) endpoint\\b
```
```json
string.quoted.double.nome
support.variable.property
```

