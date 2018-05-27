# PopulationRiddleTest
Tests out a solution to a statistics riddle.

## The riddle goes like this:
Suppose in a hypothetical society it is required for every couple to raise one girl.
This means that for every couple who raises children, they continue to have children until they produce one girl, and then they stop.
Assume that the chance of getting a boy is 50% and the chance of getting a girl is 50%
What will the ratio of boys to girls be in this society?








# SPOILER:
The test code runs 100 million couples who each produce children until they produce a girl.
It prints out the final total number of boys : then the final total number of girls.
then it prints out the ratio  (boys/girls)

each test run, the ratio is almost exactly 1. sometimes over, sometimes under.

This can be explained by looking at the births in the society as one continuous line.

If one family produces :
G
Then we go to the next, who produces:
BBBG
Then next:
BG
Then next:
G

Instead of looking at it as a series of families who have a specific birthing strategy, 
you can view it as one continuous set of births:
GBBBGBGG

Under this view, the next birth that would happen at any given time simply adds either a boy or a girl, with a 50/50 chance.
when you look at it as a series of births, it seems obvious that the ratio would be 1:1

