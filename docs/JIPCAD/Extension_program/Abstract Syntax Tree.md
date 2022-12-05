- A **parser** traces **the derivation of a sequence of tokens**
- But **the rest of the compiler** needs a structural representation of the program
- **Abstract Syntax Tree**
	- Like parse trees but ignore some details
	- Abreviated as **AST**

**Abstract Syntax Tree**
- Consider the grammar
	- $E \rightarrow$ int $| ( E ) | E + E$
- And the string
	- $5 + (2 + 3)$
- After lexical analysis (a list of tokens)
	- ![[chrome_WpLFS3D0QV.png]]
- During parsing we build a parse tree

**Abstract Syntax Trees**
- A parse tree:
- Traces the operation of the parser
- Captures nesting structure
- But too much information
	- Parentheses
	- Single-successor nodes
![[chrome_s0rRMTxJLr.png]]

- Also captures the nesting structure
- But <u>abstracts</u> from the concrete syntax 
	- So it therefore is more compact and easier to use
- An important data structure in a compiler
![[chrome_2BwElRRkvB.png]]


