#ifndef UART_H_
#define UART_H_

#include "stm32f10x.h"

#define USART_PORT (GPIOB)
#define USART_ID (USART1)
#define USART_RX_PIN (GPIO_Pin_7)
#define USART_TX_PIN (GPIO_Pin_6)

int _write(int fd, char *str, int len);
void initUart(void);

#endif
