/* ************************************************************************** */
/** Descriptive File Name

  @Company
    Company Name

  @File Name
    filename.h

  @Summary
    Brief description of the file.

  @Description
    Describe the purpose of this file.
 */
/* ************************************************************************** */

#ifndef _PREINCLUDE_H    /* Guard against multiple inclusion */
#define _PREINCLUDE_H


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
#define PACKAGE_VERSION                                              "0.1.0"

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
#define OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE                     (1)
#define OPENTHREAD_CONFIG_MAC_DEFAULT_MAX_FRAME_RETRIES_INDIRECT     (1)
#define OPENTHREAD_CONFIG_MLE_STEERING_DATA_SET_OOB_ENABLE           (1)
#define OPENTHREAD_CONFIG_ECDSA_ENABLE                               (1)
#define OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE                    (1)
#define OPENTHREAD_CONFIG_MAC_ATTACH_DATA_POLL_PERIOD                500
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_SECURITY_ENABLE            (1) 
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_TIMING_ENABLE              (1)
<#if OPEN_THREAD_COAP_BLOCK_TRANSFER_ENABLE == true>
#define OPENTHREAD_CONFIG_MESSAGE_BUFFER_SIZE                        (sizeof(void *) * 64)
</#if>
<#if OPEN_THREAD_DEVICE_ROLE == "FTD" || OPEN_THREAD_DEVICE_ROLE == "MTD">
<#if OPEN_THREAD_UART_PARSER == true>
#define OPENTHREAD_CONFIG_CLI_UART_TX_BUFFER_SIZE                    (2048)
#define OPENTHREAD_CONFIG_CLI_UART_RX_BUFFER_SIZE                    (512)
</#if>
</#if>


#define OPENTHREAD_MTD												 (1)
<#if OPEN_THREAD_LOG_SYMBOL == true>
#define OPENTHREAD_CONFIG_LOG_LEVEL                                  (${OPEN_THREAD_LOG_LEVEL_CONFIG})
</#if>
<#if (OPEN_THREAD_UART_PARSER == true) && (OPEN_THREAD_LOG_SYMBOL == true)>
#define OPENTHREAD_CONFIG_LOG_OUTPUT 								 (OPENTHREAD_CONFIG_LOG_OUTPUT_APP)
</#if>
<#if OPEN_THREAD_UART_SERVICE == true>
#define OPEN_THREAD_UART_ENABLE										 (1)
</#if>
<#if OPEN_THREAD_MTD_MLE_CHILD_TIMEOUT??>
#define OPENTHREAD_CONFIG_MLE_CHILD_TIMEOUT_DEFAULT 				 (${OPEN_THREAD_MTD_MLE_CHILD_TIMEOUT})
</#if>
<#if OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG == true>
<#if OPEN_THREAD_MTD_JOINER_ENABLE == true>
#define OPENTHREAD_CONFIG_JOINER_ENABLE                              (1)
<#else>
#define OPENTHREAD_CONFIG_JOINER_ENABLE                              (0)
</#if>
</#if>
<#if OPEN_THREAD_TCP_ENABLE_CONFIG??>
<#if OPEN_THREAD_TCP_ENABLE_CONFIG == true>
#define OPENTHREAD_CONFIG_TCP_ENABLE								 (1)
</#if>
</#if>



    /* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _PREINCLUDE_H */

/* *****************************************************************************
 End of File
 */
