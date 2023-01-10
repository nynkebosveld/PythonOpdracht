Super.py

1.For loop die hoeveelheid producten berekend met gebruik van een associatieve array
	
1.1Wat doet het:
	De for loop berekend met de gegevens die hij ophaalt uit 	de bought.csv file hoeveel items er van een bepaald 	product zijn. Hij kijkt ook naar de sold.csv file om te 	zorgen dat er geen dingen dubbel worden gerekend en 	deze in de inventory worden gezet. Hij kijkt naar de naam 	van het item en telt de items met dezelfde naam bij 	elkaar op. Hierdoor print hij bijvoorbeeld niet "aarbeien 	1x" 5 keer uit op je scherm maar zet hij "aardbeien 5x" 	neer.

1.2Waarom heb je voor deze manier gekozen:
	Ik heb gekozen om te werken met een associative array. 	Deze manier wordt universeel gebruikt wat het ook 	makkelijk maakt voor andere om de code te begrijpen. 	Tevens heb ik deze manier gebruikt omdat ik hier al 	kennis van had en hier dus goed mee kon werken.



2.Voor de profit functie heb ik gebruik gemaakt van csv readers

2.1Wat doet het:
	De profit functie leest eerst het bestand sold.csv om te 	kijken welke producten er zijn verkocht en wat hiervan de 	totale prijs is. Hierna leest hij het bestand bought,csv om 	te kijken voor hoeveel euro er aan producten is gekocht. 	Nadat hij beide getallen heeft opgehaald haalt hij het 	getal van de bought.csv van het getal van de sold.csv af 	om te kijken wat de winst is die er over is gebleven. Deze 	winst geeft hij terug. 
2.2Waarom heb je voor deze manier gekozen:
	Ik heb voor readers gekozen omdat er vereist was dat er 	met CSV bestanden gewerkt zou worden en dit de meest 	voor de hand liggende optie was



3.Voor de sold functie gebruik ik writers en readers om bestanden uit te lezen

3.1Wat doet het:
	De functie begint met 2 waardes, namelijk het product en 	de prijs. Hij gaat kijken of het product beschikbaar is door 	te kijken of er een hoger aantal producten zijn met die 	naam in de bought.csv file dan in de sold.cvs file. Dit om 	te kijken of het product wel te verkopen is. Indien dit zo is 	voegt hij het gekochte item toe aan de sold.csv file. Als 	het product niet in de bought.csv file staat of er te weinig 	van het product te koop is, zal er een error verschijnen. 	De error zal aangeven dat het product niet in stock is.

3.2Waarom heb je voor deze manier gekozen:
	Ik heb hier voor gekozen omdat dit in mijn ogen de 	makkelijkste manier is om met CSV bestanden te werken
	


