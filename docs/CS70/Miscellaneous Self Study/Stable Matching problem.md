### Preference Lists
![[chrome_RIeSPHCosS.png]]
How to match job to candidate?
**Propose-and-Reject algorithm** (a.k.a. the Gale-Shapley algorithm), and we present it now.

We think of the algorithm as proceeding in “days” to have a clear unambiguous sense of discrete time

**Every Morning:** Each job proposes (i.e. makes an offer) to the most preferred candidate on its list who has not yet rejected this job. 

**Every Afternoon:** Each candidate collects all the offers she received in the morning; to the job offer she likes best among these, she responds “maybe” (she now has it in hand or on a string), and to the other offers she says “no” (i.e., she rejects them). (This is just a way for us to virtually model that there are no “exploding offers” and a job can’t withdraw an offer once an offer is made.) 

**Every Evening:** Each rejected job crosses off the candidate who rejected its offer from its list. The above loop is repeated each successive day until there are no offers rejected. At that point, each candidate has a job offer in hand (i.e. on a string); and on this day, each candidate accepts their offered job (i.e. the job offer she has in hand) and the algorithm terminates.

In this lecture we will focus on a much more basic criterion that is rooted in the idea of **autonomy**, namely **stability**. A matching is ***unstable*** if there is a job and a candidate who *both prefer working with each other* over their **current matchings**. We will call such a pair a ***==rogue couple==***. So a matching of n jobs and n candidates is stable if it has no rogue couples. Let us now recall our example from earlier:
![[chrome_w7612wCVr3.png]]
With this matching:
{(Approximation Inc., Christine), (Basis Co., Bridget), (Control Corp., Anita)}.
This is *unstable*, since Approximation Inc and Bridget are a  rogue couple. Both would prefer to be with each other. 

Example of stable matching
{(Basis Co., Anita), (Approximation Inc., Bridget), (Control Corp., Christine)}. 
Why is (Approximation Inc., Anita) not a rogue couple here? It’s certainly true that Approximation Inc. would rather work with Anita than its current employee Bridget. Unfortunately for it, however, Anita would rather be with her current employer (Basis Co.) than with Approximation Inc.

Note also that both Control Corp. and Christine are paired with their least favorite choice in this matching. Nevertheless, this does not violate stability since none of their more preferred choices would rather work with them than who they are matched with.

Before we discuss how to find a stable matching, let us ask a more basic question: Do stable matchings always exist? Surely the answer is yes, since we could start with any matching and seemingly make it more and more stable as follows: If there is a rogue couple, modify the current matching so that this couple is matched up. Repeat. Surely this procedure must result in a stable matching? Unfortunately this reasoning is not sound! Why? Although pairing up the rogue couple reduces the number of rogue couples by one, it may also create new rogue couples. So it is not at all clear that this procedure will terminate!
![[chrome_JCphGi0cbR.png]]
We claim that in this instance, there always exists a rogue couple for any matching. For example, the matching {(A,B), (C,D)} contains the rogue couple B and C. How about {(B,C), (A,D)}? This matching is unstable because now A and C are a rogue couple.
