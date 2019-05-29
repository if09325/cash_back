import math
#Demande de rentrer la valeur du cash_back
cash_back = int(input("Combien vous devez au client? : "))

#nombre possible de 2 euros {0,1,2,3,4}
how_many_two_euros = {
	0 : 0,
	1 : 3,
	2 : 1,
	3 : 4,
	4 : 2,
	5 : 0,
	5 : 3,
	7 : 1,
	8 : 4,
	9 : 2 
}

#Résultat du return sera de la forme suivante : (Dictionnaire)
Dictionary_returned = {
	'two euros':0,
	'five euros':0,
	'ten euros':0
}

#__Round_function__ va servir d'arrondir si 0.5 ou + en sup si non en inf || exemple : a = 1.5, ceil(a) = 2 et floor(a) = 1
def __Round_function__(numb2round): 
	if numb2round - int(numb2round) >= 0.5 : 
		return math.ceil(numb2round)
	else: 
		return math.floor(numb2round)

#__valuesDisplayer__ va servir comme moyen d'affichage 
def __valuesDisplayer__(dictry):
	for i in dictry.items():
		print (i)
		
#__resultDictionary__ va servir comme d'affectation dans le dictionnaire Dictionary_returned
def __resultDictionary__(Dictionary_returned, a,b,c):
	Dictionary_returned['two euros'] = a
	Dictionary_returned['five euros'] = b
	Dictionary_returned['ten euros'] = c
	return Dictionary_returned	

#Sans attendre on va exclure le cas 1 et 3 car pas moyen de rendre la monnaie 
if cash_back == 1 or cash_back == 3 : 
	print("Pas moyen de rendre la monnaie, WE'RE REALLY SORRY :-/ ")
	
##########ODD#################ODD################ODD#####################ODD#################ODD################ODD###########
#Case One :  cash_back est impair <=> cash_back%2 != 0 à partir de 5(5 included) car 1 & 3 exclus							 #
elif cash_back%2 != 0 : 																									 #					 
		for i in range(5,100): #100 n'est pas impair mais python ne va pas jusqu'à 100 mais max-1 soit 99 		     		 #
			if i == cash_back :																								 #
				__resultDictionary__(Dictionary_returned, how_many_two_euros[i%10],1,__Round_function__(i/10)-1)			 #
				__valuesDisplayer__(Dictionary_returned)																	 #			
																															 #
##########ODD#################ODD################ODD#####################ODD#################ODD################ODD###########

#Case Two :  cash_back est pair <=> cash_back%2 == 0 	
##########EVEN#################EVEN################EVEN#####################EVEN#################EVEN################EVEN#####
else : 																													   	 #
	for i in range(2,101): #101 n'est pas pair mais python ne va pas jusqu'à 101 mais max-1 soit 100 						 #
		if i == cash_back : 																								 #
			__resultDictionary__(Dictionary_returned, how_many_two_euros[i%10],0,i//10) 									 #
			__valuesDisplayer__(Dictionary_returned)  																		 #
																															 #
##########EVEN#################EVEN################EVEN#####################EVEN#################EVEN################EVEN#####










