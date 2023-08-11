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
#define PACKAGE_VERSION                                              "0.1.0"

#define OPENTHREAD_CONFIG_FILE                                       "openthread-core-pic32cx-config.h"
#define OPENTHREAD_CORE_CONFIG_PLATFORM_CHECK_FILE                   "openthread-core-pic32cx-config-check.h"
#define OPENTHREAD_PROJECT_CORE_CONFIG_FILE                          "openthread-core-pic32cx-config.h"
#define MBEDTLS_CONFIG_FILE                                          "openthread-mbedtls-config.h"
#define MBEDTLS_USER_CONFIG_FILE                                     "pic32cx-mbedtls-config.h"

#define NDEBUG
#define OPENTHREAD_CONFIG_ASSERT_ENABLE                              (1)
#define OPEN_THREAD_UART_ENABLE										 (1)
#define OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS                     (1)
#define OPENTHREAD_CONFIG_ENABLE_BUILTIN_MBEDTLS_MANAGEMENT          (1)
#define OPENTHREAD_CONFIG_NCP_HDLC_ENABLE                            (1)
#define OPENTHREAD_CONFIG_THREAD_VERSION                             (OT_THREAD_VERSION_1_3)
#define OPENTHREAD_SPINEL_CONFIG_OPENTHREAD_MESSAGE_ENABLE           (0)
#define OPENTHREAD_SPINEL_CONFIG_RCP_RESTORATION_MAX_COUNT           (0)
#define OPENTHREAD_ENABLE_NCP_VENDOR_HOOK                            (0)
#define OPENTHREAD_RADIO                                             (1) 
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_SECURITY_ENABLE            (1) 
#define OPENTHREAD_CONFIG_LINK_RAW_ENABLE							 (1)
#define OPENTHREAD_CONFIG_MAC_SOFTWARE_TX_TIMING_ENABLE              (1)

/* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif /* _STACKCONFIG_H */

/* *****************************************************************************
 End of File
 */
