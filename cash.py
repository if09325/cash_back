cash_back = int(input("Bonjour, quel montant à rendre ?: "))
monnaie = {
	'two euros':0,
	'five euros':0,
	'ten euros':0
}

def __valuesDisplayer__(dictry):
	for i in dictry.items():
		print (i)
		
def __resultDictionary__(monnaie, a,b,c):
	monnaie['two euros'] = a
	monnaie['five euros'] = b
	monnaie['ten euros'] = c
	return monnaie
	
#cas 2 euros optimal 
if cash_back%2 == 0 and cash_back <= 8 : 
	__resultDictionary__(monnaie,cash_back/2,0,0)
	__valuesDisplayer__(monnaie)
	
#cas 5 euros optimal
elif cash_back == 5 : 
	__resultDictionary__(monnaie,0,1,0)
	__valuesDisplayer__(monnaie)

#cas 10 euros optimal	
elif cash_back%10 == 0 : 
	__resultDictionary__(monnaie,0,0,cash_back/10)
	__valuesDisplayer__(monnaie)	

#cas plus complexe 
else : 
	
		if (cash_back%10)%2 == 0 : 
			__resultDictionary__(monnaie,((cash_back%10)/2), 0, int(cash_back/10))
			__valuesDisplayer__(monnaie)
			
		elif (cash_back%10)%5 == 0 : 
			__resultDictionary__(monnaie, 0, ((cash_back%10)/5), int(cash_back/10))
			__valuesDisplayer__(monnaie)
		
		elif ((cash_back%10)%5)%2 == 0 : 
			__resultDictionary__(monnaie, ((cash_back%10)%5)/2, int((cash_back%10)/5), int(cash_back/10))
			__valuesDisplayer__(monnaie)
		else :
			print("Impossible de rendre la monnaie dans ce cas là")
		
	
	
	
	
	

