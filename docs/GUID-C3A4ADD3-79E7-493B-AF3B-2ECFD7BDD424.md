# Thread MCC Configuration

The configuration of Thread MCC is categorized into two parts: common configuration and<br /> Device Role Specific configuration. The configuration for Device Role selection is<br /> included in the Thread MCC Configuration options. If CLI services are being used, the<br /> authority to select Device Role configuration will be in CLI, and the options for device<br /> role specific configuration will be displayed in the thread configuration options. The<br /> Common configuration options are not are not applicable when the device role selected is<br /> RCP. The below image depicts the thread device role configurations.

<br />

![](GUID-B7419323-8CAE-4F53-B272-611B77D21788-low.png)

<br />

**Full Thread Device\(FTD\) MCC Configuration Options:**

The following image illustrates the role of the device as FTD and the available<br /> configuration options for FTD in the Thread Stack configuration options window.

<br />

![](GUID-C98C20C6-0916-42A4-98F2-146BB017A5C4-low.png)

<br />

From the above image FTD configuration details are as follows

**Maximum children**- The maximum number of children supported by the FTD device. The<br /> default number of children supported is 10.

**IP Addr Per Child**- The maximum number of supported IPv6 address registrations<br /> per child. The default value is 4.

**In Band Commissioning** - It is a boolean selection option which is by default<br /> disabled. In Band Commissioning has two sub options if enabled.

-   **Joiner** - Enables Joiner for In Band Commissioning. Default Value is enabled.
-   **Commissioner** – Enables Commissioner for In Band Commissioning. Default Value is Disabled.

    The image<br /> below depicts the In Band Commissioning in FTD configuration and its sub<br /> configuration options.

    <br />

    ![](GUID-C06C3599-CAC5-4F9A-B0C0-27ED69FC5E1E-low.png)

    <br />


**Minimal Thread Device\(MTD\) MCC Configuration Options:**

The following image illustrates the role of the device as MTD and the available<br /> configuration options for MTD in the Thread Stack configuration options window.

<br />

![](GUID-656FE0CE-1CE2-47B4-AB2A-9142911E0230-low.png)

<br />

From the above image MTD configuration details are as follows

**Enable Sleep** - Enables Sleep Feature. Sleep Feature is by default disabled and<br /> cannot be enabled when CLI is included \(in use\).

**MLE Child Timeout\(sec\)** - The default MLE child timeout value \(in seconds\). The<br /> default value is 240.

**In Band Commissioning** - It is a boolean selection option which is by default<br /> disabled. In Band Commissioning has one sub options if enabled.

-   **Joiner** - Enables Joiner for In Band Commissioning. Default Value is enabled.

    The image below depicts the In Band<br /> Commissioning in MTD configuration and its sub configuration options.

    <br />

    ![](GUID-E3B81FE2-7AF5-4F74-8A6B-BB9A95966D9C-low.png)

    <br />


**Common MCC Configuration Options:**

The following image illustrates the common configuration options for FTD and MTD available<br /> in the Thread Stack configuration window.

<br />

![](GUID-256D99D8-C4FF-42B7-9205-9B3E3EF8CE18-low.png)

<br />

From the above image common configuration details are as follows

**Enable Thread Log** - It enables the built in logger service from the open thread<br /> implementation which in turn uses drv\_usart for serial output logging. Log Feature is by<br /> default disabled, if enabled the log level selection is OT\_LOG\_LEVEL\_NONE. Users must<br /> change the log level as per the requirement.

<br />

**Note:** In this current release Thread Log support is available only when CLI is enabled.

<br />

**Enable TCP** - It is a boolean options which enables the TCP service and by default<br /> the option is disabled.

**Coap Block Transfer**- It is a boolean option which enables Coap Block Transfer and<br /> by default the option is disabled.

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

