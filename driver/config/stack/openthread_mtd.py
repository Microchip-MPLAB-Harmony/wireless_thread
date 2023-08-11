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

MTD_FILE_SYMBOLS.append(mtdconfigfilesym)