#ifndef PRESSURE_H_
#define PRESSURE_H_

#include "stm32f10x.h"
#include "helper_functions.h"

/* pins for HX711 0 */
#define HX711_0_PORT (GPIOA)
#define HX711_0_DOUT (GPIO_Pin_9)
#define HX711_0_SCK  (GPIO_Pin_8)


/* pins for HX711 1 */
#define HX711_1_DOUT_PORT (GPIOA)
#define HX711_1_DOUT (GPIO_Pin_15)

#define HX711_1_SCK_PORT (GPIOB)
#define HX711_1_SCK (GPIO_Pin_3)



#define HX711_T1 (5)
#define HX711_T3 (0)
#define HX711_T4 (0)

void initHX711(void);
int32_t readPressure(void);

#endif
