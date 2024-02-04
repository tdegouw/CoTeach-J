# Lesprogramma: Functioneel Programmeren

## Doel van de Les
Deze les heeft als doel om leerlingen in de vijfde klas van het VWO kennis te laten maken met de fundamentele concepten van functioneel programmeren. We zullen de basisprincipes van functioneel programmeren bespreken en praktische oefeningen uitvoeren om deze concepten toe te passen.

## Duur
2 uur

## Lesstructuur

### 1. **Introductie (15 min)**
   - Welkom en introductie van het onderwerp: Wat is functioneel programmeren?
   - Bespreking van het verschil tussen imperatief en functioneel programmeren.
   - Benadruk het belang van functies als eerste klas burgers.

### 2. **Basisconcepten van Functioneel Programmeren (45 min)**
   - **Pure Functies:**
     - Definitie van pure functies en hun voordelen.
     - Voorbeelden van pure en niet-zuivere functies.

   - **Immutabiliteit:**
     - Uitleg over immutabiliteit en waarom het belangrijk is.
     - Vergelijking met mutable datastructuren.

   - **First Class Functions:**
     - Definitie van first class functions.
     - Demonstratie van het gebruik van functies als argumenten en teruggegeven waarden.

```
def f(x):
    return x + 3
def g(function, x):
    return function(x) * function(x)
print(g(f, 7))
```


### 3. **Praktische Oefeningen (40 min)**
   - **Oefening 1: Schrijven van Pure Functies (20 min)**
     - Leerlingen schrijven en bespreken enkele pure functies in een gekozen programmeertaal (bijvoorbeeld pseudocode).

   - **Oefening 2: Gebruik van Immutable Datastructures (20 min)**
     - Leerlingen passen immutabiliteit toe door een eenvoudige applicatie te implementeren met behulp van onveranderlijke gegevensstructuren.

### 4. **Pauze (10 min)**
   - Korte pauze voor ontspanning en vragen.

### 5. **Hoogere-Orde Functies (30 min)**
   - **Definitie en Voorbeelden:**
     - Uitleg van hogere-orde functies.
     - Demonstratie van map, filter en reduce.

   - **Toepassing in Praktijk (10 min)**
     - Toepassen van hogere-orde functies in een groepsopdracht.

### 6. **Afsluitende Discussie en Samenvatting (20 min)**
   - Bespreking van de uitgevoerde oefeningen en opdrachten.
   - Herhaling van de belangrijkste concepten.
   - Mogelijkheid voor vragen en discussie.

## Huiswerk
Leerlingen krijgen een eenvoudige programmeeropdracht waarin ze de geleerde concepten toepassen. Hiermee wordt verwacht dat ze begrip ontwikkelen voor functioneel programmeren in een praktische context.

---

*Opmerking: Zorg ervoor dat de programmeertaal die wordt gebruikt toegankelijk is voor de leerlingen en past bij de inhoud van de les.*
