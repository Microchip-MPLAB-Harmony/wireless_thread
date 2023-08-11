/*******************************************************************************
 System Tasks File

  File Name:
    tasks.c

  Summary:
    This file contains source code necessary to maintain system's polled tasks.

  Description:
    This file contains source code necessary to maintain system's polled tasks.
    It implements the "SYS_Tasks" function that calls the individual "Tasks"
    functions for all polled MPLAB Harmony modules in the system.

  Remarks:
    This file requires access to the systemObjects global data structure that
    contains the object handles to all MPLAB Harmony module objects executing
    polled in the system.  These handles are passed into the individual module
    "Tasks" functions to identify the instance of the module to maintain.
 *******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "configuration.h"
#include "definitions.h"
#include "platform-pic32cx.h"

#include <assert.h>
#include <openthread-core-config.h>
#include <openthread/config.h>

#include "openthread-system.h"
#include <openthread/diag.h>
#include <openthread/tasklet.h>
#include <openthread/platform/logging.h>

// *****************************************************************************
// *****************************************************************************
// Section: RTOS "Tasks" Routine
// *****************************************************************************
// *****************************************************************************

void taskOpenThread(void *pvParam);

TaskHandle_t taskHandleOpenThread;

extern OSAL_QUEUE_HANDLE_TYPE OTQueue;

otInstance *instance;

<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
static QueueSetHandle_t xQueueSet;
static QueueSetMemberHandle_t xActivatedMember;
extern OSAL_SEM_HANDLE_TYPE semPhyInternalHandler;
</#if>

<#if OPEN_THREAD_UART_SERVICE>
<#if OPEN_THREAD_UART_PARSER == true && ((OPEN_THREAD_DEVICE_ROLE == "FTD") || (OPEN_THREAD_DEVICE_ROLE == "MTD" ))>
extern void otAppCliInit(otInstance *aInstance);
</#if>
<#if OPEN_THREAD_UART_PARSER == false && (OPEN_THREAD_DEVICE_ROLE == "RCP")>
extern void otAppNcpInit(otInstance *aInstance);
</#if>
</#if>


void otTaskletsSignalPending(otInstance *aInstance)
{
    OT_UNUSED_VARIABLE(aInstance);

    OT_Msg_T otTaskletMsg;
    otTaskletMsg.OTMsgId = OT_MSG_TASKLET_PROCESS_PENDING;
    OSAL_QUEUE_Send(&OTQueue, &otTaskletMsg,0);
}


void taskOpenThread(void *pvParam)
{
    OT_Msg_T   otMessage;
	instance = (otInstance *) pvParam;
	
	<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
	/* Create the queue set large enough to hold an event for every space in
    every queue and semaphore that is to be added to the set. */
    OSAL_QUEUE_CreateSet(&xQueueSet, 20 + 20);
    /* Add the queues and semaphores to the set.  Reading from these queues and
       semaphore can only be performed after a call to xQueueSelectFromSet() has
       returned the queue or semaphore handle from this point on. */
    OSAL_QUEUE_AddToSet( &OTQueue, &xQueueSet );
    OSAL_QUEUE_AddToSet( &semPhyInternalHandler, &xQueueSet );
	</#if>
	
pseudo_reset:   

    instance = otInstanceInitSingle();
	assert(instance);

<#if OPEN_THREAD_DEVICE_ROLE == "FTD" || OPEN_THREAD_DEVICE_ROLE == "MTD">
<#if OPEN_THREAD_UART_PARSER == true>
	otAppCliInit(instance);
</#if>
</#if>	
<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
<#if OPEN_THREAD_UART_PARSER == false>
	otAppNcpInit(instance); 
</#if>
</#if>  
    
    while (true)
    {
        while (!otSysPseudoResetWasRequested())
        {
             /* Block to wait for something to be available from the queues or
              semaphore that have been added to the set.*/
			<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
            OSAL_QUEUE_SelectFromSet(&xActivatedMember, &xQueueSet, OSAL_WAIT_FOREVER );
            if( xActivatedMember == semPhyInternalHandler )
            {
                /*Process Internal Stack Events*/
                OSAL_SEM_Pend(&semPhyInternalHandler, 0);
                PHY_TaskHandler();
            }
            else if(xActivatedMember == OTQueue )
            {
			</#if>
				<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
				OSAL_QUEUE_Receive(&OTQueue, &otMessage, 0);
				<#else>
				OSAL_QUEUE_Receive(&OTQueue, &otMessage, OSAL_WAIT_FOREVER);
				</#if>
                switch (otMessage.OTMsgId & PLAT_MODULE_ID_MASK)
                {
					<#if OPEN_THREAD_UART_SERVICE == true>
					case PLAT_UART_MODULE_ID:
                    {
                        pic32cxUartProcess(otMessage.OTMsgId);
                        break;
                    }
					</#if>
                    case PLAT_RADIO_MODULE_ID:
                    {
                        pic32cxRadioProcess(instance, otMessage.OTMsgId);
                        break;
                    }
                    case PLAT_ALARM_MODULE_ID:
                    {
                        pic32cxAlarmProcess(instance, otMessage.OTMsgId);
                        break;
                    }
                    case OT_TASKLET_PROCESS_ID:
                    {
                        otTaskletsProcess(instance);
                        break;
                    }
                    default:
                        break;
                }
			<#if OPEN_THREAD_DEVICE_ROLE == "RCP">
			}
			</#if>

        }
        
        otInstanceFinalize(instance);
    }
    goto pseudo_reset;
}


/*******************************************************************************
 End of File
 */