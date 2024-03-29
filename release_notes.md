﻿![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Wireless Thread Release Notes

## Release v1.0.1

### Bug fixes

- Fix of dependency version string in package.yml

________________________________

## Release v1.0.0

Harmony Wireless Thread package uses the [openthread](https://github.com/Microchip-MPLAB-Harmony/openthread/releases/tag/mchp_harmony_wireless_thread_v1.0.0) which is available as part of Microchip MPLAB Harmony, to provide Thread support, and OpenThread released by Google is an open-source implementation of [Thread®](https://www.threadgroup.org/). 
The Harmony Wireless Thread package offers support through MPLAB Code Configurator(MCC) component, a user-friendly GUI tool that simplifies configuration and generates code based on the selected Thread
configuration. The purpose of this package is to provide support for system-on-chip (SOC) and radio co-processor (RCP) designs.
The following features are supported as part of the current revision.

-  Thread Spec Version : v.1.3.0
-  Supported Device Roles:
    - FTD : Leader, Router, FED.
    - MTD : MED, SED.
    - RCP : UART Support
-  Thread v1.3.0 Pre-Certification
-  Thread SDK MCC component: FTD, MTD, RCP.
-  CLI Application as MCC component.
-  Bootloader Supported.
-  TCP supported.
-  Supported Devices:
    - PIC32CX1012BZ25048
    - PIC32CX1012BZ25032
    - PIC32CX1012BZ24032
    - WBZ451
    - WBZ450


## Known Issues / Limitations

-   SSED Support not available
-   Thread Log support available only with CLI App.
-   Free RTOS heap requires 45k when bootloader services are included.
-   Two Mandatory MISRA C Deviations are observed.

## Development Tools
-   MPLAB X v6.15
-   MPLAB® XC32 C/C++ Compiler v4.21
-   MPLAB® X IDE plug-ins: MPLAB® Code Configurator (MCC) v5.3.7 and above
-   Device Pack: PIC32CX-BZ2-DFP (1.2.230)

## Notes
-   [Thread®](https://www.threadgroup.org/) is registered Trademark of Thread Group.
-   The Microchip name and logo, the Microchip logo, (all others named in the document) are registered trademarks of Microchip Technology Incorporated in the U.S.A. and other countries. All other trademarks are the property of their respective companies.
