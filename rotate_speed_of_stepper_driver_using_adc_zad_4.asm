// Program kontroluj¹cy prêdkoœæ obrotu silnika krokowego wykorzystuj¹c potencjometr i przetwornik analog-cyrf
// Stworzone na zaj. lab. na PWr w ramach pracy w³asnej 
// Bartosz WoŸniak 


.include "m8535def.inc"

ldi r16, low(ramend)
out spl, r16
ldi r16, high(ramend)
out sph, r16


ldi r16, 0b11111111
out ddrd, r16

ldi r16, 0b00000000
out ddra, r16

sbi adcsra, 7
sbi admux, 5


start:

	rcall pomiar

zero:
	ldi r17, 0b00000001
	out portd, r17
	rcall time1

	ldi r17, 0b00000010
	out portd, r17
	rcall time1

	ldi r17, 0b00000100
	out portd, r17
	rcall time1

	ldi r17, 0b00001000
	out portd, r17
	rcall time1

	rjmp start

pomiar:
	sbi adcsra, 6

	czekaj:
		sbic adcsra, 6
	in r16, adch
	out portd, r16
	ret


time1:
	in r16, adch
	delay1:
		ldi r19, 250
		delay2:
			dec r19
		brne delay2
		dec r16
		brne delay1

ret
