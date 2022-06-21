#ifndef SPI_H_
#define SPI_H_


#include "stm32f10x_spi.h"
#include "stm32f10x.h"

#define GYRO_SPI SPI2

#define GYRO_SPI_MOSI_BIT   GPIO_Pin_15
#define GYRO_SPI_MOSI_PORT  GPIOB

#define GYRO_SPI_MISO_BIT   GPIO_Pin_14
#define GYRO_SPI_MISO_PORT  GPIOB

#define GYRO_SPI_SCK_BIT    GPIO_Pin_13
#define GYRO_SPI_SCK_PORT   GPIOB

#define GYRO_SPI_CS_BIT     GPIO_Pin_12
#define GYRO_SPI_CS_PORT    GPIOB

#define GYRO_SPI_ASSERT_CS() GPIO_ResetBits(GYRO_SPI_CS_PORT, GYRO_SPI_CS_BIT);
#define GYRO_SPI_DEASSERT_CS() GPIO_SetBits(GYRO_SPI_CS_PORT, GYRO_SPI_CS_BIT);

void beginTransmission(void);
void endTransmission(void);
uint8_t transmitByte(uint8_t data);

#endif
