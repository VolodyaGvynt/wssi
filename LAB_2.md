%zad 1

a_sibling(X, Y):-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y):-
    parent(X, Z), 
    parent(Z, Y).

b_first_sibling(X, Y):-
    grandparent(Z, X),  
    grandparent(Z, Y), 
    X \= Y.

c_cross_grandparents(X, Y):-
    grandparent(X, Z),
    grandparent(Y, Z),
    X \= Y.

d_step_child(X, Y):-
    parent(Z, X),
    \+ parent(Z, Y),
    X \= Y. 

e_half_sibling(X, Y):-
    parent(P, X),
    parent(P, Y),
    X \= Y,
    parent(PX, X), parent(PY, Y),
    PX \= PY,
    PX \= P, PY \= P.

f_half_uncle(X,Y):- 
    parent(X, Z),
    parent(W, Z),
	grandparent(G, Z),
    parent(G, Y).

g_niece(X, Y):-
    parent(Z, X),
    parent(G, X),
    parent(G, Y),
    grandparent(Z, Y),
	G \= Z. 
 
%zad2

kobieta(X):- 
    osoba(X), 
    \+ mezczyzna(X).

ojciec(X, Y):- 
    rodzic(X, Y), 
    mezczyzna(X).

matka(X, Y):- 
   rodzic(X, Y), 
   kobieta(X).

corka(X, Y):- 
    rodzic(Y, X), 
    kobieta(X).

brat_rodzony(X,Y):- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    mezczyzna(X), 
    X \= Y.

brat_przyrodni(X, Y):-
    rodzic(Z, X),
    rodzic(W, Y),
    Z \= W,
    mezczyzna(X),
    X \= Y.

kuzyn(X, Y) :-
    rodzic(Z, X), rodzic(G, Y),
    brat_rodzony(Z, G).

dziadek_od_strony_ojca(X, Y):-
    ojciec(X, Z),
    ojciec(Z, Y).

dziadek_od_strony_matki(X, Y):-
    ojciec(X, Z),
    matka(Z, Y).

dziadek(X, Y):-
    ojciec(X, Z),
    rodzic(Z, Y).

babcia(X, Y):-
    matka(X, Z),
    rodzic(Z, Y).

wnuczka(X, Y):-
    rodzic(X, Z),
    corka(Y, Z).

przodek_do2pokolenia_wstecz(X, Y):-
     (rodzic(X, Z), rodzic(Z, Y)) ; rodzic(X, Y).

przodek_do3pokolenia_wstecz(X, Y) :- 
    (rodzic(X, Z), rodzic(Z, W), rodzic(W, Y)) ; (rodzic(X, Z), rodzic(Z, Y)) ; rodzic(X, Y).



    
 





