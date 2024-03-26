# Thread MCC Configuration

The configuration of Thread MCC is categorized into two parts: common configuration and<br /> Device Role Specific configuration. The configuration for Device Role selection is<br /> included in the Thread MCC Configuration options. If CLI services are being used, the<br /> authority to select Device Role configuration will be in CLI, and the options for device<br /> role specific configuration will be displayed in the thread configuration options. The<br /> Common configuration options are not are not applicable when the device role selected is<br /> RCP. The below image depicts the thread device role configurations.

<br />

![](GUID-5B53FEE3-89A8-4D7D-A838-A1CA9CAC3718-low.png)

<br />

Thread Code can be generated as source or library and image below depicts the thread<br /> generation configuration.

<br />

![](GUID-6048E87C-8588-4B53-8456-94D828BB260F-low.png)

<br />

**Full Thread Device\(FTD\) MCC Configuration Options:**

The following image illustrates the role of the device as FTD and the available<br /> configuration options for FTD in the Thread Stack configuration options window.

<br />

![](GUID-A75FEB79-E8A0-42A1-BC22-C0B1154BB24F-low.png)

<br />

From the above image FTD configuration details are as follows

**Maximum children**- The maximum number of children supported by the FTD device. The<br /> default number of children supported is 20.

**IP Addr Per Child**- The maximum number of supported IPv6 address registrations<br /> per child. The default value is 4.

**In Band Commissioning** - It is a boolean selection option which is by default<br /> disabled. In Band Commissioning has two sub options if enabled.

-   **Joiner** - Enables Joiner for In Band Commissioning. Default Value is enabled.
-   **Commissioner** – Enables Commissioner for In Band Commissioning. Default Value is Disabled.

    The image<br /> below depicts the In Band Commissioning in FTD configuration and its sub<br /> configuration options.

    ![](GUID-40DAE592-423A-4416-9AE3-E0E67E50180B-low.png)


**Minimal Thread Device\(MTD\) MCC Configuration Options:**

The following image illustrates the role of the device as MTD and the available<br /> configuration options for MTD in the Thread Stack configuration options window.

<br />

![](GUID-A4D37C04-C252-4E87-A0D9-0B342DB8609F-low.png)

<br />

From the above image MTD configuration details are as follows

**Enable Sleep** - Enables Sleep Feature. Sleep Feature is by default disabled and<br /> cannot be enabled when CLI is included \(in use\).

**MLE Child Timeout\(sec\)** - The default MLE child timeout value \(in seconds\). The<br /> default value is 240.

**In Band Commissioning** - It is a boolean selection option which is by default<br /> disabled. In Band Commissioning has one sub options if enabled.

-   **Joiner** - Enables Joiner for In Band Commissioning. Default Value is enabled.

    The image below depicts the In Band<br /> Commissioning in MTD configuration and its sub configuration<br /> options.

    ![](GUID-45397627-D0A0-480C-9EE6-662ACDA59683-low.png)


**Common MCC Configuration Options:**

The following image illustrates the common configuration options for FTD and MTD available<br /> in the Thread Stack configuration window.

<br />

![](GUID-EE08A363-277B-44A4-AE3A-D79A8BD2363C-low.png)

<br />

From the above image common configuration details are as follows

**Enable Thread Log** - It enables the built in logger service from the open thread<br /> implementation which in turn uses drv\_usart for serial output logging. Log Feature is by<br /> default disabled, if enabled the log level selection is OT\_LOG\_LEVEL\_NONE. Users must<br /> change the log level as per the requirement.

<br />

**Note:** The default log level in thread prebuilt Library\(.a\) is set to OT\_LOG\_LEVEL\_DEBUG and dynamic log level control is possible.

<br />

**Enable TCP** - It is a boolean options which enables the TCP service and by default<br /> the option is disabled.

**Coap Block Transfer**- It is a boolean option which enables Coap Block Transfer and<br /> by default the option is disabled.

<br />

**Note:** Coap Block transfer is supported upto 512 bytes of block data only\(block-512\).

<br />

**Radio Co-Processor\(RCP\) MCC Configuration Options:**

The following image illustrates the role of the device as RCP and the available<br /> configuration options for RCP in the Thread Stack configuration options window.

<br />

![](GUID-8A866BAE-9D6B-483C-919E-C715E7E23262-low.png)

<br />

**HDLC Interface** - Interface to communicate with the Host device.

<br />

**Note:** In this current release RCP supports only UART based host interface protocol.

<br />

**Parent topic:**[MCC Component Configuration](GUID-E585B16B-5D65-41F2-B234-6864EA47D41C.md)

