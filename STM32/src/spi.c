#include <spi.h>


void beginTransmission(void)
{
    GYRO_SPI_ASSERT_CS();
}

void endTransmission(void)
{
    while(SPI_I2S_GetFlagStatus(GYRO_SPI, SPI_I2S_FLAG_BSY) == SET);
    GYRO_SPI_DEASSERT_CS(); // End transmission
}

uint8_t transmitByte(uint8_t data)
{
    /* Send byte through the SPI peripheral */
    SPI_I2S_SendData(GYRO_SPI, data);

    /* Wait to receive a byte */
    while (SPI_I2S_GetFlagStatus(GYRO_SPI, SPI_I2S_FLAG_RXNE) == RESET) { ; }

    /* Return the byte read from the SPI bus */
    return SPI_I2S_ReceiveData(GYRO_SPI);
}
