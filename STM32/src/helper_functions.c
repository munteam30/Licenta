#include <helper_functions.h>
#include "stm32f10x_rcc.h"
#include <stdint.h>

volatile uint32_t global_timer;

void initClocks(void)
{
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD, ENABLE);
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOE, ENABLE);
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO,  ENABLE);

    RCC_APB2PeriphClockCmd(RCC_APB2Periph_SPI1, ENABLE);
    RCC_APB1PeriphClockCmd(RCC_APB1Periph_SPI2, ENABLE);

    RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1, ENABLE);
    GPIO_PinRemapConfig(GPIO_Remap_USART1, ENABLE);
}

void delay_ms(uint32_t delay)
{
    uint32_t elapsed;
    uint32_t start = global_timer;
    do {
        elapsed = global_timer - start;
    } while (elapsed < delay) ;
}

void init_systick(void)
{
    NVIC_SetPriority(SysTick_IRQn, 1);
    SysTick_Config(SystemCoreClock/1000000);
}

//void SysTick_Handler(void)
//{
//    global_timer++;
//}
