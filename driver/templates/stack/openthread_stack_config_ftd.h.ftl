/*
 *  Copyright (c) 2024, The OpenThread Authors.
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


/*******************************************************************************
* Copyright (C) [2024], Microchip Technology Inc., and its subsidiaries. All rights reserved.
  
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


#ifndef _STACKCONFIG_H    /* Guard against multiple inclusion */
#define _STACKCONFIG_H


/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Included Files                                                    */
/* ************************************************************************** */
/* ************************************************************************** */

/* This section lists the other files that are included in this file.
 */

/* TODO:  Include other files here if needed. */


/* Provide C++ Compatibility */
#ifdef __cplusplus
extern "C" {
#endif


/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Constants                                                         */
/* ************************************************************************** */
/* ************************************************************************** */

/*  A brief description of a section can be given directly below the section
    banner.
 */


/* ************************************************************************** */
/** Descriptive Constant Name

  @Summary
    Brief one-line summary of the constant.

  @Description
    Full description, explaining the purpose and usage of the constant.
    <p>
    Additional description in consecutive paragraphs separated by HTML 
    paragraph breaks, as necessary.
    <p>
    Type "JavaDoc" in the "How Do I?" IDE toolbar for more information on tags.

  @Remarks
    Any additional remarks
 */
 
//#define OT_PLATFORM                                                  (external)
#define PACKAGE_NAME                                                 "OPENTHREAD"
#define PACKAGE_VERSION                                              "thread-reference-20230706"

#define OPENTHREAD_CONFIG_FILE                                       "openthread-core-pic32cx-config.h"
#define OPENTHREAD_CORE_CONFIG_PLATFORM_CHECK_FILE                   "openthread-core-pic32cx-config-check.h"
#define OPENTHREAD_PROJECT_CORE_CONFIG_FILE                          "openthread-core-pic32cx-config.h"
#define MBEDTLS_CONFIG_FILE                                          "openthread-mbedtls-config.h"
#define MBEDTLS_USER_CONFIG_FILE                                     "pic32cx-mbedtls-config.h"

#define NDEBUG
#define OPENTHREAD_CONFIG_ASSERT_ENABLE                              (1)
#define OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS                     (1)
#define OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS_MANAGEMENT          (1)
#define OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE                           (1)
#define OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE                   (0)
#define OPENTHREAD_CONFIG_PING_SENDER_ENABLE                         (1)
#define OPENTHREAD_CONFIG_THREAD_VERSION                             (OT_THREAD_VERSION_1_3)
#define OPENTHREAD_CONFIG_COAP_API_ENABLE                            (1)
#define OPENTHREAD_CONFIG_COAP_BLOCKWISE_TRANSFER_ENABLE             (1)
#define OPENTHREAD_CONFIG_COAP_MAX_BLOCK_LENGTH                      (512)
#define OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE                     (1)
#define OPENTHREAD_CONFIG_MAC_DEFAULT_MAX_FRAME_RETRIES_INDIRECT     (1)
#define OPENTHREAD_CONFIG_MLE_STEERING_DATA_SET_OOB_ENABLE           (1)
#define OPENTHREAD_CONFIG_ECDSA_ENABLE                               (1)
#define OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE                    (1)
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_SECURITY_ENABLE            (1) 
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_TIMING_ENABLE              (1)
#define OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE                          (1)
#define OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE                 (1)
<#if OPEN_THREAD_DEVICE_ROLE == "FTD" || OPEN_THREAD_DEVICE_ROLE == "MTD">
<#if OPEN_THREAD_UART_PARSER == true>
#define OPENTHREAD_CONFIG_CLI_UART_TX_BUFFER_SIZE                    (2048)
</#if>
</#if>


#define OPENTHREAD_FTD                                               (1)
#define OPENTHREAD_CONFIG_LOG_MAX_SIZE                               (512)
#define OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE                   (1)
<#if (OPEN_THREAD_UART_PARSER == true) && (OPEN_THREAD_LOG_SYMBOL == true)>
#define OPENTHREAD_CONFIG_LOG_OUTPUT                                 (OPENTHREAD_CONFIG_LOG_OUTPUT_APP)
<#elseif OPEN_THREAD_LOG_SYMBOL == true>
#define OPEN_THREAD_LOG_ENABLED                                      (1)
</#if>
<#if OPEN_THREAD_LIBRARY_GENERATION == "Library">
#define OPENTHREAD_CONFIG_JOINER_ENABLE                              (1)
#define OPENTHREAD_CONFIG_COMMISSIONER_ENABLE                        (1)
#define OPENTHREAD_CONFIG_TCP_ENABLE                                 (1)
#define SYS_PDS_NUM_MAX_CHILDREN_ENTRY                               (20)
#define OPENTHREAD_CONFIG_MLE_IP_ADDRS_PER_CHILD                     (4)
#define OPENTHREAD_CONFIG_NUM_MESSAGE_BUFFERS                        (64)
<#else>
<#if OPEN_THREAD_LOG_SYMBOL == true>
#define OPENTHREAD_CONFIG_LOG_LEVEL                                  (${OPEN_THREAD_LOG_LEVEL_CONFIG})
</#if>
<#if OPEN_THREAD_FTD_IN_BAND_COMMISSIONING_CONFIG == true>
<#if OPEN_THREAD_FTD_JOINER_ENABLE == true>
#define OPENTHREAD_CONFIG_JOINER_ENABLE                              (1)
<#else>
#define OPENTHREAD_CONFIG_JOINER_ENABLE                              (0)
</#if>
<#if OPEN_THREAD_FTD_COMMISSIONER_ENABLE == true>
#define OPENTHREAD_CONFIG_COMMISSIONER_ENABLE                        (1)
<#else>
#define OPENTHREAD_CONFIG_COMMISSIONER_ENABLE                        (0)
</#if>
</#if>
<#if OPEN_THREAD_TCP_ENABLE_CONFIG??>
<#if OPEN_THREAD_TCP_ENABLE_CONFIG == true>
#define OPENTHREAD_CONFIG_TCP_ENABLE                                 (1)
</#if>
</#if>
#define OPENTHREAD_CONFIG_MLE_MAX_CHILDREN                           (${OPEN_THREAD_FTD_MLE_MAX_CHILD_CONFIG})
#define SYS_PDS_NUM_MAX_CHILDREN_ENTRY                               (${OPEN_THREAD_FTD_MLE_MAX_CHILD_CONFIG})
#define OPENTHREAD_CONFIG_MLE_IP_ADDRS_PER_CHILD                     (${OPEN_THREAD_MLE_IP_ADDR_PER_CHILD})
#define OPENTHREAD_CONFIG_NUM_MESSAGE_BUFFERS                        (64)
</#if>

<#if OPEN_THREAD_UART_SERVICE == true>
#define OPEN_THREAD_UART_ENABLE                                      (1)
</#if>
#define OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE            (1)

#define OPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE                       (1)              
#define OPENTHREAD_CONFIG_DUA_ENABLE                                (1) 
#define OPENTHREAD_CONFIG_MLR_ENABLE                                (1)
#define OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE                         (1)





    
    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _STACKCONFIG_H */

/* *****************************************************************************
 End of File
 */
