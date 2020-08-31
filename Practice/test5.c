#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>
#define CS_ADC	7 
#define SPI_CHANNEL	0 
#define SPI_SPEED	1000000 
int adcRead(char adcChannel) {
     char buff[3]; 
     int adcValue = 0; 
     buff[0] = 0x06 |((adcChannel & 0x07)>>2); buff[1] = ((adcChannel &0x07)<<6); buff[2] = 0x00; digitalWrite(CS_ADC,LOW); wiringPiSPIDataRW(SPI_CHANNEL, buff, 3); buff[1] = 0x0F & buff[1]; adcValue = (buff[1] <<8) | buff[2]; digitalWrite(CS_ADC,HIGH); return adcValue; } int main(void) { int adcValue_CDS = 0; wiringPiSetupGpio(); if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) <0) { return -1; } pinMode(CS_ADC, OUTPUT); while(1) { adcValue_CDS = adcRead(0); printf("CDS = %u\n",adcValue_CDS); delay(1000); } return 0; }
