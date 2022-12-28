Our first building block is the notion of a **proposition**, which is simply a statement which is either true or false.

(1) Conjunction: P∧Q (“P and Q"). True only when both P and Q are true. 
(2) Disjunction: P∨Q (“P or Q"). True when at least one of P and Q is true. 
(3) Negation: ¬P (“not P"). True when P is false.

A fundamental principle known as the **law of the excluded middle** says that, for any proposition P, either P is true or ¬P is true (but not both). Thus $P ∨ ¬P$ is always true, regardless of the truth value of P. A propositional form that is always true regardless of the truth values of its variables is called a ***tautology***. Conversely, a statement such as P∧ ¬P, which is always false, is called a ***contradiction***.

A statement (compound sentence) is called a ***tautology*** if it always has the true value for all possible truth values of its propositional variables (simple sentences). 

A statement is called a ***contradiction*** if it always has the false value.

A statement is called a ***contingency*** if it can be either true or false, depending on the truth values of its propositional variables

p ∨ ¬p and (p → q) ∨ ¬q are *tautologies*. 
(p → q) ∧ p ∧ ¬q is a *contradiction*. 
(p → q) ∨ ¬p is a *contingency*

The most important and subtle propositional form is an implication: 
(4) **Implication**: P =⇒ Q (“P implies Q"). This is the same as “If P, then Q."

Note also that P ⇒ Q is logically equivalent to ¬P∨Q, as can be seen by comparing the last two columns of the above truth table: for all possible truth values of P and Q, P =⇒ Q and ¬P∨ Q take the same values (i.e., they have the same truth table). We write this as (P =⇒ Q) ≡ (¬P∨Q).

Implication is always true when $P$ is false. For statements such as “If pigs can fly, then horses can read" or “If 14 is odd then 1+2 = 18.". When an implication is stupidly true because the hypothesis is false, we say that it is vacuously true.

![[chrome_c8cY0CUm95.png]]

Sanity check! 
Use quantifiers to express the following two statements: “For all integers x, 2x + 1 is odd”, and “There exists an integer between 2 and 4”
1st one: $\forall x\in N, 2x+1$ is odd
2nd one: $\exists x\in N, x>2$ and $x<4$ 

¬(P∧Q) ≡ (¬P∨ ¬Q) 
¬(P∨Q) ≡ (¬P∧ ¬Q)
Complement of P conjunction with Q is disjunction of complement P and complement Q

## HARD STUFF
¬(P∧Q) ≡ (¬P∨ ¬Q) 
¬(P∨Q) ≡ (¬P∧ ¬Q)
De Morgan's laws
## Existence quantification:
∃x P(x) has true value if there exists $x$ such that $P(x)$ is true
∀x P(x) has true value if all possible $x$ leads to $P(x)$ being true. 

### Laws of negation:
¬(∀xP(x)) ≡ ∃x¬P(x) 
¬(∃xP(x)) ≡ ∀x¬P(x)

To see a more complex example, fix some universe and propositional formula P(x, y). 
Assume we have the proposition 
¬(∀x∃yP(x, y)) 
and we want to push the negation operator inside the quantifiers. By the above laws, we can do it as follows: 
¬(∀x∃yP(x, y)) ≡ ∃x¬(∃yP(x, y)) ≡ ∃x∀y¬P(x, y).

Sentence:
- There are at least 3 distinct integer n that satisfy P(n) condition:
$∃x∃y∃z(x \neq y∧y \neq z∧z \neq x∧P(x)∧P(y)∧P(z)).$
- There are at most three distinct integers x that satisfy P(x)
$∃x∃y∃z∀d(P(d) ⇒ d = x∨d = y∨d = z).$
*Description:* There exists $(x,y,z)$ such that for any $d$, $P(d)$ implies that $d$ must either be x or y or z 
$$∀x∀y∀v∀z((x \neq y∧y \neq v∧v \neq x∧x \neq z∧y \neq z∧v \neq z) =⇒ ¬(P(x)∧P(y)∧P(v)∧P(z)))$$
*Description:* For any $(x,y,v,z)$,  none of them are equal to each other implies that the either $P(x), P(y),P(v),P(z)$ one of them must be false

Finally, what if we want to express the sentence “there are **exactly** three distinct integers x that satisfy P(x)"? This is now easy: we can just use the conjunction of the two propositions above.
i.e.
$∃x∃y∃z∀d((x \neq y∧y \neq z∧z \neq x∧P(x)∧P(y)∧P(z)) ∧ (P(d) ⇒ d = x∨d = y∨d = z)).$
For statements p and q, if p ↔ q is a **tautology**, we say that p and q are ***logically equivalent*** or simply equivalent, written
$$p ⇔ q$$
If $p → q$ is a tautology, we write $p ⇒ q$, and say that $p$ logically implies $q$. Indeed, when $p$ has T value we must have that $q$ has T value too.
