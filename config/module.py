##############################################################################
# Copyright (C) [2024], Microchip Technology Inc., and its subsidiaries. All rights reserved.
  
# The software and documentation is provided by Microchip and its contributors 
# "as is" and any express, implied or statutory warranties, including, but not 
# limited to, the implied warranties of merchantability, fitness for a particular 
# purpose and non-infringement of third party intellectual property rights are 
# disclaimed to the fullest extent permitted by law. In no event shall Microchip 
# or its contributors be liable for any direct, indirect, incidental, special,
# exemplary, or consequential damages (including, but not limited to, procurement 
# of substitute goods or services; loss of use, data, or profits; or business 
# interruption) however caused and on any theory of liability, whether in contract, 
# strict liability, or tort (including negligence or otherwise) arising in any way 
# out of the use of the software and documentation, even if advised of the 
# possibility of such damage.
# 
# Except as expressly permitted hereunder and subject to the applicable license terms 
# for any third-party software incorporated in the software and any applicable open 
# source software license terms, no license or other rights, whether express or 
# implied, are granted under any patent or other intellectual property rights of 
# Microchip or any third party.
##############################################################################

def loadModule():
    print("Load Module: Harmony Open Thread SDK")

    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          'WBZ451H'
                          } 
                          
    processor = Variables.get('__PROCESSOR') 
    
    print('processor={}'.format(processor))
                          
    if (processor in pic32cx_bz2_family):                      
        openthread  = Module.CreateComponent('OPEN_THREAD', 'Thread Stack', 'Wireless/Drivers/Thread', 'driver/config/stack/drv_openthread.py')
        openthread.setDisplayType('Thread SDK Driver')
        openthread.addDependency('OT_802154phy_dependency', 'IEEE 802.15.4 PHY', 'IEEE 802.15.4 PHY', True, True)
        openthread.addDependency("OT_WolfCrypt_Dependency", "LIB_WOLFCRYPT", None, False, True)
        openthread.addDependency("OT_USART_dependency", "DRV_USART", 'Thread USART', False, False)
        openthread.addDependency("OT_CONSOLE_dependency", "SYS_CONSOLE", 'Thread Log', False, True)
        openthread.addDependency('OT_SysTimeDependency', 'SYS_TIME', 'SYS_TIME', True, True)
        openthread.addDependency('OT_FreeRtosDependency', 'RTOS', 'RTOS', True, True)
        openthread.addDependency('OT_HarmonyCoreDependency', 'Core Service', 'Core', True, True)
        openthread.addDependency('OT_DeviceSupportDependency', 'Device_Support', 'Device_Support', True, True)
        openthread.addDependency('OT_PDS_Module_Dependency', 'PDS_SubSystem', None, True, True)
        openthread.addCapability('openthread_Capability', 'Thread Stack', True)
        
        
        openthreadcli  = Module.CreateComponent('THREAD_CLI', 'CLI', 'Wireless/Drivers/Thread/App', 'driver/config/app/openthread_cli.py')
        openthreadcli.setDisplayType('Thread Serial Interface')
        openthreadcli.addDependency('openthread_Dependency', 'Thread Stack','Thread Stack',True, True)
        

        
