#include <stdio.h> 
#include <wiringPi.h> 
#include <wiringPiSPI.h> 
#include <wiringPiI2C.h> 
#define CS_ADC	7 
#define SPI_CHANNEL	0 
#define SPI_SPEED	1000000 
#define LED_I2C_ADDR	0x20 
#define OUT_PORT1	0x03 
#define CONFIG_PORT1	0x07 
const int aLedData[8] = {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80}; int fd; int adcRead(char adcChannel) { char buff[3]; int adcValue = 0; buff[0] = 0x06 |((adcChannel &0x07) >>2); buff[1] = ((adcChannel & 0x07)<<6); buff[2] = 0x00; digitalWrite(CS_ADC, LOW); wiringPiSPIDataRW(SPI_CHANNEL, buff, 3); buff[1] = 0x0F & buff[1]; adcValue = (buff[1] <<8 | buff[2]); digitalWrite(CS_ADC,HIGH); return adcValue; } void ledOnByRange(int x, int min, int max, int ledNo) { int i; int data = 0; if(x<max && x>=min) { for(i=0; i<ledNo; i++) { data = aLedData[i] |data; } wiringPiI2CWriteReg16(fd, OUT_PORT1, data); } } int main(void) { int adcValue_CDS = 0; wiringPiSetupGpio(); if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) <0) { return -1; } if((fd = wiringPiI2CSetup(LED_I2C_ADDR)) <0) { return -1; } pinMode(CS_ADC, OUTPUT); wiringPiI2CWriteReg16(fd, CONFIG_PORT1, 0x0000); while(1) { adcValue_CDS = adcRead(0); printf("CDS = %u\n", adcValue_CDS); delay(100); ledOnByRange(adcValue_CDS, 3700, 4000, 8); ledOnByRange(adcValue_CDS, 3200, 3700, 4); ledOnByRange(adcValue_CDS, 900, 3200, 1); ledOnByRange(adcValue_CDS, 0,900,0); } return 0; }
