#ifndef HELPER_FUNCTIONS_H_
#define HELPER_FUNCTIONS_H_

#include <stdint.h>
#include "uart.h"

void delay_ms(uint32_t delay);
void initClocks(void);
void init_systick(void);
void SysTick_Handler(void);

#endif
