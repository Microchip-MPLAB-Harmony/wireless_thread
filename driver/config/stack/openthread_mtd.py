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
#open thread MTD Configuration

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
# global coreincpath_ftd_mtd
global coreincpath_mtd
coreincpath_mtd   = [['openthread/src/core/common',False,["extension_example.cpp"],False],
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

Handle_FTD_MTD_RCP_FileSymbls(openthread,coreincpath_mtd,["MTD"])#["FTD","MTD"])



#MTD config includes
# global mtdconfigincpath
# mtdconfigincpath   = [["examples/config/mtd",False,['ot_tasks.c'],False,"config","src"]] #Default configuration

# Handle_FTD_MTD_RCP_FileSymbls(openthread,mtdconfigincpath,["MTD"])
global MTD_OPTION_SYMBOLS
MTD_OPTION_SYMBOLS = []

global openthreadmtdconfigMenu
openthreadmtdconfigMenu = openthread.createMenuSymbol("OPEN_THREAD_MTD_MENU_SYMBOL", openthreadcoreconfig)
openthreadmtdconfigMenu.setLabel("MTD Configuration")
openthreadmtdconfigMenu.setVisible(False)

global openthreadmtdsleepEnable
openthreadmtdsleepEnable = openthread.createBooleanSymbol("OPEN_THREAD_MTD_SLEEP_ENABLE",openthreadmtdconfigMenu)
openthreadmtdsleepEnable.setLabel("Enable Sleep")
openthreadmtdsleepEnable.setDefaultValue(0)
openthreadmtdsleepEnable.setVisible(True)
openthreadmtdsleepEnable.setDescription("Enable Sleep Configuration")
openthreadmtdsleepEnable.setDependencies(openthreadMtdConfigcallback,["OPEN_THREAD_MTD_SLEEP_ENABLE"])

# global openthreadmtdPollPeriod
# openthreadmtdPollPeriod = openthread.createIntegerSymbol("OPEN_THREAD_MTD_POLL_PERIOD",openthreadmtdconfigMenu)
# openthreadmtdPollPeriod.setLabel("Poll Period(sec)")
# openthreadmtdPollPeriod.setDefaultValue(240)
# openthreadmtdMleChildTimeout.setMin("240")
# openthreadmtdPollPeriod.setVisible(False)
# openthreadmtdPollPeriod.setDescription("Child Poll Period")
# openthreadmtdPollPeriod.setDependencies(openthreadMtdConfigcallback,["OPEN_THREAD_MTD_SLEEP_ENABLE"])

global openthreadmtdMleChildTimeout
openthreadmtdMleChildTimeout = openthread.createIntegerSymbol("OPEN_THREAD_MTD_MLE_CHILD_TIMEOUT",openthreadmtdconfigMenu)
openthreadmtdMleChildTimeout.setLabel("MLE Child Timeout(sec)")
openthreadmtdMleChildTimeout.setDefaultValue(240)
openthreadmtdMleChildTimeout.setMin(1)
openthreadmtdMleChildTimeout.setVisible(True)
openthreadmtdMleChildTimeout.setDescription("MLE Child Timeout")


global openthreadmtdInBandCommissioningConfig
openthreadmtdInBandCommissioningConfig = openthread.createBooleanSymbol("OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG",openthreadmtdconfigMenu)
openthreadmtdInBandCommissioningConfig.setLabel("In Band Commissioning")
openthreadmtdInBandCommissioningConfig.setDefaultValue(0)
openthreadmtdInBandCommissioningConfig.setVisible(True)
openthreadmtdInBandCommissioningConfig.setDescription("In Band Commissioning Enable")
openthreadmtdInBandCommissioningConfig.setDependencies(openthreadMtdConfigcallback,["OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG"])


global openthreadmtdJoinerEnable
openthreadmtdJoinerEnable = openthread.createBooleanSymbol("OPEN_THREAD_MTD_JOINER_ENABLE",openthreadmtdconfigMenu)
openthreadmtdJoinerEnable.setLabel("Joiner")
openthreadmtdJoinerEnable.setDefaultValue(1)
openthreadmtdJoinerEnable.setVisible(False)
openthreadmtdJoinerEnable.setDescription("Open Thread Joiner Enable")
# openthreadmtdInBandCommissioningConfig.setDependencies(openthreadMtdConfigcallback,["OPEN_THREAD_MTD_JOINER_ENABLE"])


# global openthreadmtdCommissionerEnable
# openthreadmtdCommissionerEnable = openthread.createBooleanSymbol("OPEN_THREAD_MTD_COMMISSIONER_ENABLE",openthreadmtdconfigMenu)
# openthreadmtdCommissionerEnable.setLabel("Enable Commissioner")
# openthreadmtdCommissionerEnable.setDefaultValue(0)
# openthreadmtdCommissionerEnable.setVisible(False)
# openthreadmtdCommissionerEnable.setDescription("Open Thread Commssioner Enable")

global openthreadmtdLibraryEnable
openthreadmtdLibraryEnable = openthread.createLibrarySymbol("OPEN_THREAD_MTD_LIB_ENABLE",None)
openthreadmtdLibraryEnable.setDestPath("/driver/lib")
openthreadmtdLibraryEnable.setSourcePath("/driver/src/stack/pic32cx_bz2/lib/lib-OpenThread_MTD.a")
openthreadmtdLibraryEnable.setOutputName("lib-OpenThread_MTD.a")
openthreadmtdLibraryEnable.setEnabled(False)

global mtdconfigfilesym
mtdconfigfilesym = openthread.createFileSymbol('MTD_OPEN_THREAD_CONFIG',None)
mtdconfigfilesym.setSourcePath("/driver/templates/stack/openthread_stack_config_mtd.h.ftl")
mtdconfigfilesym.setOutputName("openthread_stack_config.h")
mtdconfigfilesym.setDestPath('driver/thread/inc')
mtdconfigfilesym.setProjectPath('config/'+configName+'/driver/thread/inc/openthread_stack_config.h')
mtdconfigfilesym.setType("HEADER")
mtdconfigfilesym.setOverwrite(True)
mtdconfigfilesym.setMarkup(True)
mtdconfigfilesym.setEnabled(False)

MTD_HDR_FILE_SYMBOLS.append(mtdconfigfilesym)
# MTD_FILE_SYMBOLS.append(openthreadmtdLibraryEnable)

MTD_OPTION_SYMBOLS.extend([openthreadmtdsleepEnable,openthreadmtdMleChildTimeout,openthreadmtdInBandCommissioningConfig,openthreadmtdJoinerEnable])