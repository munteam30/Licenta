/*
 * gyro.h
 *
 */

#ifndef GYRO_ACCEL_H_
#define GYRO_ACCEL_H_

#include "helper_functions.h"


#define GYRO_SPI SPI2

#define GYRO_SPI_MOSI_BIT   GPIO_Pin_15
#define GYRO_SPI_MOSI_PORT  GPIOB

#define GYRO_SPI_MISO_BIT   GPIO_Pin_14
#define GYRO_SPI_MISO_PORT  GPIOB

#define GYRO_SPI_SCK_BIT    GPIO_Pin_13
#define GYRO_SPI_SCK_PORT   GPIOB

#define GYRO_SPI_CS_BIT     GPIO_Pin_12
#define GYRO_SPI_CS_PORT    GPIOB

#define GYRO_OFFSET_X (0)
#define GYRO_OFFSET_Y (0)
#define GYRO_OFFSET_Z (0)

/* gyro initialization and comm */
extern volatile uint32_t global_timer;
void Timebase_Delay_ms(uint32_t delay);
void init_systick(void);
void initGyro(void);
void gyroRead(int16_t *readValues);


#endif /* GYRO_H_ */
