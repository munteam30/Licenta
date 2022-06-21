#include <inc/uart.h>

void initUart(void)
 {
 	USART_InitTypeDef usartinit;
 	GPIO_InitTypeDef gpio;
    GPIO_StructInit(&gpio);
 	gpio.GPIO_Pin = USART_TX_PIN; //TX
 	gpio.GPIO_Mode = GPIO_Mode_AF_PP;
 	gpio.GPIO_Speed = GPIO_Speed_50MHz;
 	GPIO_Init(USART_PORT, &gpio);
 	gpio.GPIO_Pin = USART_RX_PIN; //RX
 	gpio.GPIO_Mode = GPIO_Mode_IPU;
 	GPIO_Init(USART_PORT, &gpio);

 	USART_StructInit(&usartinit);
 	usartinit.USART_BaudRate = 115200;
 	usartinit.USART_WordLength = USART_WordLength_8b;
 	usartinit.USART_StopBits = USART_StopBits_1;
 	usartinit.USART_Parity = USART_Parity_No;
 	usartinit.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
 	usartinit.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
 	USART_Init(USART_ID, &usartinit);
 	USART_Cmd(USART_ID, ENABLE);
 }


int _write(int fd, char *str, int len)
{
	(void)fd;
	uint32_t i;
	for( i = 0; i < len; i++){
    	while (USART_GetFlagStatus(USART_ID, USART_FLAG_TXE) == RESET);
    	USART_SendData(USART_ID, (uint16_t) (str[i]));
    }
	return 0;
}
