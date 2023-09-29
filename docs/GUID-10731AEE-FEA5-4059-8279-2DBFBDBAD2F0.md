# Creating a new MCC Harmony Project

This section briefs about the project generation, MCC configuration using CLI, Thread<br /> component and details about the default project configuration considered for thread<br /> SDK.

<br />

**Note:** The below steps are common and necessary for both FTD and MTD projects.

<br />

1.  Create MCC Project for any one of PIC32CXBZ2 devices \(WBZ450 /WBZ451 /PIC32CX1012BZ25048 /PIC32CX1012BZ24032\)
2.  OpenMCC Window. By default, the MCC window will appear as follows.

    <br />

    ![](GUID-B3A0ACA4-813C-4446-93A4-5BC79D5934F9-low.png)

    <br />

3.  OnceProject graph is getting displayed for the created project, Double click on the **CLI** component.

    <br />

    **Note:** CLI and Thread Stack components will appear in Device Resources only ifwireless\_thread is cloned in MCC framework path.

    <br />

    ![](GUID-5269341D-B653-4B34-8374-5F52C82DCF67-low.png)

    <br />

    <br />

4.  Upon selecting the component, the MCC will auto activate the Thread stack as<br /> dependent module. Thread stack and other inter dependent component dependencies<br /> will be auto activated and shows Popup for getting the approval. Select “Yes�?<br /> for all of them.

    <br />

    ![](GUID-96CAED19-2EA1-49F4-881E-5D90217CB293-low.png)

    <br />

5.  CLI will auto activate the Thread USART capability as part of its functional usage. Then PHY component dependencies auto activation will be triggered.

    <br />

    ![](GUID-AA3532C3-EC13-468A-8B8A-11D865600459-low.png)

    <br />

    Below are the list of PHY Component Dependencies.

    1.  DeviceSupport Library
    2.  Core
    3.  TRNG
    4.  SYSTEM Time Module \(PHYUses one client of SYS\_TIME\_MODULE\) – So, the number of SYS\_TIME\_CLIENT should be more than 1.
6.  IEEE802.15.4 PHY doesn't processes request through a seperate Free RTOS task and below is the IEEE 802.15.4 PHY configurtaion for Microchip Thread SDK.

    <br />

    ![](GUID-F01F541A-42CB-4D2F-AF5D-7A6CFD7FDF14-low.png)

    <br />

7.  Below is the Device support library configuration considered for the Microchip Thread SDK.

    <br />

    ![](GUID-D40BBAF5-8A90-42C2-826E-8C810D07C999-low.png)

    <br />

8.  The project graph will look like

    <br />

    ![](GUID-2C3DDC47-AE46-4878-BB8D-0DC19853C8F3-low.png)

    <br />

9.  RightClick on TIME module for selecting the timer source, Select any of the timer.

    <br />

    ![](GUID-941AD636-B92C-495C-8F49-986268114548-low.png)

    <br />

10. Below is the TC0 configuration considered for the Microchip Thread SDK.

    <br />

    ![](GUID-73BF67DB-CA06-413F-931F-BFBC9250CC19-low.png)

    <br />

11. Choose the Thread role under CLI configuration options as shown below.

    Select the Device Role as FTD for CLI+Thread<br /> FTD project.

    <br />

    ![](GUID-9B0BDC16-4644-4A84-83C3-3616B6CE0714-low.png)

    <br />

    Select the Device Role as MTD for CLI+Thread MTD project.

    <br />

    ![](GUID-73B18DD9-041B-40A9-9F6A-7879F8D96BC2-low.png)

    <br />

12. Right click onUSART Driver =\> Go to Satisfiers =\> Click on SERCOM0\(sercom0\)

    <br />

    ![](GUID-02468DFF-E7FB-4668-B1EE-B905E726CBB2-low.png)

    <br />

13. Click on SERCOM 0 =\> Go to configuration options =\> Change Receive pinout, Transmitpinout.

    <br />

    ![](GUID-4E1A4329-F2E6-4A71-9DCB-361C7A444E8B-low.png)

    <br />

14. Configure the SERCOM0 system setting to enable the Direct High Speed inside system Configuration options → Generate Fues → DEVCFG1.

    <br />

    ![](GUID-3FBB6754-AB59-47AA-B970-549E1CF4168E-low.png)

    <br />

15. Click on Generate Tab for Code generation. Upon code generation, Thread files will be added to the project.

    <br />

    ![](GUID-92241D85-4C18-464F-B5FC-D3436E78BE6E-low.png)

    <br />

16. Once Generation completes the header, source files of Thread will be added under config =\> driver/thread.

    <br />

    ![](GUID-DAFA2B4D-BCF6-4556-93DE-ACCD4A1CF70F-low.png)

    <br />

17. RTOS task for thread stack will be created tasks.c file and otSysInit \(\) will be called fromSYS\_Initialize\(\) function.
18. app\_user\_edits.cfile changes: selected line should be commented.

    <br />

    ![](GUID-A3A3CE35-D54B-4623-BEE5-84EC115B038A-low.png)

    <br />


**Parent topic:**[Microchip Thread SDK](GUID-35F8786B-0912-4736-BD9F-7975E01A9D0E.md)

