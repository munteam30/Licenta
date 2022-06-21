/*
 * gyro.c
 *
 *  Created on: Aug 20, 2020
 *      Author: Ovidiu
 */


/* Includes */
#include <helper_functions.h>
#include <stddef.h>
#include "stm32f10x.h"
#include "stm32f10x_gpio.h"
#include "gyroAccel.h"

/********** Configurables ********************/


/********** Utilities ********************/

/* low level stuff */
#define GYRO_SPI_ASSERT_CS() GPIO_ResetBits(GYRO_SPI_CS_PORT, GYRO_SPI_CS_BIT);
#define GYRO_SPI_DEASSERT_CS() GPIO_SetBits(GYRO_SPI_CS_PORT, GYRO_SPI_CS_BIT);

void init_gyro(void);
void init_systick(void);

/**
**===========================================================================
**
**  Internal functions
**
**===========================================================================
*/

void init_gyro(void)
{
    /* Using the LSM6DSD33 in SPI mode */
    SPI_InitTypeDef spi_gyro;
    GPIO_InitTypeDef gpio;
    delay_ms(20000); /* allow 20 ms boot period */

    GPIO_StructInit(&gpio);
    gpio.GPIO_Pin = GYRO_SPI_SCK_BIT | GYRO_SPI_MOSI_BIT; // SCK MOSI Pins
    gpio.GPIO_Mode = GPIO_Mode_AF_PP;
    gpio.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GYRO_SPI_MOSI_PORT, &gpio);

    gpio.GPIO_Pin = GYRO_SPI_MISO_BIT; // MISO Pin
    gpio.GPIO_Mode = GPIO_Mode_IN_FLOATING;
    gpio.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GYRO_SPI_MISO_PORT, &gpio);

    gpio.GPIO_Pin = GYRO_SPI_CS_BIT; // CS
    gpio.GPIO_Mode = GPIO_Mode_Out_PP;
    GPIO_Init(GYRO_SPI_CS_PORT, &gpio);

    GYRO_SPI_DEASSERT_CS();

    SPI_StructInit(&spi_gyro);
    spi_gyro.SPI_Direction = SPI_Direction_2Lines_FullDuplex;
    spi_gyro.SPI_Mode = SPI_Mode_Master;
    spi_gyro.SPI_DataSize = SPI_DataSize_8b;
    spi_gyro.SPI_CPOL = SPI_CPOL_High;
    spi_gyro.SPI_CPHA = SPI_CPHA_2Edge;
    spi_gyro.SPI_NSS = SPI_NSS_Soft;
    spi_gyro.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_4;
    spi_gyro.SPI_FirstBit = SPI_FirstBit_MSB;
    SPI_Init(GYRO_SPI, &spi_gyro);
    SPI_Cmd(GYRO_SPI, ENABLE);
}

/**
 * Configure the gyro.
 */
void initGyro(void)
{
    init_systick();
	init_gyro();
    beginTransmission();
    (void)transmitByte(0x18u); // Write CTRL_9_XL
    (void)transmitByte(0x38u); // CTRL_9_XL: enable XYZ accel
    (void)transmitByte(0x38u); // CTRL_10_G: enable XYZ gyro
    endTransmission();


    beginTransmission();
    (void)transmitByte(0x10u); // Write CTRL1_XL
    //(void)transmitByte(0x84u); // CTRL1_XL: Set accel ODR=1.66 kHz, FS_XL = 16g
    //(void)transmitByte(0x7Cu); // CTRL1_XL: Set accel ODR=833 Hz, FS_XL = 8g
    //(void)transmitByte(0xA4u); // CTRL1_XL: Set accel ODR=6.6kHz, FS_XL = 16g
    (void)transmitByte(0x6Cu); // CTRL1_XL: Set accel ODR=416 Hz, FS_XL = 8g

    //(void)transmitByte(0x11u);// Write CTRL2_G
    ////(void)transmitByte(0x8Cu); // CTRL2_G: Set gyro ODR=1.66 kHz, FS_G = 2000 dps
    //(void)transmitByte(0x7Cu); // CTRL2_G: Set gyro ODR=833 Hz, FS_G = 2000 dps
    (void)transmitByte(0x6Cu); // CTRL2_G: Set gyro ODR=416, FS_G = 2000 dps
    (void)transmitByte(0xC4u); // CTRL3_C: Set BOOT = 1, BDU = 1, IF_INC = 1 (keep default)
    endTransmission();

    delay_ms(80000); // 80 ms for sensor to configure itself
}

/**
 * Update the Gyro values
 */
void gyroRead(int16_t readValues[])
{
    beginTransmission();
    transmitByte(0x80u | 0x22u); // Read OUTX_L_G
    readValues[0]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //gyroX
    readValues[1]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //gyroY
    readValues[2]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //gyroZ
    readValues[3]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //accelX
    readValues[4]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //accelY
    readValues[5]  = transmitByte(0x00u) | transmitByte(0x00u) << 8u; //accelZ
    endTransmission();

    readValues[0] = readValues[0] - GYRO_OFFSET_X;
    readValues[1] = readValues[1] - GYRO_OFFSET_Y;
    readValues[2] = readValues[2] - GYRO_OFFSET_Z;

}

