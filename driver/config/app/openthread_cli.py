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

import inspect
import os
import sys
import glob
import ntpath

folderpathpos = 0
fileslistpos  = 1
#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD FILE GENERATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def importIncFile(component,HeaderFiles,incpath,Enable,DeviceType,custompath = ''):
    # print("Inc_Path:"+incpath,"HeaderFiles:",HeaderFiles)
    HeaderFileSymbls = []
    for file in HeaderFiles:
        if DeviceType != '':
            hdrfilesym = (str(DeviceType)+"_")+((file.upper().replace('.','_')).replace('-','_'))
        else:
            hdrfilesym = (file.upper().replace('.','_')).replace('-','_')
        # print(hdrfilesym)
        try:
            incFileSym = component.createFileSymbol(hdrfilesym, None)
        except:
            # if DeviceType == "FTD":
                # FTD_FILE+=1
                # hdrfilesym = "FTD"+str(FTD_FILE)
            # elif DeviceType == "MTD":
                # MTD_FILE+=1
                # hdrfilesym = "MTD"+str(MTD_FILE)
            # elif DeviceType == "RCP":
                # RCP_FILE+=1
                # hdrfilesym = "RCP"+str(RCP_FILE)
            # else:
                # hdrfilesym = None
            incFileSym = component.createFileSymbol(None, None)
        incFileSym.setOverwrite(True)
        incFileSym.setOutputName(file)
        if 'src' == incpath or 'src/crypto' == incpath:
            incFileSym.setSourcePath(incpath +'/'+ file)
        else:
            incFileSym.setSourcePath('../'+incpath +'/'+ file)
        if custompath != '':
            # print("HeaderFileCustom:"+custompath)
            incFileSym.setDestPath('driver/thread/'+custompath)
            incFileSym.setProjectPath('config/'+configName+'/driver/thread/' + custompath+ '/' +file)
        else:
            # incFileSym.setSourcePath(incpath +'/'+ file)
            incFileSym.setDestPath('driver/thread/'+incpath)
            incFileSym.setProjectPath('config/'+configName+'/driver/thread/' + incpath+ '/' +file)
   
        incFileSym.setType("HEADER")
        incFileSym.setEnabled(Enable)
        
        HeaderFileSymbls.append(incFileSym)
    return HeaderFileSymbls
        
        
def importSrcFile(component,SourceFiles,incpath,Enable,DeviceType,custompath = ''):
    # print("Inc_Path:"+incpath,"SourceFiles:",SourceFiles)
    SourceFileSymbls = []
    for file in SourceFiles:
        if DeviceType != '':
            Srcfilesym = (str(DeviceType)+"_")+((file.upper().replace('.','_')).replace('-','_'))
        else:
            Srcfilesym = (file.upper().replace('.','_')).replace('-','_')
        # print(Srcfilesym)
        try:
            srcFileSym = component.createFileSymbol(Srcfilesym, None)
        except:
            # if DeviceType == "FTD":
                # FTD_FILE+=1
                # Srcfilesym = "FTD"+str(FTD_FILE)
            # elif DeviceType == "MTD":
                # MTD_FILE+=1
                # Srcfilesym = "MTD"+str(MTD_FILE)
            # elif DeviceType == "RCP":
                # RCP_FILE+=1
                # Srcfilesym = "RCP"+str(RCP_FILE)
            # else:
                # Srcfilesym = None
            # print("Entered Except")
            Srcfilesym = (str(DeviceType)+"_")+str(file)
            srcFileSym = component.createFileSymbol(Srcfilesym, None)
        srcFileSym.setOverwrite(True)
        srcFileSym.setOutputName(file)
        if 'src' == incpath or 'src/crypto' == incpath:
            srcFileSym.setSourcePath(incpath+ '/' + file)
        else:
            srcFileSym.setSourcePath('../'+incpath+ '/' + file)
        if custompath != '':
            # print(custompath)
            srcFileSym.setDestPath('driver/thread/'+custompath)
            srcFileSym.setProjectPath('config/'+configName+'/driver/thread/' + custompath+ '/' +file)
        else:
            # srcFileSym.setSourcePath(incpath+ '/' + file)
            srcFileSym.setDestPath('driver/thread/'+incpath)
            srcFileSym.setProjectPath('config/'+configName+'/driver/thread/' + incpath+ '/' +file)
        srcFileSym.setType("SOURCE")
        srcFileSym.setEnabled(Enable)
        
        SourceFileSymbls.append(srcFileSym)
    return SourceFileSymbls



def importfiles(component,includepath,Enable,DeviceType = ''):
    # print("openthread-importfiles")
    # print("DeviceType:"+DeviceType)
    File_symbols = []
    for Incpath in includepath:
        # print(Incpath)
        hdrcustompath = ''
        srccustompath = ''
        incpath = Incpath[0]
        incsubdir = Incpath[1]
        if len(Incpath) > 2:
            incFiles = Incpath[2]
            incfile = Incpath[3]
            if len(Incpath)> 4:
                hdrcustompath = Incpath[4]
                if len(Incpath) > 5:
                    srccustompath = Incpath[5]
        else:
            incFiles = []
            
        for record in range(len(openthreadfileRecords)):
            # print("DirPath:"+openthreadfileRecords[record][folderpathpos]) 
            # print("IncPath:"+incpath)
            # print("\n")
            if incpath == openthreadfileRecords[record][folderpathpos]:
                print("IncPath:"+incpath)
                headerfiles = []
                sourcefiles = []
                for file in openthreadfileRecords[record][fileslistpos]:
                    # print("File:"+file)
                    
                    if incFiles != []:
                        if incfile == False:
                            if file in incFiles:
                                includefile = False
                            else:
                                includefile = True
                        elif incfile == True:
                            if file in incFiles:
                                includefile = True
                            else:
                                includefile = False
                    else:
                        includefile = True
                        
                    if includefile == True:
                        if '.h' in file or '.hpp' in file:
                            headerfiles.append(file)
                        if '.c' in file or '.cpp' in file:
                            if '.cmake' not in file:
                                sourcefiles.append(file)
                                
                                
                if headerfiles != []:
                    if hdrcustompath != '':
                        hdrsymlist = importIncFile(component,headerfiles,incpath ,Enable,DeviceType,hdrcustompath)
                    else:
                        hdrsymlist = importIncFile(component,headerfiles,incpath,Enable,DeviceType)
                    
                    for hdrsymbl in hdrsymlist:   
                        File_symbols.append(hdrsymbl)
                        
                if sourcefiles != []:
                    if srccustompath != '':
                        Srcsymlist = importSrcFile(component,sourcefiles,incpath,Enable,DeviceType,srccustompath)
                    else:
                        Srcsymlist = importSrcFile(component,sourcefiles,incpath,Enable,DeviceType)
                    
                    for srcsymbl in Srcsymlist:
                        File_symbols.append(srcsymbl)
            
                if incsubdir == True:
                    for subrecord in range(len(openthreadfileRecords)):
                        if incpath != openthreadfileRecords[subrecord][folderpathpos]:
                            if incpath in openthreadfileRecords[subrecord][folderpathpos]:
                                subincpath = openthreadfileRecords[subrecord][folderpathpos]
                                # print("SubIncpath:"+openthreadfileRecords[subrecord][folderpathpos])
                                headerfiles1 = []
                                sourcefiles1 = []
                                for file in openthreadfileRecords[subrecord][fileslistpos]:
                                    # print("File:"+file)
                                    if incFiles != []:
                                        if incfile == False:
                                            if file in incFiles:
                                                includefile = False
                                            else:
                                                includefile = True
                                        elif incfile == True:
                                            if file in incFiles:
                                                includefile = True
                                            else:
                                                includefile = False
                                    else:
                                        includefile = True
                                    
                                    if includefile == True:
                                        if '.h' in file or '.hpp' in file:
                                            headerfiles1.append(file)
                                        if ('.c' in file) or ('.cpp' in file):
                                            if '.cmake' not in file:
                                                sourcefiles1.append(file)
                                if headerfiles1 != []:
                                    if hdrcustompath != '':
                                        hdrsymlist = importIncFile(component,headerfiles1,subincpath,Enable,DeviceType,hdrcustompath)
                                    else:
                                        hdrsymlist = importIncFile(component,headerfiles1,subincpath,Enable,DeviceType)
                                    for hdrsymbl in hdrsymlist:
                                        File_symbols.append(hdrsymbl)
                                        
                                if sourcefiles1 != []:
                                    if srccustompath != '':
                                        Srcsymlist = importSrcFile(component,sourcefiles1,subincpath,Enable,DeviceType,srccustompath)
                                    else:
                                        Srcsymlist = importSrcFile(component,sourcefiles1,subincpath,Enable,DeviceType)
                                    for srcsymbl in Srcsymlist:
                                        File_symbols.append(srcsymbl)
                                                                
    return File_symbols  


def setIncPath(component, incPaths):
    # print("setIncPath-Entered")
    for incPath in incPaths:
        incPathSym = component.createSettingSymbol("OPENTHREAD_INC_PATH_C" + incPath.replace(".", "_").replace("/", "_").upper(), None)
        incPathSym.setValue("../src/config/" + configName + "/driver/thread" +incPath + ";")
        incPathSym.setCategory("C32")
        incPathSym.setKey("extra-include-directories")
        incPathSym.setAppend(True, ";")
        incPathSym.setEnabled(True)
        # incPathSym.setDependencies(callback, dependencies)
        
        incPathSymCpp = component.createSettingSymbol("OPENTHREAD_INC_PATH_CPP" + incPath.replace(".", "_").replace("/", "_").upper(), None)
        incPathSymCpp.setValue("../src/config/" + configName + "/driver/thread" + incPath + ";")
        incPathSymCpp.setCategory("C32CPP")
        incPathSymCpp.setKey("extra-include-directories")
        incPathSymCpp.setAppend(True, ";")
        incPathSymCpp.setEnabled(True)
        # incPathSymCpp.setDependencies(callback, dependencies)
        

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Callbacks ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def OpenThreadConfigChangeCallback(symbol,event):
    print('OpenThreadConfigChangeCallback',symbol,event)
    remoteSymbol = event['symbol']
    symbolID = event["id"]
    value = event["value"]
    if symbolID == "OPEN_THREAD_DEVICE_ROLE_CONFIG_2":
        openthreadRoleSelected.setValue(str(remoteSymbol.getSelectedKey()))

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ File Parsing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPONENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def instantiateComponent(openthreadcli):
    global open_thread_cli
    open_thread_cli = openthreadcli
    print("Open Thread CLI")
    
    global configName
    configName = Variables.get("__CONFIGURATION_NAME")
    
    global requiredComponents
    requiredComponents = [
        "OPEN_THREAD"
    ]
    
    res = Database.activateComponents(requiredComponents)
    
    execfile(Module.getPath() + '/driver/config/stack/openthread_filesystem_Parser.py')
    
    # print("***********************************************")
    # print("\tOpen Thread File System Cli")
    # print("***********************************************")
    # for i in range(len(openthreadfileRecords)):
        # print(openthreadfileRecords[i])
        # print('\n')
    # print("***********************************************")
    
    # global openthreadRoleSelected
    # openthreadRoleSelected = openthreadcli.createStringSymbol("OPEN_THREAD_ROLE_SELECTED",None)
    # openthreadRoleSelected.setLabel("Selected Thread Role")
    # openthreadRoleSelected.setDefaultValue(Database.getComponentByID("OPEN_THREAD").getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CONFIG_2").getSelectedKey())
    # openthreadRoleSelected.setVisible(True)
    # openthreadRoleSelected.setReadOnly(True)
    # openthreadRoleSelected.setDependencies(OpenThreadConfigChangeCallback,['OPEN_THREAD.OPEN_THREAD_DEVICE_ROLE_CONFIG_2'])
    
    global openthreadroleCliconfig
    openthreadroleCliconfig = openthreadcli.createKeyValueSetSymbol("OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG", None)
    openthreadroleCliconfig.setLabel("Thread Device Role")
    openthreadroleCliconfig.addKey("FTD", "FTD", "FTD")
    openthreadroleCliconfig.addKey("MTD", "MTD", "MTD")
    openthreadroleCliconfig.setDefaultValue(0)
    openthreadroleCliconfig.setOutputMode("Value")
    openthreadroleCliconfig.setDisplayMode("Description")
    openthreadroleCliconfig.setDescription("Open Thread Device Role Configuration")
    openthreadroleCliconfig.setVisible(True)
    # openthreadroleCliconfig.setReadOnly(True)
    
    global openthreadclicomment1
    openthreadclicomment1 = openthreadcli.createCommentSymbol("OPEN_THREAD_CLI_COMMENT_1",None)
    openthreadclicomment1.setLabel("*****CLI is not supported with RCP*****")
    openthreadclicomment1.setVisible(True)
    
    global openthreadcliUartService
    openthreadcliUartService = openthreadcli.createBooleanSymbol("OPEN_THREAD_CLI_UART_SYM",None)
    openthreadcliUartService.setLabel("CLI Uart")
    openthreadcliUartService.setVisible(False)
    openthreadcliUartService.setDefaultValue(0)
    
    #CLI File includes paths
    global CliIncPath
    CliIncPath   =   [['openthread/src/cli',False],
                      ['openthread/examples/apps/cli',False,['cli_uart.cpp'],True]
                     ]
                     
    importfiles(open_thread_cli,CliIncPath,True)
    
    #CLI File Include Paths
    global CliIncPaths
    CliIncPaths = ["/openthread/examples/apps"
  
                     ]
                      
    setIncPath(open_thread_cli,CliIncPaths)
    
    
    

def finalizeComponent(openthreadcli):
    pass


def onAttachmentConnected(source, target):
    print('onAttachmentConnected-Cli')
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    if connectID == "openthread_Dependency":
        openthreadcliUartService.setValue(True)
        
    

def destroyComponent(openthreadcli):
    openthreadcliUartService.setValue(False)
