// Program kontroluj¹cy iloœæ zapalonych segmentów wyœwietlacza 7-segmentowego, wykorzystuj¹c potencjometr i przetwornik analog-cyrf
// Stworzone na zaj. lab. na PWr w ramach pracy w³asnej 
// Bartosz WoŸniak 


.include "m8535def.inc"

ldi r16, 0b11111111
out ddrd, r16

ldi r16, 0b00000000
out ddra, r16

sbi adcsra, 7
sbi admux, 5


start:
	sbi adcsra, 6

	czekaj:
		sbic adcsra, 6

	in r16, adch

	cpi r16, 0b00110011
	brlo zero

	cpi r16, 0b01100110
	brlo jeden

	cpi r16, 0b10010101
	brlo dwa

	cpi r16, 0b11000110
	brlo trzy

	cpi r16, 0b11111110
	brlo cztery

	cpi r16, 0b11111111
	brsh piec

zero:
	ldi r17, 0b11110111
	out portd, r17
	rjmp start

jeden:
	ldi r17, 0b11000001
	out portd, r17
	rjmp start

dwa:
	ldi r17, 0b10111011
	out portd, r17
	rjmp start
	
trzy:
	ldi r17, 0b11101011
	out portd, r17
	rjmp start

cztery:
	ldi r17, 0b11001101
	out portd, r17
	rjmp start
	
piec:
	ldi r17, 0b11101110
	out portd, r17
	rjmp start


//ldi r16, 0b00000000
//in r16, pina

//ldi r17, 0b11000001
//out admux, r17

//ldi r17, 0b11000110
//out adcsra, r17

//petla:

//	in r19, adcl
//	out portd, r19

//	rjmp petla
