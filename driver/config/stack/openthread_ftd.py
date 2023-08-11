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
#open thread FTD Configuration

"""
    The File path list has the following information
    #0 - Base Dir path 
    #1 - Include sub Directories into Generation - 
        True - To include Files from sub directories in the Generation
        False - Do not include
    #2 - List of Files to Include/Exclude - [] --> if no list available
    #3 - Boolean to Include/Exclude files from #2 
        True: Include files from the list
        False: Exclude files from the list
    #4  Custom path for Header File Generation 
    #5  Custom path for Source File Generation
"""

#FTD,MTD File includes paths
global coreincpath_ftd
coreincpath_ftd   = [['openthread/src/core/common',False,["extension_example.cpp"],False],
                         ['openthread/src/core/api',False],
                         ['openthread/src/core/backbone_router',False],
                         ['openthread/src/core/border_router',False,["routing_manager.hpp"],True],
                         ['openthread/src/core/coap',False],
                         ['openthread/src/core/config',False],
                         ['openthread/src/core/crypto',False],
                         ['openthread/src/core/diags',False],
                         ['openthread/src/core/mac',False],
                         ['openthread/src/core/meshcop',False],
                         ['openthread/src/core/net',False],
                         ['openthread/src/core/radio',False],
                         ['openthread/src/core/thread',False],
                         ['openthread/src/core/utils',False],
                         ['openthread/src/core',False]
                        ]

Handle_FTD_MTD_RCP_FileSymbls(openthread,coreincpath_ftd,["FTD"])



#FTD config includes
# global ftdconfigincpath
# ftdconfigincpath   = [["examples/config/ftd",False,['ot_tasks.c'],False,"config","src"]] #Default configuration

# Handle_FTD_MTD_RCP_FileSymbls(openthread,ftdconfigincpath,["FTD"])

global openthreadftdconfigMenu
openthreadftdconfigMenu = openthread.createMenuSymbol("OPEN_THREAD_FTD_MENU_SYMBOL", openthreadcoreconfig)
openthreadftdconfigMenu.setLabel("FTD Configuration")
openthreadftdconfigMenu.setVisible(True)

global openthreadftdMleMaxChildconfig
openthreadftdMleMaxChildconfig = openthread.createIntegerSymbol("OPEN_THREAD_FTD_MLE_MAX_CHILD_CONFIG",openthreadftdconfigMenu)
openthreadftdMleMaxChildconfig.setLabel("Maximum children")
openthreadftdMleMaxChildconfig.setDefaultValue(10)
openthreadftdMleMaxChildconfig.setMin(10)
openthreadftdMleMaxChildconfig.setMax(32)
openthreadftdMleMaxChildconfig.setVisible(True)
openthreadftdMleMaxChildconfig.setDescription("Open Thread MLE Max Children")
# openthreadftdEnable.setDependencies(openthreadParserUpdateCallback,['OPEN_THREAD_UART_PARSER'])

global openthreadftdMleIpAddrPerChildConfig
openthreadftdMleIpAddrPerChildConfig = openthread.createIntegerSymbol("OPEN_THREAD_MLE_IP_ADDR_PER_CHILD",openthreadftdconfigMenu)
openthreadftdMleIpAddrPerChildConfig.setLabel("IP Addr Per Child")
openthreadftdMleIpAddrPerChildConfig.setDefaultValue(4)
openthreadftdMleIpAddrPerChildConfig.setMin(4)
openthreadftdMleIpAddrPerChildConfig.setMax(8)
openthreadftdMleIpAddrPerChildConfig.setVisible(True)
openthreadftdMleIpAddrPerChildConfig.setDescription("Open Thread MLE IP Addr Per Child")

global openthreadftdInBandCommissioningConfig
openthreadftdInBandCommissioningConfig = openthread.createBooleanSymbol("OPEN_THREAD_FTD_IN_BAND_COMMISSIONING_CONFIG",openthreadftdconfigMenu)
openthreadftdInBandCommissioningConfig.setLabel("In Band Commissioning")
openthreadftdInBandCommissioningConfig.setDefaultValue(0)
openthreadftdInBandCommissioningConfig.setVisible(True)
openthreadftdInBandCommissioningConfig.setDescription("In Band Commissioning Enable")
openthreadftdInBandCommissioningConfig.setDependencies(openthreadFtdConfigcallback,["OPEN_THREAD_FTD_IN_BAND_COMMISSIONING_CONFIG"])


# global openthreadftdNumMsgBuffersConfig
# openthreadftdNumMsgBuffersConfig = openthread.createIntegerSymbol("OPEN_THREAD_FTD_NUM_MSG_BUFFERS",openthreadftdconfigMenu)
# openthreadftdNumMsgBuffersConfig.setLabel("Num of Message Buffers")
# openthreadftdNumMsgBuffersConfig.setDefaultValue(44)
# openthreadftdNumMsgBuffersConfig.setMin(44)
# openthreadftdNumMsgBuffersConfig.setMax(60)
# openthreadftdNumMsgBuffersConfig.setVisible(True)
# openthreadftdNumMsgBuffersConfig.setDescription("Open Thread Num of Message Buffers")

global openthreadftdJoinerEnable
openthreadftdJoinerEnable = openthread.createBooleanSymbol("OPEN_THREAD_FTD_JOINER_ENABLE",openthreadftdconfigMenu)
openthreadftdJoinerEnable.setLabel("Joiner")
openthreadftdJoinerEnable.setDefaultValue(1)
openthreadftdJoinerEnable.setVisible(False)
openthreadftdJoinerEnable.setDescription("Open Thread Joiner Enable")


global openthreadftdCommissionerEnable
openthreadftdCommissionerEnable = openthread.createBooleanSymbol("OPEN_THREAD_FTD_COMMISSIONER_ENABLE",openthreadftdconfigMenu)
openthreadftdCommissionerEnable.setLabel("Commissioner")
openthreadftdCommissionerEnable.setDefaultValue(0)
openthreadftdCommissionerEnable.setVisible(False)
openthreadftdCommissionerEnable.setDescription("Open Thread Commssioner Enable")

global ftdconfigfilesym
ftdconfigfilesym = openthread.createFileSymbol('FTD_OPEN_THREAD_CONFIG',None)
ftdconfigfilesym.setSourcePath("/driver/templates/stack/openthread_stack_config_ftd.h.ftl")
ftdconfigfilesym.setOutputName("openthread_stack_config.h")
ftdconfigfilesym.setDestPath('driver/thread/inc')
ftdconfigfilesym.setProjectPath('config/'+configName+'/driver/thread/inc/openthread_stack_config.h')
ftdconfigfilesym.setType("HEADER")
ftdconfigfilesym.setOverwrite(True)
ftdconfigfilesym.setMarkup(True)
ftdconfigfilesym.setEnabled(False)

FTD_FILE_SYMBOLS.append(ftdconfigfilesym)


#Enable FTD File Symbols --> Default Role = FTD
EnableFileSymbls("FTD")