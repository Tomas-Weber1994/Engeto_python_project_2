# Game Bulls and Cows

## Popis projektu
Jedná se o textový analyzátor - program, který se snaží prokousat libovolně dlouhým textem a zjistit o něm různé informace.

Program si od uživatele vyžádá přihlašovací jméno a heslo, zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty.Pokud není registrovaný, upozorní jej a program se ukončí. 

Registrováni jsou následující uživatelé:

Uživatelské jméno   Heslo
bob                  123
ann                 pass123
mike                password123
liz                 pass123

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
