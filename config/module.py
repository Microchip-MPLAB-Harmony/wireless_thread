# coding: utf-8
##############################################################################
# Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

def loadModule():
    print("Load Module: Harmony Open Thread SDK")

    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          } 
                          
    processor = Variables.get('__PROCESSOR') 
    
    print('processor={}'.format(processor))
                          
    if (processor in pic32cx_bz2_family):                      
        openthread  = Module.CreateComponent('OPEN_THREAD', 'Thread Stack', 'Wireless/Drivers/Thread', 'driver/config/stack/drv_openthread.py')
        openthread.setDisplayType('Thread SDK Driver')
        openthread.addDependency('OT_802154phy_dependency', 'IEEE 802.15.4 PHY', 'IEEE 802.15.4 PHY', True, True)
        openthread.addDependency("OT_WolfCrypt_Dependency", "LIB_WOLFCRYPT", None, False, True)
        openthread.addDependency("OT_USART_dependency", "DRV_USART", 'Thread USART', False, False)
        openthread.addDependency('OT_SysTimeDependency', 'SYS_TIME', 'SYS_TIME', True, True)
        openthread.addDependency('OT_FreeRtosDependency', 'RTOS', 'RTOS', True, True)
        openthread.addDependency('OT_HarmonyCoreDependency', 'Core Service', 'Core', True, True)
        openthread.addDependency('OT_DeviceSupportDependency', 'Device_Support', 'Device_Support', True, True)
        openthread.addDependency('OT_PDS_Module_Dependency', 'PDS_SubSystem', None, True, True)
        openthread.addCapability('openthread_Capability', 'Thread Stack', True)
        
        
        openthreadcli  = Module.CreateComponent('THREAD_CLI', 'CLI', 'Wireless/Drivers/Thread/App', 'driver/config/app/openthread_cli.py')
        openthreadcli.setDisplayType('Thread Serial Interface')
        openthreadcli.addDependency('openthread_Dependency', 'Thread Stack','Thread Stack',True, True)
        

        
