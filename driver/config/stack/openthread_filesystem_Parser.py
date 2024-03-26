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

#Global list with openthread file list record
global openthreadfileRecords
openthreadfileRecords = []
#Absolute paths to Parse through the repo
global abs_paths
abs_paths = [
             'openthread/include/openthread',
             'openthread/include/openthread/platform',
             'openthread/src/cli',
             'openthread/src/core',
             'openthread/src/core/api',
             'openthread/src/core/backbone_router',
             'openthread/src/core/border_router',
             'openthread/src/core/coap',
             'openthread/src/core/common',
             'openthread/src/core/config',
             'openthread/src/core/crypto',
             'openthread/src/core/diags',
             'openthread/src/core/mac',
             'openthread/src/core/meshcop',
             'openthread/src/core/net',
             'openthread/src/core/radio',
             'openthread/src/core/thread',
             'openthread/src/core/utils',
             'openthread/src/lib/hdlc',
             'openthread/src/lib/platform',
             'openthread/src/lib/spinel',
             'openthread/src/lib/url',
             'openthread/src/ncp',
             'openthread/third_party/mbedtls',
             'openthread/third_party/mbedtls/repo/configs',
             'openthread/third_party/mbedtls/repo/include/mbedtls',
             'openthread/third_party/mbedtls/repo/include/psa',
             'openthread/third_party/mbedtls/repo/library',
             'openthread/third_party/tcplp',
             'openthread/third_party/tcplp/bsdtcp',
             'openthread/third_party/tcplp/bsdtcp/cc',
             'openthread/third_party/tcplp/bsdtcp/sys',
             'openthread/third_party/tcplp/lib',
             'openthread/examples/platforms',
             'openthread/examples/platforms/utils',
             'openthread/examples/apps/cli',
             'openthread/examples/apps/ncp' 
             
            ]
global plat_abs_path
plat_abs_path = [
                    'driver/src/stack/pic32cx_bz2/src',
                    'driver/src/stack/pic32cx_bz2/src/crypto'
                ]
      

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ File Parsing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------

def get_file_names(path):
    files = []
    c_files = glob.glob(path + "/*.c")
    # print("c_files",c_files)
    h_files = glob.glob(path + "/*.h")
    # print("h_files",h_files)
    cpp_files = glob.glob(path + "/*.cpp")
    # print("cpp_files",cpp_files)
    hpp_files = glob.glob(path + "/*.hpp")
    # print("hpp_files",hpp_files)
    for file in c_files:
        filename = ntpath.basename(file)
        files.append(filename)
    for file in h_files:
        filename = ntpath.basename(file)
        files.append(filename)
    for file in cpp_files:
        filename = ntpath.basename(file)
        files.append(filename)
    for file in hpp_files:
        filename = ntpath.basename(file)
        files.append(filename)
    # print("files",files)
    return files



if openthreadfileRecords == []:
    wirelessthreadDir = get_script_dir() + "/../../../"
    thirdpartyopenthreadDir = get_script_dir() + "/../../../../"
    for path in abs_paths:
        openthread_include =  thirdpartyopenthreadDir + path
            # print("openthread_include",openthread_include)
        files = get_file_names(openthread_include)
        # print("Global Executed",files)
        localDirList = []
        localDirList.append(path)
        localDirList.append(files)
        openthreadfileRecords.append(localDirList)
        
    for path in plat_abs_path:
        openthread_include =  wirelessthreadDir + path
        files = get_file_names(openthread_include)
        # print("Global Executed",files)
        localDirList = []
        localDirList.append(path)
        localDirList.append(files)
        openthreadfileRecords.append(localDirList)

    for i in range(len(openthreadfileRecords)):
        print(openthreadfileRecords[i])
        print('\n')




