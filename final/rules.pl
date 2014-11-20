%! Predicates
:- dynamic(lifter/1).
:- dynamic(powerlifter/1).
:- dynamic(bodybuilder/1).
:- dynamic(purpose/2).
:- dynamic(similar/2).

%! Rules
lifter(X) :- powerlifter(X) ; bodybuilder(X).
powerlifter(X) :- purpose(X, Y) , aresimilar(strength, Y).
bodybuilder(X) :- purpose(X, Y) , aresimilar(mass, Y).
powerbuilder(X) :- powerlifter(X) , bodybuilder(X).
aresimilar(X, Y) :- similar(X, Y) ; similar(Y, X) ; X = Y.

%! Facts
similar(strength, power).
similar(mass, looks).
similar(mass, size).
