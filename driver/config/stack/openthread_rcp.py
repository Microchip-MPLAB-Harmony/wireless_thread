##############################################################################
# Copyright (C) [2023], Microchip Technology Inc., and its subsidiaries. All rights reserved.
  
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
#open thread RCP Configuration

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


#RCP File includes paths
global commonincpath_rcp
commonincpath_rcp = [ 
                    ['openthread/src/core/config',False],
                    ['openthread/src/core/crypto',False],
                    ['openthread/src/core/diags',False],
                    ['openthread/src/core/mac',False,['link_raw.cpp', 'link_raw.hpp','mac_frame.cpp', 'mac_frame.hpp','mac_types.cpp', 'mac_types.hpp', 'sub_mac.cpp', 'sub_mac.hpp', 'sub_mac_callbacks.cpp'],True],
                    ['openthread/src/core/meshcop',False,['network_name.hpp','extended_panid.hpp'],True],
                    ['openthread/src/core/net',False,['icmp6.hpp','ip4_types.hpp','ip6.hpp','ip6_address.hpp','ip6_headers.hpp','ip6_mpl.hpp','ip6_types.hpp','nat64_translator.hpp','netif.hpp','socket.hpp','tcp6.hpp','udp6.hpp','checksum.hpp'],True],
                    ['openthread/src/core',False],
                    ['openthread/src/core/radio',False,['trel_interface.cpp','trel_link.cpp','trel_packet.cpp'],False],
                    ['openthread/src/core/thread',False,['topology.hpp','child_mask.hpp','link_quality.hpp','mle_types.hpp','network_data_types.hpp','mlr_types.hpp'],True],
                    ['openthread/src/core/utils',False,['heap.cpp','heap.hpp','otns.hpp','power_calibration.hpp'],True],
                    ['openthread/src/core/api',False,["instance_api.cpp","link_raw_api.cpp","logging_api.cpp","message_api.cpp","random_noncrypto_api.cpp","tasklet_api.cpp"],True],
                                                            
                    ['openthread/src/core/common',False,["appender.cpp",     "appender.hpp",        #"arg_macros.hpp",
                                                        "binary_search.cpp", #"bit_vector.hpp",
                                                        "crc16.cpp",         "crc16.hpp",           "extension_example.cpp",
                                                        "frame_builder.cpp", "frame_builder.hpp",   "frame_data.cpp", 
                                                        "heap.cpp",            "heap_allocatable.hpp", 
                                                        "heap_array.hpp",    "heap_data.cpp",       "heap_data.hpp",       "heap_string.cpp", 
                                                        "heap_string.hpp",   "notifier.cpp",        "retain_ptr.hpp",       
                                                        "settings.cpp",      "settings.hpp",        "settings_driver.hpp", "time_ticker.cpp",
                                                        "trickle_timer.cpp", "trickle_timer.hpp",   "uptime.cpp"],False],

                   # ['openthread/src/lib/spinel',False],
                   # ['openthread/src/lib/hdlc',False],
                   # ['openthread/src/lib/platform',False],
                   # ['openthread/src/lib/url',False],
                   ['openthread/src/lib',True],
                   ['openthread/src/ncp',False],
                   ['openthread/examples/apps/ncp',False,['ncp.c'],True]
                  ]

Handle_FTD_MTD_RCP_FileSymbls(openthread,commonincpath_rcp,["RCP"])


#RCP config includes
# global rcpconfigincpath
# rcpconfigincpath   = [["examples/config/rcp",False,['ot_tasks.c'],False,"config","src"]] #Default configuration

# Handle_FTD_MTD_RCP_FileSymbls(openthread,rcpconfigincpath,["RCP"])

global openthreadrcpconfigMenu
openthreadrcpconfigMenu = openthread.createMenuSymbol("OPEN_THREAD_RCP_MENU_SYMBOL", openthreadcoreconfig)
openthreadrcpconfigMenu.setLabel("RCP Configuration")
openthreadrcpconfigMenu.setVisible(False)

global openthreadRcpHdlcConfig
openthreadRcpHdlcConfig = openthread.createKeyValueSetSymbol("OPEN_THREAD_RCP_HDLC_CONFIG", openthreadrcpconfigMenu)
openthreadRcpHdlcConfig.setLabel("HDLC Interface")
openthreadRcpHdlcConfig.addKey("UART", "UART", "UART")
openthreadRcpHdlcConfig.setDefaultValue(0)
openthreadRcpHdlcConfig.setOutputMode("Value")
openthreadRcpHdlcConfig.setDisplayMode("Description")
openthreadRcpHdlcConfig.setDescription("Open Thread Device Role Configuration")
openthreadRcpHdlcConfig.setVisible(True)

global rcpconfigfilesym
rcpconfigfilesym = openthread.createFileSymbol('RCP_OPEN_THREAD_CONFIG',None)
rcpconfigfilesym.setSourcePath("/driver/templates/stack/openthread_stack_config_rcp.h.ftl")
rcpconfigfilesym.setOutputName("openthread_stack_config.h")
rcpconfigfilesym.setDestPath('driver/thread/inc')
rcpconfigfilesym.setProjectPath('config/'+configName+'/driver/thread/inc/openthread_stack_config.h')
rcpconfigfilesym.setType("HEADER")
rcpconfigfilesym.setOverwrite(True)
rcpconfigfilesym.setMarkup(True)
rcpconfigfilesym.setEnabled(False)

RCP_FILE_SYMBOLS.append(rcpconfigfilesym)
