sum_number([], 0).
sum_number([X|T], Sum) :-
    sum_number(T, Sum1), Sum is Sum1 + X.
    
    
?- sum_number([1,2,3,4,5], _X), write(_X).