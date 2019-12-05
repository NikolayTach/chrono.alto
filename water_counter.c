#include "defines.h"
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interupt.h>
#include "ustart.h"

ISR(USAR_RXC_vest)
{
}

int main (void)
{
   unit16_t t;
   USTART int();
   
   while(1)
   {
         ADCRA = 0; // Disable ADC
         ADMUX = 0;
         ADCRA = 1 << ADEN; // Enable ADC 
         ADCSRA |= 1 << ADSC; // Start conversion
         while (!(ADCRA & (1<<ADIF))) ;
         t = ADC;
         tx_str("0 ");
         tx_d(t);
