# DPLL
DPLL algorithm that takes in sentences in conjunctive normal form: 
sentence = [['a', 'b', 'c'], ['-d', 'r']] 
where the sentence above means:
( a or b or c ) and ( not d or r )
where a, b, c, d and r are propsitions that are True or False
and not a, not b, ... are the negations of their respecitve propositions

the DPLL algorith searches through the states of possible models (arrangements of propositions being True or False)
and returns a possible model (arrangement) if there is one, or states that there is not one

This algorithm avoids searching the whole wearch space of possible models by eliminating 'pure propositions' which is the case where, 
if there is an unassigned proposition in a clause of the given sentence, there is no unassigned negation of this proposition in any clause of the sentence.
In this case, the proposition is set to True.

As well as this, if there is only one unassigned value in a clause, and the clause is not already given to be True (have a True value). Then the proposition is set to be True

If any clause has only propositions that are set to false, the sentence cannot be satisfied by that model with any additional propositoins set

This algorithm uses bredth first search to search through the space of models, with the above given amendments.
