
#include <inc/pressure.h>

void initHX711(){
    /* configure gpio pins fo HX711 comm */
	GPIO_InitTypeDef gpio;
    GPIO_StructInit(&gpio);
    gpio.GPIO_Speed = GPIO_Speed_50MHz;
    /* initialize SCK as Push-Pull */
    gpio.GPIO_Pin = HX711_0_SCK;
    gpio.GPIO_Mode = GPIO_Mode_Out_PP;
    GPIO_Init(HX711_0_PORT, &gpio);
    /* initialize SCK as Push-Pull */
    gpio.GPIO_Pin = HX711_1_SCK;
    gpio.GPIO_Mode = GPIO_Mode_Out_PP;
    GPIO_Init(HX711_1_SCK_PORT, &gpio);
    /* initialize DOUT as floating input */
    gpio.GPIO_Pin = HX711_0_DOUT;
    gpio.GPIO_Mode = GPIO_Mode_IN_FLOATING;
    GPIO_Init(HX711_0_PORT, &gpio);
    /* initialize DOUT as floating input */
    gpio.GPIO_Pin = HX711_1_DOUT;
    gpio.GPIO_Mode = GPIO_Mode_IN_FLOATING;
    GPIO_Init(HX711_1_DOUT_PORT, &gpio);

}

int32_t readPressure1(){
		int32_t pressureValue = 0;
    	//comment next line while testing
        //delay_ms(HX711_T1);
        uint8_t i;
        for (i = 0; i < 24; i++){
        	GPIO_SetBits(HX711_0_PORT, HX711_0_SCK);
        	//delay_ms(HX711_T3);
        	// sample
        	pressureValue |= (GPIO_ReadInputDataBit(HX711_0_PORT, HX711_0_DOUT));
        	pressureValue <<= 1;
        	GPIO_ResetBits(HX711_0_PORT, HX711_0_SCK);
        	//delay_ms(HX711_T4);
        }
        /* shift one more bit to make 25 */
    	GPIO_SetBits(HX711_0_PORT, HX711_0_SCK);
    	//delay_ms(HX711_T3);
    	GPIO_ResetBits(HX711_0_PORT, HX711_0_SCK);
    	//delay_ms(HX711_T4);

    	pressureValue <<= 8;

    	return pressureValue;
}
int32_t readPressure2(){
		int32_t pressureValue = 0;
    	//comment next line while testing
        //delay_ms(HX711_T1);
        uint8_t i;
        for (i = 0; i < 24; i++){
        	GPIO_SetBits(HX711_1_SCK_PORT, HX711_1_SCK);
        	//delay_ms(HX711_T3);
        	// sample
        	pressureValue |= (GPIO_ReadInputDataBit(HX711_1_DOUT_PORT, HX711_1_DOUT));
        	pressureValue <<= 1;
        	GPIO_ResetBits(HX711_1_SCK_PORT, HX711_1_SCK);
        	//delay_ms(HX711_T4);
        }
        /* shift one more bit to make 25 */
    	GPIO_SetBits(HX711_1_SCK_PORT, HX711_1_SCK);
    	//delay_ms(HX711_T3);
    	GPIO_ResetBits(HX711_1_SCK_PORT, HX711_1_SCK);
    	//delay_ms(HX711_T4);

    	pressureValue <<= 8;

    	return pressureValue;
}
