/*
******************************************************************************
File:     main.c
Info:     Generated by Atollic TrueSTUDIO(R) 9.1.0   2020-08-20

The MIT License (MIT)
Copyright (c) 2018 STMicroelectronics

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

******************************************************************************
*/

/* Includes */

#include <stddef.h>
#include "stm32f10x.h"
#include <stdio.h>
#include <stdlib.h>
#include "gyroAccel.h"
#include "spi.h"
#include "uart.h"
#include "helper_functions.h"

//#include "pressure.h"

int var1=0,var2= 0,var3 = 0,var4 = 0,var5 = 0,var6 = 0,var7 = 0,var8 = 0;
int varx1=0,varx2= 0,varx3 = 0,varx4 = 0,varx5 = 0,varx6 = 0,varx7 = 0,varx9 = 0,varx8 = 0 , varx10 = 0;
int val[4];
/**
**===========================================================================
**
**  Abstract: main program
**
**===========================================================================
*/
int16_t extremitati(int16_t val[]);
int16_t filtrareValoriMediiX(int16_t variabila);
int16_t filtrareValoriMediiY(int16_t variabila);
int main(void)
{	initClocks();
	initUart();
  //  initGyro();

    //delay_ms(10000); //10ms
    printf("mihai");
    int16_t poz[2];
    int16_t acc[2];
    int16_t gyroValues[6];


    while(1){

    	gyroRead(gyroValues);
        for(int i = 0 ; i <3; i++){

    		if(gyroValues[i+3] > -11 && gyroValues[i+3] < 11)	gyroValues[i+3] = 0;
    		if(gyroValues[i+3] > 4140)  gyroValues[i+3] = 4100;
    		if(gyroValues[i+3] < -4140)	gyroValues[i+3] = -4100;

    		poz[i] = gyroValues[i+3] / 23;

    	}
    	 //RESTRICTIONAREA PENTRU 360* PE AXA OY

    	    		if(poz[1] > 0 && poz [2] > 0){
    	    			int temp = poz[1];
    	    			poz[1] = -temp / 2;
    	    		}

    	    		else if(poz[1] > 0 && poz [2] < 0){
    	    				poz[1] = -(90 + (90 - poz[1]/2));
    	    			}
    	    		else if(poz[1] < 0 && poz [2] < 0){
    	    		    				poz[1] = (90 + (90 + poz[1]/2));
    	    		}
    	    		else if(poz[1] < 0 && poz [2] > 0)
    					{ int temp = poz[1];
    	    			poz[1] = -temp/2;}

   //RESTRICTIONAREA PENTRU 360* PE AXA OX

					if(poz[0] > 0 && poz [2] > 0){
						int temp = poz[0];
						poz[0] = -temp / 2;
					}

					else if(poz[0] > 0 && poz [2] < 0){
								poz[0] = -(90 + (90 - poz[0]/2));
							}
					else if(poz[0] < 0 && poz [2] < 0){
										poz[0] = (90 + (90 + poz[0]/2));

					}
					else if(poz[0] < 0 && poz [2] > 0)
						{ int temp = poz[0];
						poz[0] = -temp/2;}
    //Configurare Acceleratie
    	  for(int j = 0; j< 2;j++)
    	  acc[j] = gyroValues[j] * 0.00244; //    m/(s^2)

    	  for(int i = 0 ;i<5;i++)
    	  {		poz[0] = filtrareValoriMediiX(poz[0]);
    	  		val[i] = poz[0];}

    	 // printf("%d %d %d %d %d ",val[0],val[1],val[2],val[3],val[4]);
    	// poz[0] = extremitati(val);
    	//  printf("    %d    ",poz[0]);
    	  poz[1] = filtrareValoriMediiY(poz[1]);


// Print doar pozitii
    	//printf("X= %d,Y= %d,Z= %d\n", poz[0] , poz[1],poz[2] );

// Print pozitii si accelerari
    	printf("Mihai");

    	printf("%d %d ", acc[0], acc[1]);
    	delay_ms(2000);  // ------> desi scrie dealy milisec inseamna delay micro sec deci pt o sec ai nevoie de 1 000 000
    	printf("X= %d,Y= %d,Z= %d\n" , poz[0],poz[1],poz[2]);

    }


}

int16_t filtrareValoriMediiX(int16_t variabila){
	int iesire;



	varx5 = varx4;
	varx4 = varx3;
	varx3 = varx2;
	varx2 = varx1;
	varx1 = variabila;


	iesire = (varx1+varx2+varx3+varx4+varx5)/5;

    //printf("%d %d %d %d %d ", varx1, varx2, varx3, varx4, varx5);
	return iesire;
}
int16_t filtrareValoriMediiY(int16_t variabila){
	int iesire;



	var8 = var7;
	var7 = var6;
	var6 = var5;
	var5 = var4;
	var4 = var3;
	var3 = var2;
	var2 = var1;
	var1 = variabila;



	iesire = (var1+var2+var3+var4+var5+var6+var7+var8)/8;

	return iesire;
}

int16_t extremitati(int16_t val[]){
int16_t medie;
	for(int i = 0; i<4;i++)
	{

	if(val[i+1]<= 175 && val[i+1] >= -175)
		if(val[i+1] >= val[i] + 70 || val[i+1] <= val[i] - 70)
			val[i+1] = val[i];
	}

	medie = val[3];
	return medie;
}

#ifdef  USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *   where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */

  /* Infinite loop */
  while (1)
  {
  }
}
#endif

/*
 * Minimal __assert_func used by the assert() macro
 * */
void __assert_func(const char *file, int line, const char *func, const char *failedexpr)
{
	(void) file;
	(void) line;
	(void) func;
	(void) failedexpr;
  while(1)
  {}
}

/*
 * Minimal __assert() uses __assert__func()
 * */
void __assert(const char *file, int line, const char *failedexpr)
{
   __assert_func (file, line, NULL, failedexpr);
}

#ifdef USE_SEE
#ifndef USE_DEFAULT_TIMEOUT_CALLBACK
/**
  * @brief  Basic management of the timeout situation.
  * @param  None.
  * @retval sEE_FAIL.
  */
uint32_t sEE_TIMEOUT_UserCallback(void)
{
  /* Return with error code */
  return sEE_FAIL;
}
#endif
#endif /* USE_SEE */

