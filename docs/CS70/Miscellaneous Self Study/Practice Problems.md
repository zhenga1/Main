A ***celebrity*** at a party is someone whom everyone knows, yet who knows no one. Suppose that you are at a party with n people. For any pair of people A and B at the party, you can ask A if they know B and receive an honest answer. Give a recursive algorithm to determine whether there is a celebrity at the party, and if so who, by asking at most 3n−4 questions. (Note: for the purpose of this question you are just visiting the party to ask questions. What you are trying to determine is whether the n people actually attending the party include a celebrity.) Prove by induction that your algorithm always correctly identifies a celebrity if there is one, and that the number of questions is at most 3n−4.

Key insight: Asking any pair of people whether they know each other will always eliminate one person as celebrity. 
Algo:
- First randomly choose two people (A and B) and ask if one of them, A, knows B.
	- If true, then A is not a celebrity. B is next step
	- If false, then B is not a celebrity. A is next step
- Use next step on the following person, C. Whoever's status is still not determined is next step to ask the next random person. 
	- (n-1) questions eliminate n-1 people from being celebrity.
- NEXT VERIFICATION OF THE ONE AND ONLY
- CHECK THAT EVERYONE KNOWS CELEBRITY
	- (n-1) questions asked. 
- CHECK CELEBRITY KNOWS NO ONE
	- (n-1) questions asked
Total 3n-3
- CATCH, minus one since the celebrity (lets call C) must have been paired up with at least one person, so at least one of the CHECK questions is redundant.
Total 3n-4. 

Inductive proof:
- Base case. 2 people clearly can be identified by 2 questions. Use elimination method to eliminate one person as celebrity, then check whether the celebrity dude knows the other guy, or vice versa. 
- Inductive case. Assume works for $n=k$. 
	- For $n=k+1$, take first $k$ people and use algo to identify celeb THIS IS WRONG
	- JUST see above

A common recursively defined function is the factorial, defined for a nonnegative number n as n! = n(n − 1)(n − 2)...1, with base case 0! = 1. Let us reinforce our understanding of the connection between recursion and induction by considering the following theorem involving factorials. 
Theorem: For all n ∈ N, n > 1 =⇒ n! < n^n . Prove this theorem using induction. (Hint: In the Inductive Step, write (n+1)! = (n+1)· n!, and use the Induction Hypothesis.)
- Base case, we have 2! < 2^2 = 4.
- Inductive case: 
	- Let k! < k^k
	- Then (k+1)! = k! x (k+1) < k^k x (k+1) < (k+1)^k x (k+1) = (k+1)^(k+1). QED

Use the proof of Theorem 3.6 to design an algorithm that, given any amount of postage of at least 12c, outputs the numbers of 4c and 5c stamps that make up this postage. What’s the largest number of 5c stamps your algorithm will ever use?

Algo: 
- Take n as no of postage.
- Calculate m = n mod 4
- Set no of 5s as equal to m
- then no of 4s will be equal to (n-5m)//4

So max is 3. 

