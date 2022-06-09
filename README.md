# Game Bulls and Cows

Popis projektu
V tomto projektu bude tvým cílem vytvořit textový analyzátor - program, který se bude umět prokousat libovolně dlouhým textem a zjistit o něm různé informace.

Ještě než začneš, budeš pracovat se zadanými předpřipravenými texty. Kód se ti pak bude lépe kontrolovat. Tyto texty jsou dostupné zde.



Tvůj program bude obsahovat následující:

Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
ZKOPÍROVAT KÓD
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...
Vyžádá si od uživatele přihlašovací jméno a heslo,
zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
pokud není registrovaný, upozorni jej a ukonči program.**
Registrováni jsou následující uživatelé:

+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+


Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.


Pro vybraný text spočítá následující statistiky:
počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.


Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
