# Computerteknologi HF1 - Klimaanlæg
Mark Pedersen & Mads Finseth 18-06-2020

## Projektbeskrivelse:
Vi har lavet et klimaanlæg, hvor en blæser sætter i gang hvis temperaturen er over 28C.

Vores projekt består af følgende komponenter:

● GrovePi

● Raspberry Pi Model B Rev 1.2

● Strømforsyning (PSU)

● 12V kabinet-blæser

● GrovePi Relay

● GrovePi DHT11

● GrovePi LED

● GrovePi Display.


Vi har jumpet en strømforsyning, så vi kan få strøm til vores blæser. For at sætte blæseren
til vores GrovePi, har vi en ledning fra blæser til molex, en ledning fra relæet til molex, og en
ledning fra blæser til relæet.
Vi har en temperaturføler som aktiverer vores relæ, når temperaturen når x antal grader (I
dette tilfælde 28C).
Da vi har blæseren til relæet, vil blæseren starte, og en LED vil begynde at lyse når
blæseren starter. Når temperaturen er under den værdi vi har sat, slukker både blæseren og
LED igen. Vi har et LED Display som viser temperaturen.

<br/>

## Billede af vores klimaanlæg:
## Vores kode:



# Links:
https://gpiozero.readthedocs.io/en/stable/index.html

