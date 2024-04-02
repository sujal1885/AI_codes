male(dashrath).
male(ram).
male(laxman).
male(bharat).
male(shatrugan).

female(sita).
female(kaushalya).

wife(kaushalya, dashrath).
wife(sita, ram).

parent(dashrath, ram).
parent(dashrath, laxman).
parent(dashrath, bharat).
parent(dashrath, shatrugan).
parent(kaushalya, ram).
parent(kaushalya, laxman).
parent(kaushalya, bharat).
parent(kaushalya, shatrugan).


father(X,Y):-male(X),parent(X,Y).
mother(X,Y):-female(X),parent(X,Y).

father_in_law(X,Y):-male(X),father(X,Z),wife(Y,Z).
mother_in_law(X,Y):-female(X),mother(X,Z),wife(Y,Z).
brother_in_law(X,Y):-male(X),father(Z,X),father(Z,P),wife(Y,P).
