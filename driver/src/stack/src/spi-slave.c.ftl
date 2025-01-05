/*
 *  Copyright (c) 2025, The OpenThread Authors.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. Neither the name of the copyright holder nor the
 *     names of its contributors may be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 *  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 *  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 *  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 *  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 *  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 *  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 *  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * @file
 *   This file implements the OpenThread platform abstraction for SPI slave communication.
 *
 */


/*******************************************************************************
* Copyright (C) [2025], Microchip Technology Inc., and its subsidiaries. All rights reserved.
  
* The software and documentation is provided by Microchip and its contributors 
* "as is" and any express, implied or statutory warranties, including, but not 
* limited to, the implied warranties of merchantability, fitness for a particular 
* purpose and non-infringement of third party intellectual property rights are 
* disclaimed to the fullest extent permitted by law. In no event shall Microchip 
* or its contributors be liable for any direct, indirect, incidental, special,
* exemplary, or consequential damages (including, but not limited to, procurement 
* of substitute goods or services; loss of use, data, or profits; or business 
* interruption) however caused and on any theory of liability, whether in contract, 
* strict liability, or tort (including negligence or otherwise) arising in any way 
* out of the use of the software and documentation, even if advised of the 
* possibility of such damage.
* 
* Except as expressly permitted hereunder and subject to the applicable license terms 
* for any third-party software incorporated in the software and any applicable open 
* source software license terms, no license or other rights, whether express or 
* implied, are granted under any patent or other intellectual property rights of 
* Microchip or any third party.
 *******************************************************************************/


#include <definitions.h>
#include "platform-pic32cx.h"
#include <openthread-system.h>
#include <common/code_utils.hpp>
#include <utils/code_utils.h>
#include <openthread/platform/spi-slave.h>
#include <string.h>

#if OPENTHREAD_CONFIG_NCP_SPI_ENABLE

typedef enum
{
    SPI_TRANSACTION_DONE,
    SPI_TRANSACTION_IN_PROGRESS,
} otSpiSlaveTransactionState;

#define SPI_SLAVE_TX_BUFFER_LEN    256U
#define SPI_SMALL_PACKET_LEN       164U


extern OSAL_QUEUE_HANDLE_TYPE OTQueue;

static void  *sContext = NULL;
static uint8_t *sOutputBuf = NULL;
static uint16_t sOutputBufLen = 0;
static uint8_t  *sInputBuf = NULL;
static uint16_t  sInputBufLen  = 0;
otPlatSpiSlaveTransactionCompleteCallback sCompleteCallback = NULL;
otPlatSpiSlaveTransactionProcessCallback  sProcessCallback  = NULL;

static uint8_t spiTxDummyBuffer[SPI_SLAVE_TX_BUFFER_LEN];
static uint8_t TxBuffEmptyWithDataLen[10];
static uint8_t spiTxBuffer[SPI_SLAVE_TX_BUFFER_LEN];
static uint16_t receivedBytes = 0;
static volatile bool transactionRequested = false;
static otSpiSlaveTransactionState transactionState = SPI_TRANSACTION_DONE;
static volatile uint32_t nbReqDuringSpiTrans = 0;

static void CheckSpiSlaveTransactionStatus(void);

static void otSpiSlaveCallback(uintptr_t contextHandle)
{
    
}

void otSpiSlaveSSCallback (GPIO_PIN pin, uintptr_t context)
{
    bool PinState = GPIO_PinRead(pin);
   
    
    if(PinState && transactionState!= SPI_TRANSACTION_DONE )
    {
        transactionState = SPI_TRANSACTION_DONE;
        memcpy(spiTxDummyBuffer, spiTxBuffer, sOutputBufLen + 1);
        receivedBytes = ${OPEN_THREAD_RCP_SPI_INST}_SPI_ReadCountGet();
        if(sInputBuf != NULL)
        {
            ${OPEN_THREAD_RCP_SPI_INST}_SPI_Read(sInputBuf, receivedBytes );
        }    
        
        CheckSpiSlaveTransactionStatus();

    }
    
    else
    {       
        transactionState = SPI_TRANSACTION_IN_PROGRESS;
      
        ${OPEN_THREAD_RCP_SPI_INST}_SPI_Write(spiTxDummyBuffer, sizeof(spiTxDummyBuffer));

    }
}

static void CheckSpiSlaveTransactionStatus(void)
{
    OT_Msg_T otUARTMsg; 
    
    if(sInputBuf == NULL || sOutputBuf == NULL)
    {
        sOutputBufLen = 0;
        sInputBufLen = 0;
    }

    if (sCompleteCallback(sContext, sOutputBuf, sOutputBufLen, sInputBuf, sInputBufLen, receivedBytes > sOutputBufLen ? receivedBytes : sOutputBufLen ))
    {
       otUARTMsg.OTMsgId = OT_MSG_SPI_SLAVE_PROCESS;
       OSAL_QUEUE_Send(&OTQueue, &otUARTMsg,0);

    }

}

void pic32cxSpiInit(void)
{
    size_t SpiTxDummyDataIdx;

    for (SpiTxDummyDataIdx = 0; SpiTxDummyDataIdx < sizeof(spiTxDummyBuffer); SpiTxDummyDataIdx++)
    {
        spiTxDummyBuffer[SpiTxDummyDataIdx] = 0xFF;
        spiTxBuffer[SpiTxDummyDataIdx] = 0xFf;
    }
    
}

void pic32cxSpiSlaveProcess(OT_MsgId_T otUartMsgId)
{    
    if (OT_MSG_SPI_SLAVE_PROCESS == otUartMsgId)
    {
        sProcessCallback(sContext);
    }
}

void otPlatSpiSlaveDisable(void)
{
    sCompleteCallback = NULL;
    sProcessCallback  = NULL;
    sContext          = NULL;
}

otError otPlatSpiSlaveEnable(otPlatSpiSlaveTransactionCompleteCallback aCompleteCallback,
                             otPlatSpiSlaveTransactionProcessCallback  aProcessCallback,
                             void                                     *aContext)
{   
   
    /*
     * SPI properties (based on openthread SPI recommendations):
     * CS is active low.
     * CLK is active high.
     * Data is valid on leading edge of CLK.
     * Data is sent in multiples of 8-bits (bytes).
     * Bytes are sent most-significant bit first.
     */
    
    otError result = OT_ERROR_NONE;
    
    if(aCompleteCallback != NULL && aProcessCallback != NULL)
    {
        // Check if SPI Slave interface is already enabled.
        otEXPECT_ACTION(sCompleteCallback == NULL, result = OT_ERROR_ALREADY);
        
        ${OPEN_THREAD_RCP_SPI_INST}_SPI_CallbackRegister(otSpiSlaveCallback,(uintptr_t)0);
        GPIO_PinInterruptCallbackRegister(SPI_SS_PIN, otSpiSlaveSSCallback, (uintptr_t)0 );
        GPIO_PinIntEnable(SPI_SS_PIN, GPIO_INTERRUPT_ON_BOTH_EDGES);


        sCompleteCallback = aCompleteCallback;
        sProcessCallback  = aProcessCallback;
        sContext          = aContext;
        return result;
    }

exit:
    return result;
}

otError otPlatSpiSlavePrepareTransaction(uint8_t *aOutputBuf,
                                         uint16_t aOutputBufLen,
                                         uint8_t *aInputBuf,
                                         uint16_t aInputBufLen,
                                         bool     aRequestTransactionFlag)
{
    otError result = OT_ERROR_NONE;
    static bool isRequestFrameSent = true;
       
    if(sCompleteCallback != NULL)
    {
        otEXPECT_ACTION(transactionState !=SPI_TRANSACTION_IN_PROGRESS , result=OT_ERROR_BUSY);

        if (transactionState == SPI_TRANSACTION_DONE)
        {
            if (aInputBuf != NULL)
            {
                sInputBuf    = aInputBuf;
                sInputBufLen = aInputBufLen;
            }

            if(aOutputBuf != NULL)
            {
                sOutputBuf    = aOutputBuf;  
                sOutputBufLen = aOutputBufLen;
                
                uint16_t txDataLen = aOutputBuf[4] << 8 | aOutputBuf[3];         
            
				if (txDataLen > SPI_SMALL_PACKET_LEN && isRequestFrameSent)                    
				{
					for (int i = 0; i < 10; i++)
					{
						if (i < 5)
							TxBuffEmptyWithDataLen[i] = aOutputBuf[i];
						else
							TxBuffEmptyWithDataLen[i] = 0xFF;
									
					}
					memcpy(spiTxDummyBuffer, TxBuffEmptyWithDataLen, 10);
	   
					isRequestFrameSent = false;

				}
				else
					{
						memcpy(spiTxDummyBuffer, sOutputBuf, sOutputBufLen);
						isRequestFrameSent = true;
					}
				}

            if(aRequestTransactionFlag)
            {
                ${OPEN_THREAD_RCP_SPI_INST}_SPI_Ready();
            }
  
        }     
        
    }

 exit:
    if (result == OT_ERROR_BUSY)
    {      
        nbReqDuringSpiTrans++;
    }
    return result;
}

#endif  //OPENTHREAD_CONFIG_NCP_SPI_ENABLE



