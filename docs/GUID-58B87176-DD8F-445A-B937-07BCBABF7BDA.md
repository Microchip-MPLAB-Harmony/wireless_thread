# Supported Features and Library Configurations:

The following features are supported as part of the current revision.

<br />

-   **Thread Spec Version**: v.1.3.0
-   **Supported Device Roles** –
    -   **FTD**: Leader, Router, FED.
    -   **MTD** : MED, SED.
    -   **RCP** : UART Support
-   Thread v1.3.0 Certified library for FTD and MTD.
-   Thread SDK MCC component - FTD, MTD, RCP.
-   CLI Application as MCC component.
-   **Supported Devices:**
    -   PIC32CX1012BZ25048
    -   PIC32CX1012BZ25032
    -   PIC32CX1012BZ24032
    -   WBZ451
    -   WBZ450
-   Validation Platform : WBZ451 Curiosity Xplained Pro

<br />

Microchip Thread SDK supports both library and source generation of legacy openthread<br /> based on the configuration selected. The following table provides the supported features<br /> in prebuilt libraries provided as part of this SDK.

<br />

|Thread feature|Library Support|
|FTD|MTD|
|--------------|---------------|
|---|---|
|COMMISSIONER|Yes|N/A|
|JOINER|Yes|Yes|
|DNS\_CLIENT|Yes|Yes|
|DHCP6\_SERVER|No|No|
|DHCP6\_CLIENT|Yes|Yes|
|COAP|Yes|Yes|
|COAPS|Yes|Yes|
|DIAGNOSTIC|No|No|
|LINK\_RAW|No|No|
|MAC\_FILTER|No|No|
|TMF NETDATA|Yes|Yes|
|SRP CLIENT|Yes|Yes|
|LOG LEVEL|Yes|Yes|
|DYNAMIC LOG LEVEL|Yes|Yes|
|TCP|Yes|Yes|
|LINK METRICS|Yes|No|
|DUA|Yes|Yes|
|MLR|Yes|Yes|
|UDP\_FORWARD|No|No|
|ECDSA|Yes|Yes|
|CSL RECEIVER|No|Yes|
|SNTP\_CLIENT|No|No|
|CHILD\_SUPERVISION|Yes|Yes|
|JAM\_DETECTION|No|No|
|BORDER\_AGENT|No|No|
|BORDER\_ROUTER|No|No|

<br />

The following table provides the details of configured settings provided with prebuilt<br /> libraries.

<br />

|Thread Configuration|Library Support|
|FTD|MTD|
|--------------------|---------------|
|---|---|
|COAP MAX BLOCK LENGTH|512|512|
|MESSAGE BUFFERS|64|44|
|LOG LEVEL|5|5|
|MLE MAX CHILDREN|20|N/A|
|MLE IP ADDR PER CHILD|4|N/A|
|MLE CHILD TIMEOUT|N/A|240|
|MAC ATTACH POLL PERIOD|N/A|500|

<br />

