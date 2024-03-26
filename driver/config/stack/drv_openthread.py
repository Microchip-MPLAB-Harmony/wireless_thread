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
#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD CONFIGURATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
import inspect
import os
import sys
import glob
import ntpath

global FTD_HDR_FILE_SYMBOLS
FTD_HDR_FILE_SYMBOLS = []
global FTD_SRC_FILE_SYMBOLS
FTD_SRC_FILE_SYMBOLS = []
global MTD_HDR_FILE_SYMBOLS
MTD_HDR_FILE_SYMBOLS = []
global MTD_SRC_FILE_SYMBOLS
MTD_SRC_FILE_SYMBOLS = []
global COMMON_HDR_FILE_SYMBOLS
COMMON_HDR_FILE_SYMBOLS = []
global COMMON_SRC_FILE_SYMBOLS
COMMON_SRC_FILE_SYMBOLS = []
global PAL_HDR_FILE_SYMBOLS
PAL_HDR_FILE_SYMBOLS = []
global PAL_SRC_FILE_SYMBOLS
PAL_SRC_FILE_SYMBOLS = []
global RCP_FILE_SYMBOLS
RCP_FILE_SYMBOLS = []
global TCP_HDR_FILE_SYMBOLS
TCP_HDR_FILE_SYMBOLS = []
global TCP_SRC_FILE_SYMBOLS
TCP_SRC_FILE_SYMBOLS = []
folderpathpos = 0
fileslistpos  = 1
# FTD_FILE = 0
# MTD_FILE = 0
# RCP_FILE = 0
TcpEnabled = 0


pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          } 
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
        if src_path1 == incpath or src_path2 == incpath:
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
        if src_path1 == incpath or src_path2 == incpath:
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
    Hdr_File_symbols = []
    Src_File_symbols = []
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
                # print("IncPath:"+incpath)
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
                        Hdr_File_symbols.append(hdrsymbl)
                        
                if sourcefiles != []:
                    # if openthreadlibraryGen.getValue() == False or 'src' == incpath or 'src/crypto' == incpath:
                        if srccustompath != '':
                            Srcsymlist = importSrcFile(component,sourcefiles,incpath,Enable,DeviceType,srccustompath)
                        else:
                            Srcsymlist = importSrcFile(component,sourcefiles,incpath,Enable,DeviceType)
                        
                        for srcsymbl in Srcsymlist:
                            Src_File_symbols.append(srcsymbl)
            
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
                                        Hdr_File_symbols.append(hdrsymbl)
                                        
                                if sourcefiles1 != []:
                                    # if openthreadlibraryGen.getValue() == False or 'src' == incpath or 'src/crypto' == incpath:
                                        if srccustompath != '':
                                            Srcsymlist = importSrcFile(component,sourcefiles1,subincpath,Enable,DeviceType,srccustompath)
                                        else:
                                            Srcsymlist = importSrcFile(component,sourcefiles1,subincpath,Enable,DeviceType)
                                        for srcsymbl in Srcsymlist:
                                            Src_File_symbols.append(srcsymbl)
                                                                
    return Hdr_File_symbols,Src_File_symbols                                


def Handle_FTD_MTD_RCP_FileSymbls(component,DirPathlist,DeviceType = []):
    
    if DeviceType != []:
        if "FTD" in DeviceType:
            ftdHdrfilesymb,ftdSrcfilesymb = importfiles(component,DirPathlist,False,DeviceType="FTD")
            for symb in ftdHdrfilesymb:
                FTD_HDR_FILE_SYMBOLS.append(symb)
            for symb in ftdSrcfilesymb:
                FTD_SRC_FILE_SYMBOLS.append(symb)
        if "MTD" in DeviceType:
            mtdHdrfilesymb,mtdSrcfilesymb = importfiles(component,DirPathlist,False,DeviceType="MTD")
            for symb in mtdHdrfilesymb:
                MTD_HDR_FILE_SYMBOLS.append(symb)
            for symb in mtdSrcfilesymb:
                MTD_SRC_FILE_SYMBOLS.append(symb)
        if "RCP" in DeviceType:
            rcpHdrfilesymb,rcpSrcfilesymb = importfiles(component,DirPathlist,False,DeviceType="RCP")
            for symb in rcpHdrfilesymb:
                RCP_FILE_SYMBOLS.append(symb)
            for symb in rcpSrcfilesymb:
                RCP_FILE_SYMBOLS.append(symb)
    

def EnableFileSymbls(DeviceType):
    if DeviceType == "FTD":
        for symbl in FTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(True)
        if openthreadlibraryGen.getSelectedKey() == "Source":
            for symbl in FTD_SRC_FILE_SYMBOLS:
                symbl.setEnabled(True) 
            openthreadftdLibraryEnable.setEnabled(False)
        elif openthreadlibraryGen.getSelectedKey() == "Library":
            openthreadftdLibraryEnable.setEnabled(True)
            for symbl in FTD_SRC_FILE_SYMBOLS:
                symbl.setEnabled(False) 
        for symbl in MTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(False)
        for symbl in MTD_SRC_FILE_SYMBOLS:
            symbl.setEnabled(False)
        openthreadmtdLibraryEnable.setEnabled(False)
        for symbl in RCP_FILE_SYMBOLS:
            symbl.setEnabled(False)
    elif DeviceType == "MTD":
        for symbl in FTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(False)
        for symbl in FTD_SRC_FILE_SYMBOLS:
            symbl.setEnabled(False)
        openthreadftdLibraryEnable.setEnabled(False)
        for symbl in MTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(True)
        if openthreadlibraryGen.getSelectedKey() == "Source":
            for symbl in MTD_SRC_FILE_SYMBOLS:
                symbl.setEnabled(True)
            openthreadmtdLibraryEnable.setEnabled(False)
        elif openthreadlibraryGen.getSelectedKey() == "Library":
            openthreadmtdLibraryEnable.setEnabled(True)
            for symbl in FTD_SRC_FILE_SYMBOLS:
                symbl.setEnabled(False) 
            for symbl in MTD_SRC_FILE_SYMBOLS:
                symbl.setEnabled(False)
        for symbl in RCP_FILE_SYMBOLS:
            symbl.setEnabled(False)
    elif DeviceType == "RCP":
        for symbl in FTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(False)
        for symbl in FTD_SRC_FILE_SYMBOLS:
            symbl.setEnabled(False)
        for symbl in MTD_HDR_FILE_SYMBOLS:
            symbl.setEnabled(False)
        for symbl in MTD_SRC_FILE_SYMBOLS:
            symbl.setEnabled(False)
        openthreadftdLibraryEnable.setEnabled(False)
        openthreadmtdLibraryEnable.setEnabled(False)
        for symbl in RCP_FILE_SYMBOLS:
            symbl.setEnabled(True)
            

def HandleTcpFileSymbols(Enable):
    Value = False
    for symbls in TCP_HDR_FILE_SYMBOLS:
        symbls.setEnabled(Enable)
    if Enable == True and openthreadlibraryGen.getSelectedKey() == "Source":
        Value = True
    for symbls in TCP_SRC_FILE_SYMBOLS:
        symbls.setEnabled(Value)
        
def HandleCommonFileSymbols(Enable):
    Value = False
    for symbls in COMMON_HDR_FILE_SYMBOLS:
        symbls.setEnabled(Enable)
    
    if openthreadDevicerole.getValue() == "RCP":
        Value = True
    elif Enable == True and openthreadlibraryGen.getSelectedKey() == "Source":
        Value = True
    for symbls in COMMON_SRC_FILE_SYMBOLS:
        symbls.setEnabled(Value)

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD COMPILER HANDLING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------


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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD MCC CALLBACKS ~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
def HandleUsartResourceAllocation(DeviceType,logEnable):
    # componentids = Database.getActiveComponentIDs()
    if DeviceType == "FTD" or DeviceType == "MTD":
        if (Database.getSymbolValue("THREAD_CLI","OPEN_THREAD_CLI_UART_SYM") == True):#("OPEN_THREAD_CLI" in componentids):
            # print("HandleUsartResourceAllocation")
            localComponent.setDependencyEnabled("OT_CONSOLE_dependency", False)
            if openthreadUartConfig.getValue() == False:
                openthreadUartConfig.setValue(True)
        else:
            openthreadUartConfig.setValue(False)
            localComponent.setDependencyEnabled("OT_USART_dependency",False)
            
            # if openthreadLogEnable.getValue() == True:
                # requiredComponent = ["SYS_CONSOLE"]
                # openthreadUartConfig.setValue(True)
                # localComponent.setDependencyEnabled("OT_CONSOLE_dependency", True)
                # if "SYS_CONSOLE" not in componentids: 
                    # Database.activateComponents(requiredComponent)


def HandleLibConfigurationOptions(EnableLibrary):
    if EnableLibrary == True:
        openthreadmtdconfigMenu.setVisible(False)
        openthreadrcpconfigMenu.setVisible(False)
        openthreadftdconfigMenu.setVisible(False)
        openthreadTcpEnableConfig.setVisible(False)
        openthreadCoapBlockEnable.setVisible(False)
        openthreadloglevelconfig.setVisible(False)
        openthreadLogEnable.setVisible(True)
    else:
        HandleDeviceConfigOptions(openthreadDevicerole.getValue())
    


def HandleDeviceConfigOptions(DeviceType):
    if DeviceType == "FTD":
        openthreadlibraryGen.setVisible(True)
        if openthreadlibraryGen.getSelectedKey() == "Source":
            openthreadmtdconfigMenu.setVisible(False)
            openthreadrcpconfigMenu.setVisible(False)
            openthreadftdconfigMenu.setVisible(True)
            openthreadLogEnable.setVisible(True)
            if openthreadLogEnable.getValue() == True:
                openthreadloglevelconfig.setVisible(True)
            if openthreadUartParser.getValue() == True:
                openthreadcomment1.setVisible(True)
            else:
                openthreadcomment1.setVisible(False)
            openthreadTcpEnableConfig.setVisible(True)
            openthreadCoapBlockEnable.setVisible(True)
        elif openthreadlibraryGen.getSelectedKey() == "Library":
            HandleLibConfigurationOptions(True)
        # Database.setSymbolValue("IEEE_802154_PHY","CREATE_PHY_SEMAPHORE",True)
           
           
    elif DeviceType == "MTD":
        openthreadlibraryGen.setVisible(True)
        if openthreadlibraryGen.getSelectedKey() == "Source":
            openthreadftdconfigMenu.setVisible(False)
            openthreadrcpconfigMenu.setVisible(False)
            openthreadmtdconfigMenu.setVisible(True)
            for symb in MTD_OPTION_SYMBOLS:
                    symb.setVisible(True)
            if openthreadUartParser.getValue() == True:
                openthreadmtdsleepEnable.setValue(False)
                openthreadmtdsleepEnable.setReadOnly(True)
            if openthreadmtdInBandCommissioningConfig.getValue() == False:
                openthreadmtdJoinerEnable.setVisible(False)
            openthreadLogEnable.setVisible(True)
            if openthreadLogEnable.getValue() == True:
                openthreadloglevelconfig.setVisible(True)
            if openthreadUartParser.getValue() == True:
                openthreadcomment1.setVisible(True)
            else:
                openthreadcomment1.setVisible(False)
            openthreadTcpEnableConfig.setVisible(True)
            openthreadCoapBlockEnable.setVisible(True)
        elif openthreadlibraryGen.getSelectedKey() == "Library":
            HandleLibConfigurationOptions(True)
            if openthreadUartParser.getValue() == False:
                for symb in MTD_OPTION_SYMBOLS:
                    symb.setVisible(False)
                openthreadmtdconfigMenu.setVisible(True)
                openthreadmtdsleepEnable.setVisible(True)
                openthreadmtdsleepEnable.setReadOnly(False)
        # Database.setSymbolValue("IEEE_802154_PHY","CREATE_PHY_SEMAPHORE",True)
        
        
    elif DeviceType == "RCP":
        HandleLibConfigurationOptions(True)
        openthreadlibraryGen.setVisible(False)
        openthreadrcpconfigMenu.setVisible(True)
        openthreadLogEnable.setVisible(False)
        # Database.setSymbolValue("IEEE_802154_PHY","CREATE_PHY_SEMAPHORE",True)
        
    #Checks and Handles Usart Resource based on Config
    HandleUsartResourceAllocation(DeviceType,openthreadLogEnable.getValue())
    
####################################################################################
####################Core Configuration Callback######################################
####################################################################################
def openthreadcoreconfigcallback(symbol,event):
    remotesymbol = event["symbol"]
    symbolID = event["id"]
    value = event["value"]
    global localComponent
    localComponent = symbol.getComponent()
    # print("openthreadconfigcallback",symbol,event)
    if symbolID == "OPEN_THREAD_DEVICE_ROLE_CONFIG_1":
        if value == 0:
            openthreadDevicerole.setValue("FTD")
            
        elif value == 1:
            openthreadDevicerole.setValue("MTD")
                
        elif value == 2:
            openthreadDevicerole.setValue("RCP")
    
    elif symbolID == "OPEN_THREAD_DEVICE_ROLE":
        if value == "FTD":
            HandleDeviceConfigOptions("FTD")
            #Enable File Symbols
            EnableFileSymbls("FTD")
            if openthreadTcpEnableConfig.getValue() == False:
                HandleTcpFileSymbols(False)
            else:
                HandleTcpFileSymbols(True)
            HandleCommonFileSymbols(True)
            
        elif value == "MTD":
            HandleDeviceConfigOptions("MTD")
            #Enable File Symbols
            EnableFileSymbls("MTD")
            if openthreadTcpEnableConfig.getValue() == False:
                HandleTcpFileSymbols(False)
            else:
                HandleTcpFileSymbols(True)
            HandleCommonFileSymbols(True)
            
        elif value == "RCP":
            HandleDeviceConfigOptions("RCP")
            if openthreadUartConfig.getValue() == False:
                openthreadUartConfig.setValue(True)
            #Enable File Symbols
            EnableFileSymbls("RCP")
            openthreadUartParser.setValue(False)
            HandleTcpFileSymbols(False)
            HandleCommonFileSymbols(True)

    
    elif symbolID == "OPEN_THREAD_LOG_SYMBOL":
        if value == True:
            openthreadloglevelconfig.setVisible(True)
            if openthreadUartConfig.getValue() == False:
                # openthreadUartConfig.setValue(True)
                localComponent.setDependencyEnabled("OT_USART_Dependency",False)
                EnableConsoleDependency()
        elif value == False:
            openthreadloglevelconfig.setVisible(False)
            #HandleUsartResourceAllocation(openthreadDevicerole.getValue(),False)
            localComponent.setDependencyEnabled("OT_CONSOLE_dependency", False)
            
            
    elif symbolID == "OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG":
        # openthreadroleconfig2.setValue(remotesymbol.getSelectedKey())
        openthreadroleconfig1.setValue(Database.getSymbolValue("THREAD_CLI","OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG"))
    
    elif symbolID == "OPEN_THREAD_TCP_ENABLE_CONFIG":
        if value == True:
            HandleTcpFileSymbols(True)
        elif value == False:
            HandleTcpFileSymbols(False)


def openthreadFileGenerationCallback(symbol,event):
    symbolID = event["id"]
    value = event["value"]
    global localComponent
    localComponent = symbol.getComponent()
    
    if symbolID == "OPEN_THREAD_LIBRARY_GENERATION":
        if value == True:
            HandleLibConfigurationOptions(True)
            EnableFileSymbls(openthreadDevicerole.getValue())
            HandleTcpFileSymbols(True)
            HandleCommonFileSymbols(True)
        else:
            HandleLibConfigurationOptions(False)
            EnableFileSymbls(openthreadDevicerole.getValue())
            if openthreadTcpEnableConfig.getValue() == False:
                HandleTcpFileSymbols(False)
            HandleCommonFileSymbols(True)
 
####################################################################################
####################System Configuration Callback###################################
####################################################################################

def HandleUsartDependencies(Enable):
    # openthreadApphData.setEnabled(Enable)
    # openthreadAppcData1.setEnabled(Enable)
    # openthreadAppcData2.setEnabled(Enable)
    # openthreadAppcData3.setEnabled(Enable)
    openthreadserialparsing.setValue(Enable)
    
def EnableConsoleDependency():
    componentids = Database.getActiveComponentIDs()
    requiredComponent = ["sys_console"]
    # openthreadUartConfig.setValue(True)
    localComponent.setDependencyEnabled("OT_CONSOLE_dependency", True)
    if "sys_console" not in componentids: 
        Database.activateComponents(requiredComponent)
    Database.connectDependencies([['OPEN_THREAD','OT_CONSOLE_dependency','sys_console_0','sys_console']])


def openthreadSystemconfigcallback(symbol,event):
    # print(symbol,event)
    symbolID = event["id"]
    value = event["value"]
    global localComponent
    localComponent = symbol.getComponent()
    componentids = Database.getActiveComponentIDs()
    requiredComponent = ["drv_usart"]
    # print("componentids:",componentids)
    if symbolID == "OPEN_THREAD_UART_SERVICE":
        if value == True:
            localComponent.setDependencyEnabled("OT_CONSOLE_dependency", False)
            if "drv_usart" not in componentids: 
                Database.activateComponents(requiredComponent)
            componentids = Database.getActiveComponentIDs()
            localComponent.setDependencyEnabled("OT_USART_dependency",True)
            Database.connectDependencies([['OPEN_THREAD','OT_USART_dependency','drv_usart_0','drv_usart']])
            if Database.getSymbolValue("drv_usart","DRV_USART_COMMON_MODE") != "Asynchronous":
                Database.setSymbolValue("drv_usart", "DRV_USART_COMMON_MODE", "Asynchronous")
            HandleUsartDependencies(True)
                
        elif value == False:
            # if openthreadroleconfig1.getValue() != "RCP":
            if "drv_usart" in componentids: 
                Database.deactivateComponents(requiredComponent)
                print("componentids",componentids)
                # Database.connectDependencies(["OPEN_THREAD","OT_USART_Dependency","drv_usart","DRV_USART"])
            # openthreadserialparsing.setValue(False)
            HandleUsartDependencies(False)
            if openthreadLogEnable.getValue() == True:
                EnableConsoleDependency()
            # else:
                # openthreadUartConfig.setValue(True)
    elif symbolID == "SYS_CONSOLE_DEVICE":
        print("componentids",componentids)
        if value != "":
            print("SercomConnectedCallback",value)
            global uartTxRingBufferSym
            uartTxRingBufferSym = Database.getComponentByID(value.lower()).getSymbolByID("USART_TX_RING_BUFFER_SIZE")
            uartTxRingBufferSym.setValue(1024)
            uartTxRingBufferSym.setReadOnly(True)
        else:
            uartTxRingBufferSym.setReadOnly(False)
        
    elif symbolID == "SYS_TIME_PLIB":
        if value != "":
            global TcPrescalerSymbol
            TcPrescalerSymbol = Database.getComponentByID(value.lower()).getSymbolByID("TC_CTRLA_PRESCALER")
            print("Tc0Callback",value)
            TcPrescalerSymbol.setValue(5)
            TcPrescalerSymbol.setReadOnly(True)
        else:
            TcPrescalerSymbol.setReadOnly(False)

####################################################################################
####################Open Thread Parser Callback###################################
####################################################################################        

def openthreadParserUpdateCallback(symbol,event):
    # print("openthreadParserUpdateCallback",symbol,event)
    TcpEnabled = 0
    symbolID = event["id"]
    value = event["value"]
    if symbolID == "OPEN_THREAD_CLI_UART_SYM":
        if value == True:
            openthreadcomment1.setVisible(True)
            openthreadUartParser.setValue(True)
            # openthreadroleconfig1.setValue(Database.getComponentByID("THREAD_CLI").getSymbolByID("OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG").getValue())
            openthreadroleconfig1.setReadOnly(True)
            # print("openthreadroleconfig2.getKey()",openthreadroleconfig2.getSelectedKey())
            openthreadDevicerole.setValue(str(openthreadroleconfig1.getSelectedKey()))
            #Disable Sleep Option in MTD config while CLI Enabled
            if openthreadmtdsleepEnable.getValue() == True:
                openthreadmtdsleepEnable.setValue(False)
            openthreadmtdsleepEnable.setReadOnly(True)
            
        elif value == False:
            openthreadcomment1.setVisible(False)
            openthreadUartParser.setValue(False)
            openthreadroleconfig1.setReadOnly(False)
            # print("openthreadroleconfig1.getKey()",openthreadroleconfig1.getSelectedKey())
            openthreadDevicerole.setValue(str(openthreadroleconfig1.getSelectedKey()))
            #Re Enable Sleep Option in MTD config while CLI Disbaled
            openthreadmtdsleepEnable.setReadOnly(False)

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD FTD CALLBACKS ~~~~~~~~~~~~~~~~~~~~~~
#------------------------------------------------------------------------------- 
        
def openthreadFtdConfigcallback(symbol,event):
    # print("openthreadFtdConfigcallback",symbol,event)
    symbolID = event["id"]
    value = event["value"]
    
    if symbolID == "OPEN_THREAD_FTD_IN_BAND_COMMISSIONING_CONFIG":
        if value == True:
            openthreadftdJoinerEnable.setVisible(True)
            openthreadftdCommissionerEnable.setVisible(True)
            
        elif value == False:
            openthreadftdJoinerEnable.setVisible(False)
            openthreadftdCommissionerEnable.setVisible(False)

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPEN THREAD MTD CALLBACKS ~~~~~~~~~~~~~~~~~~~~~~
#------------------------------------------------------------------------------- 

def openthreadMtdConfigcallback(symbol,event):
    # print("openthreadMtdConfigcallback",symbol,event)
    symbolID = event["id"]
    value = event["value"]
    
    if symbolID == "OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG":
        if value == True:
            openthreadmtdJoinerEnable.setVisible(True)
            
        elif value == False:
            openthreadmtdJoinerEnable.setVisible(False)
            
    elif symbolID == "OPEN_THREAD_MTD_SLEEP_ENABLE":
        if value == True:
            Database.setSymbolValue("pic32cx_bz2_devsupport","ENABLE_DEEP_SLEEP",True)
        elif value == False:
            Database.setSymbolValue("pic32cx_bz2_devsupport","ENABLE_DEEP_SLEEP",False)
            
    # elif symbolID == "OPEN_THREAD_MTD_JOINER_ENABLE":
        # if value == False:
            # print("openthread_component.clearSymbolValue('OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG')")
            # openthreadmtdInBandCommissioningConfig.setValue(False)
            # Database.clearSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_IN_BAND_COMMISSIONING_CONFIG")
            # Database.clearSymbolValue("OPEN_THREAD","OPEN_THREAD_MTD_JOINER_ENABLE")
        
        
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
global deviceName
deviceName = Variables.get("__PROCESSOR")

def instantiateComponent(openthread):
    global openthread_component
    openthread_component = openthread
    print("Open Thread driver component")
    #Disable UART and Log  Dependencies until Parser or Log is enabled
    openthread.setDependencyEnabled("OT_USART_dependency", False)
    openthread.setDependencyEnabled("OT_CONSOLE_dependency", False)
    
    global src_path1
    global src_path2
    if deviceName in pic32cx_bz2_family:
        src_path1 = 'driver/src/stack/pic32cx_bz2/src'
        src_path2 = 'driver/src/stack/pic32cx_bz2/src/crypto'
    
    #Parse open thread File System
    # ParseOpenThreadFileSystem()
    execfile(Module.getPath() + '/driver/config/stack/openthread_filesystem_Parser.py')
    
    # print("***********************************************")
    # print("\tOpen Thread File System")
    # print("***********************************************")
    # for i in range(len(openthreadfileRecords)):
        # print(openthreadfileRecords[i])
        # print('\n')
    # print("***********************************************")
    
    global configName
    configName = Variables.get("__CONFIGURATION_NAME")
    # print configName
    
    global requiredComponents
    requiredComponents = [
        "IEEE_802154_PHY",
        "sys_time",
        "FreeRTOS",
        "trng",
        "rcon",
        "lib_wolfcrypt",
        "pic32cx_bz2_devsupport",
        "lib_crypto"
    ]
    
    for component in requiredComponents:
        res = Database.activateComponents([component])
    
   
    
    remoteComponent = Database.getComponentByID("trng")
    if (remoteComponent):
        # print('Printing TRNG remoteComponent Value')
        # print(remoteComponent)
        symbol = remoteComponent.getSymbolByID("trngEnableInterrupt")
        symbol1 = remoteComponent.getSymbolByID("trngEnableEvent")
        symbol2 = remoteComponent.getSymbolByID("TRNG_STANDBY")
        # print('Printing TRNG Symbol Value')
        # print(symbol)
        symbol.setReadOnly(True)
        symbol1.setReadOnly(True)
        symbol2.setReadOnly(True)
    #Database.setSymbolValue("trng", "trngEnableInterrupt", True)
    #Database.setSymbolValue("trng", "trngEnableEvent", True)
    #Database.setSymbolValue("trng", "TRNG_STANDBY", True)
    Database.setSymbolValue("core", "AES_CLOCK_ENABLE", True)

    Database.setSymbolValue("core", "ZIGBEE_CLOCK_ENABLE", True)
    # Database.setSymbolValue("core", "CONFIG_SCOM0_HSEN", "DIRECT")
    
    # print(openthreadfileRecords)
    
    #############################################################################
    ## Thread Core Config options
    #############################################################################
    global openthreadcoreconfig
    openthreadcoreconfig = openthread.createMenuSymbol("OPEN_THREAD_CORE_MENU_SYMBOL", None)
    openthreadcoreconfig.setLabel("Thread config")
    openthreadcoreconfig.setVisible(True)
    
    #Non Cli Device Role Config
    global openthreadroleconfig1
    openthreadroleconfig1 = openthread.createKeyValueSetSymbol("OPEN_THREAD_DEVICE_ROLE_CONFIG_1", openthreadcoreconfig)
    openthreadroleconfig1.setLabel("Device Role")
    openthreadroleconfig1.addKey("FTD", "FTD", "FTD")
    openthreadroleconfig1.addKey("MTD", "MTD", "MTD")
    openthreadroleconfig1.addKey("RCP", "RCP", "RCP")
    openthreadroleconfig1.setDefaultValue(0)
    openthreadroleconfig1.setOutputMode("Value")
    openthreadroleconfig1.setDisplayMode("Description")
    openthreadroleconfig1.setDescription("Open Thread Device Role Configuration")
    openthreadroleconfig1.setVisible(True)
    openthreadroleconfig1.setReadOnly(False)
    openthreadroleconfig1.setDependencies(openthreadcoreconfigcallback,["OPEN_THREAD_DEVICE_ROLE_CONFIG_1","THREAD_CLI.OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG"])
    
    global openthreadlibraryGen
    openthreadlibraryGen = openthread.createKeyValueSetSymbol("OPEN_THREAD_LIBRARY_GENERATION",openthreadcoreconfig)
    openthreadlibraryGen.setLabel("Thread Generation")
    openthreadlibraryGen.addKey("Source","Source","Source")
    openthreadlibraryGen.addKey("Library","Library","Library")
    openthreadlibraryGen.setDefaultValue(0)
    openthreadlibraryGen.setVisible(True)
    openthreadlibraryGen.setDependencies(openthreadFileGenerationCallback,["OPEN_THREAD_LIBRARY_GENERATION"])
    
    #Cli Device Role Config
    # global openthreadroleconfig2
    # openthreadroleconfig2 = openthread.createKeyValueSetSymbol("OPEN_THREAD_DEVICE_ROLE_CONFIG_2", openthreadcoreconfig)
    # openthreadroleconfig2.setLabel("Device Role")
    # openthreadroleconfig2.addKey("FTD", "FTD", "FTD")
    # openthreadroleconfig2.addKey("MTD", "MTD", "MTD")
    # openthreadroleconfig2.setDefaultValue(0)
    # openthreadroleconfig2.setOutputMode("Value")
    # openthreadroleconfig2.setDisplayMode("Description")
    # openthreadroleconfig2.setDescription("Open Thread Device Role Configuration")
    # openthreadroleconfig2.setVisible(False)
    # openthreadroleconfig2.setReadOnly(True)
    # openthreadroleconfig2.setDependencies(openthreadcoreconfigcallback,["OPEN_THREAD_DEVICE_ROLE_CONFIG_2"])
    
    global openthreadcomment1
    openthreadcomment1 = openthread.createCommentSymbol("OPEN_THREAD_COMMENT_1",openthreadcoreconfig)
    # openthreadcomment1.setLabel("Enable Thread UART Parser")
    openthreadcomment1.setLabel("*****CLI is not supported with RCP*****")
    openthreadcomment1.setVisible(False)
    
    #############################################################################
    ## Thread Device Type Specific Handling
    #############################################################################
    
    execfile(Module.getPath() + '/driver/config/stack/openthread_ftd.py')
    
    execfile(Module.getPath() + '/driver/config/stack/openthread_mtd.py')
    
    execfile(Module.getPath() + '/driver/config/stack/openthread_rcp.py')
    
   #Enable FTD File Symbols --> Default Role = FTD
    EnableFileSymbls("FTD")
    
    #############################################################################
    
    #Device Role Config for FTL
    global openthreadDevicerole
    openthreadDevicerole = openthread.createStringSymbol("OPEN_THREAD_DEVICE_ROLE",None)
    openthreadDevicerole.setLabel("Device Role")
    openthreadDevicerole.setDefaultValue("FTD")
    openthreadDevicerole.setVisible(False)
    openthreadDevicerole.setDependencies(openthreadcoreconfigcallback,["OPEN_THREAD_DEVICE_ROLE"])
    
    global openthreadUartConfig
    openthreadUartConfig = openthread.createBooleanSymbol("OPEN_THREAD_UART_SERVICE",openthreadcoreconfig)
    openthreadUartConfig.setLabel("Enable Thread UART")
    openthreadUartConfig.setDefaultValue(0)
    openthreadUartConfig.setVisible(False)
    openthreadUartConfig.setDescription("Open Thread System Configuration")
    openthreadUartConfig.setDependencies(openthreadSystemconfigcallback,["OPEN_THREAD_UART_SERVICE","sys_console_0:SYS_CONSOLE_DEVICE","sys_time:SYS_TIME_PLIB"])


    global openthreadUartParser
    openthreadUartParser = openthread.createBooleanSymbol("OPEN_THREAD_UART_PARSER",openthreadcoreconfig)
    openthreadUartParser.setLabel("Enable Thread UART Parser")
    openthreadUartParser.setDefaultValue(0)
    openthreadUartParser.setVisible(False)
    openthreadUartParser.setDescription("Open Thread Serial Parser")
    openthreadUartParser.setDependencies(openthreadParserUpdateCallback,["THREAD_CLI.OPEN_THREAD_CLI_UART_SYM",'OPEN_THREAD_UART_PARSER'])
        
    
    # openthreadcomment1.setDescription("Open Thread Serial Parser")
    
    #Boolean symbol to generate the APP code through Device Support library 
    global openthreadserialparsing
    openthreadserialparsing = openthread.createBooleanSymbol("OPEN_THREAD_ENABLE_SERIAL_PARSING", None)
    openthreadserialparsing.setLabel("Enable Command Parsing")
    openthreadserialparsing.setDefaultValue(False)
    openthreadserialparsing.setVisible(False)
    # openthreadserialparsing.setDependencies(openthreadcliParserCallback,["OPEN_THREAD_CLI.OPEN_THREAD_CLI_UART_SYM"])
    
    global openthreadLogEnable
    openthreadLogEnable = openthread.createBooleanSymbol("OPEN_THREAD_LOG_SYMBOL",openthreadcoreconfig)
    openthreadLogEnable.setLabel("Enable Thread Log")
    openthreadLogEnable.setDefaultValue(0)
    openthreadLogEnable.setVisible(True)
    openthreadLogEnable.setDescription("Open Thread Serial Log")
    openthreadLogEnable.setDependencies(openthreadcoreconfigcallback,['OPEN_THREAD_LOG_SYMBOL'])
    
    global openthreadloglevelconfig
    openthreadloglevelconfig = openthread.createKeyValueSetSymbol("OPEN_THREAD_LOG_LEVEL_CONFIG", openthreadcoreconfig)
    openthreadloglevelconfig.setLabel("Log Level")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_NONE", "OT_LOG_LEVEL_NONE", "OT_LOG_LEVEL_NONE")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_CRIT", "OT_LOG_LEVEL_CRIT", "OT_LOG_LEVEL_CRIT")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_WARN", "OT_LOG_LEVEL_WARN", "OT_LOG_LEVEL_WARN")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_NOTE", "OT_LOG_LEVEL_NOTE", "OT_LOG_LEVEL_NOTE")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_INFO", "OT_LOG_LEVEL_INFO", "OT_LOG_LEVEL_INFO")
    openthreadloglevelconfig.addKey("OT_LOG_LEVEL_DEBG", "OT_LOG_LEVEL_DEBG", "OT_LOG_LEVEL_DEBG")
    openthreadloglevelconfig.setDefaultValue(0)
    openthreadloglevelconfig.setOutputMode("Value")
    openthreadloglevelconfig.setDisplayMode("Description")
    openthreadloglevelconfig.setDescription("Open Thread Device Role Configuration")
    openthreadloglevelconfig.setVisible(False)
    # openthreadloglevelconfig.setDependencies(openthreadcoreconfigcallback,["OPEN_THREAD_LOG_SYMBOL"])
    
    global openthreadTcpEnableConfig
    openthreadTcpEnableConfig = openthread.createBooleanSymbol("OPEN_THREAD_TCP_ENABLE_CONFIG",openthreadcoreconfig)
    openthreadTcpEnableConfig.setLabel("Enable TCP")
    openthreadTcpEnableConfig.setDefaultValue(0)
    openthreadTcpEnableConfig.setVisible(True)
    openthreadTcpEnableConfig.setDescription("Open Thread TCP Enable")
    openthreadTcpEnableConfig.setDependencies(openthreadcoreconfigcallback,['OPEN_THREAD_TCP_ENABLE_CONFIG'])
    
    global openthreadCoapBlockEnable
    openthreadCoapBlockEnable = openthread.createBooleanSymbol("OPEN_THREAD_COAP_BLOCK_TRANSFER_ENABLE",openthreadcoreconfig)
    openthreadCoapBlockEnable.setLabel("Coap Block Transfer")
    openthreadCoapBlockEnable.setDefaultValue(0)
    openthreadCoapBlockEnable.setVisible(True)
    openthreadCoapBlockEnable.setDescription("Open Thread Coap Block Transfer Enable")
    
    
    #############################################################################
    ## Thread Common File Symbols Handling
    #############################################################################
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
    
    #common File includes paths
    global commonincpath
    commonincpath   =   [['openthread/third_party/mbedtls',False],
                         ['openthread/third_party/mbedtls/repo/configs',False],
                         ['openthread/third_party/mbedtls/repo/include/mbedtls',False],
                         ['openthread/third_party/mbedtls/repo/include/psa',False],
                         ['openthread/third_party/mbedtls/repo/library',False],
                         ['openthread/include/openthread',True],
                         ['openthread/examples/platforms/utils',False,["logging_rtt.h","logging_rtt.c"],False],
                         ['openthread/examples/platforms',False]
                        ]
    
    hdrFileSymbls,srcFileSymbls = importfiles(openthread,commonincpath,True) 
    
    for symb in hdrFileSymbls:
        COMMON_HDR_FILE_SYMBOLS.append(symb)
        
    for symb in srcFileSymbls:
        COMMON_SRC_FILE_SYMBOLS.append(symb)
    
    global palincpath
    palincpath    =  [['driver/src/stack/pic32cx_bz2/src',False,[],False,'inc','src'],
                         ['driver/src/stack/pic32cx_bz2/src/crypto',False,[],False,'inc/crypto','src/crypto']
                     ]
    
    hdrFileSymbls,srcFileSymbls = importfiles(openthread,palincpath,True)
    
    for symb in hdrFileSymbls:
        PAL_HDR_FILE_SYMBOLS.append(symb)
        
    for symb in srcFileSymbls:
        PAL_SRC_FILE_SYMBOLS.append(symb)
    
    # Database.setSymbolValue('pic32cx_bz2_devsupport','ZIGBEESTACK_LOADED','OPEN_THREAD')
    
    global openthreadTypesHFile
    openthreadTypesHFile = openthread.createFileSymbol('OPEN_THREAD_TYPES_H',None)
    openthreadTypesHFile.setSourcePath("/driver/src/stack/include/types.h")
    openthreadTypesHFile.setOutputName("types.h")
    openthreadTypesHFile.setDestPath('driver/thread/inc')
    openthreadTypesHFile.setProjectPath('config/'+configName+'/driver/thread/inc/types.h')
    openthreadTypesHFile.setType("HEADER")
    openthreadTypesHFile.setOverwrite(True)
    openthreadTypesHFile.setMarkup(True)
    openthreadTypesHFile.setEnabled(False)
    
    global openthreadStringsHFile
    openthreadStringsHFile = openthread.createFileSymbol('OPEN_THREAD_STRINGS_H',None)
    openthreadStringsHFile.setSourcePath("/driver/src/stack/include/strings.h")
    openthreadStringsHFile.setOutputName("strings.h")
    openthreadStringsHFile.setDestPath('driver/thread/inc')
    openthreadStringsHFile.setProjectPath('config/'+configName+'/driver/thread/inc/strings.h')
    openthreadStringsHFile.setType("HEADER")
    openthreadStringsHFile.setOverwrite(True)
    openthreadStringsHFile.setMarkup(True)
    openthreadStringsHFile.setEnabled(False)
    
    TCPFiles = [openthreadTypesHFile,openthreadStringsHFile]
    
    #TCP Files include paths
    global TcpIncPath
    TcpIncPath     =  [['openthread/third_party/tcplp',False],
                       ['openthread/third_party/tcplp/bsdtcp',False,["types.h"],False],
                       ['openthread/third_party/tcplp/bsdtcp/cc',False],
                       ['openthread/third_party/tcplp/bsdtcp/sys',False],
                       ['openthread/third_party/tcplp/lib',False]
                      ]
    
    Tcphdrfilesymb,TcpSrcfilesymb = importfiles(openthread,TcpIncPath,False)
    for symbl in Tcphdrfilesymb:
        TCP_HDR_FILE_SYMBOLS.append(symbl)
    TCP_HDR_FILE_SYMBOLS.extend(TCPFiles)
    
    for symbl in TcpSrcfilesymb:
        TCP_SRC_FILE_SYMBOLS.append(symbl)
    
    #############################################################################
    ## Thread FTL Handlings
    #############################################################################
    
    global openthreadtaskCFile
    openthreadtaskCFile = openthread.createFileSymbol('OPEN_THREAD_TASK_C',None)
    openthreadtaskCFile.setSourcePath("/driver/templates/stack/ot_tasks.c.ftl")
    openthreadtaskCFile.setOutputName("ot_tasks.c")
    openthreadtaskCFile.setDestPath('driver/thread/src')
    openthreadtaskCFile.setProjectPath('config/'+configName+'/driver/thread/src/ot_tasks.c')
    openthreadtaskCFile.setType("SOURCE")
    openthreadtaskCFile.setOverwrite(True)
    openthreadtaskCFile.setMarkup(True)
    
    global openthreadMbedtlsconfig
    openthreadMbedtlsconfig = openthread.createFileSymbol('OPEN_THREAD_MBEDTLS_CONFIG',None)
    openthreadMbedtlsconfig.setSourcePath("/driver/templates/stack/openthread-mbedtls-config.h.ftl")
    openthreadMbedtlsconfig.setOutputName("openthread-mbedtls-config.h")
    openthreadMbedtlsconfig.setDestPath('driver/thread/inc')
    openthreadMbedtlsconfig.setProjectPath('config/'+configName+'/driver/thread/inc/openthread-mbedtls-config.h')
    openthreadMbedtlsconfig.setType("HEADER")
    openthreadMbedtlsconfig.setOverwrite(True)
    openthreadMbedtlsconfig.setMarkup(True)
    
    #############################################################################
    ## Thread Prepocessor Directives Include paths
    #############################################################################
    
    #Include Directories
    global commonIncPaths
    commonIncPaths = [#"/examples/platforms",
                      #"/examples/platforms/utils",
                      "/openthread/include",
                      "/openthread/src",
                      "/openthread/src/core",
                      "opethread/src/ncp",
                      "/openthread/third_party/mbedtls/repo/include",
                      "/openthread/third_party/mbedtls/repo/library",
                      "/openthread/third_party/tcplp",
                      "/openthread/third_party/tcplp/bsdtcp",
                      "/openthread/third_party/tcplp/lib",
                      "/openthread/third_party/tcplp/bsdtcp/cc",
                      "/openthread/examples/platforms",
                      "/openthread/examples/platforms/utils",
                      "/inc",
                      "/inc/crypto",
                      "/src",
                      "/src/crypto"
                      ]
                      
    setIncPath(openthread,commonIncPaths)
    
    #############################################################################
    ## Thread App.c/App.h File Symbols
    #############################################################################
    # global openthreadApphData
    # openthreadApphData = openthread.createFileSymbol('OPEN_THREAD_APP_H_DATA', None)
    # openthreadApphData.setType('STRING')
    # openthreadApphData.setOutputName('pic32cx_bz2_devsupport.LIST_DS_THREAD_APPH_MSG_ID_1')
    # openthreadApphData.setSourcePath('driver/templates/stack/OTMsgIdFile.h.ftl')
    # openthreadApphData.setMarkup(True)
    # openthreadApphData.setEnabled(False)
    
    # global openthreadAppcData1
    # openthreadAppcData1 = openthread.createFileSymbol('OPEN_THREAD_APP_C_DATA_1', None)
    # openthreadAppcData1.setType('STRING')
    # openthreadAppcData1.setOutputName('pic32cx_bz2_devsupport.LIST_DS_THREAD_APPC_MSG_ID_1')
    # openthreadAppcData1.setSourcePath('driver/templates/stack/OTMsgIdFile2.c.ftl')
    # openthreadAppcData1.setMarkup(True)
    # openthreadAppcData1.setEnabled(False)
    
    # global openthreadAppcData2
    # openthreadAppcData2 = openthread.createFileSymbol('OPEN_THREAD_APP_C_DATA_2', None)
    # openthreadAppcData2.setType('STRING')
    # openthreadAppcData2.setOutputName('pic32cx_bz2_devsupport.LIST_DS_THREAD_APPC_MSG_ID_2')
    # openthreadAppcData2.setSourcePath('driver/templates/stack/OTMsgIdFile1.c.ftl')
    # openthreadAppcData2.setMarkup(True)
    # openthreadAppcData2.setEnabled(False)
    
    # global openthreadAppcData3
    # openthreadAppcData3 = openthread.createFileSymbol('OPEN_THREAD_APP_C_DATA_3', None)
    # openthreadAppcData3.setType('STRING')
    # openthreadAppcData3.setOutputName('pic32cx_bz2_devsupport.LIST_DS_THREAD_APPC_MSG_ID_3')
    # openthreadAppcData3.setSourcePath('driver/templates/stack/OTMsgIdFile3.c.ftl')
    # openthreadAppcData3.setMarkup(True)
    # openthreadAppcData3.setEnabled(False)
    
    ##########################################################################################
    ## Thread Initialization code File Symbols
    #########################################################################################
    
    openthreadinitData = openthread.createFileSymbol('OPEN_THREAD_INITIALIZATION_DATA', None)
    openthreadinitData.setType('STRING')
    openthreadinitData.setOutputName('core.LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA')
    openthreadinitData.setSourcePath('driver/templates/system/system_initialize_data.c.ftl')
    openthreadinitData.setMarkup(True)
    
    openthreadQinit = openthread.createFileSymbol('OPEN_THREAD_INITIALIZATION_C', None)
    openthreadQinit.setType('STRING')
    openthreadQinit.setOutputName('core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE')
    openthreadQinit.setSourcePath('driver/templates/system/system_initialize_middleware.c.ftl')
    openthreadQinit.setMarkup(True)
    
    openthreadTasksC = openthread.createFileSymbol('OPEN_THREAD_TASKS_C', None)
    openthreadTasksC.setType('STRING')
    openthreadTasksC.setOutputName('core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS')
    openthreadTasksC.setSourcePath('driver/templates/system/system_tasks.c.ftl')
    openthreadTasksC.setMarkup(True)
    
    openthreadTasksDefC = openthread.createFileSymbol('OPEN_THREAD_TASK_INITIALIZATION_C', None)
    openthreadTasksDefC.setType('STRING')
    openthreadTasksDefC.setOutputName('core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS')
    openthreadTasksDefC.setSourcePath('driver/templates/system/system_tasks_def.c.ftl')
    openthreadTasksDefC.setMarkup(True)
    
    openthreadDefinitionsH = openthread.createFileSymbol('OPEN_THREAD_DEFINITIONS_H', None)
    openthreadDefinitionsH.setType('STRING')
    openthreadDefinitionsH.setOutputName('core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES')
    openthreadDefinitionsH.setSourcePath('driver/templates/system/system_definitions.h.ftl')
    openthreadDefinitionsH.setMarkup(True)
    
    ##########################################################################################
    ## Thread Compiler settings
    #########################################################################################
    
    # === Set C optimization level
    OTCOptLevel = openthread.createSettingSymbol("OPENTHREAD_C_OPTIMIZATION", None)
    OTCOptLevel.setValue("-O2")
    OTCOptLevel.setCategory("C32")
    OTCOptLevel.setKey("optimization-level")
    
    # === Set CPP optimization level
    OTCPPOptLevel = openthread.createSettingSymbol("OPENTHREAD_CPP_OPTIMIZATION", None)
    OTCPPOptLevel.setValue("-O2")
    OTCPPOptLevel.setCategory("C32CPP")
    OTCPPOptLevel.setKey("optimization-level")
    
    
    # === Additional options
    global xc32CMSECompilerFlag
    xc32CMSECompilerFlag =  openthread.createSettingSymbol("SEC_XC32_CMSE_FLAG", None)
    xc32CMSECompilerFlag.setCategory("C32")
    xc32CMSECompilerFlag.setKey("appendMe")
    xc32CMSECompilerFlag.setValue("-include"+'"'+ "../src/config/"+configName + '/driver/thread/'+'inc/openthread_stack_config.h'+'"')
    xc32CMSECompilerFlag.setAppend(True, " ")
    
    global xc32PPCMSECompilerFlag
    xc32PPCMSECompilerFlag =  openthread.createSettingSymbol("SEC_XC32PP_CMSE_FLAG", None)
    xc32PPCMSECompilerFlag.setCategory("C32CPP")
    xc32PPCMSECompilerFlag.setKey("appendMe")
    xc32PPCMSECompilerFlag.setValue("-include" +'"'+"../src/config/"+configName + '/driver/thread/'+'inc/openthread_stack_config.h'+'"')
    xc32PPCMSECompilerFlag.setAppend(True, " ")
       
    

def onAttachmentConnected(source, target):
    # print("onAttachmentConnected-openthread:",source,target)
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    if (connectID == "OT_WolfCrypt_Dependency"):
        # Database.connectDependencies([['lib_crypto', 'LIB_CRYPTO_WOLFCRYPT_Dependency', 'lib_wolfcrypt', 'lib_wolfcrypt']])
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_128", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_ecb", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_ecb_hw", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_cbc", True)
        Database.setSymbolValue("lib_wolfcrypt", "wolfcrypt_aes_cbc_hw", True)
        
    elif (connectID == "OT_USART_dependency"):
        if Database.getSymbolValue("drv_usart","DRV_USART_COMMON_MODE") != "Asynchronous":
            Database.setSymbolValue("drv_usart", "DRV_USART_COMMON_MODE", "Asynchronous")
        openthreadUartConfig.setValue(True)
        # Database.connectDependencies([['OPEN_THREAD','OT_USART_dependency','drv_usart_0','drv_usart']])
    
    elif (connectID == "OT_802154phy_dependency"):
        Database.setSymbolValue("IEEE_802154_PHY","CREATE_PHY_RTOS_TASK",True)
        Database.setSymbolValue("IEEE_802154_PHY","CREATE_PHY_SEMAPHORE",True)
        Database.setSymbolValue("IEEE_802154_PHY","PHY_TASK_PRIORITY",4)
        global phy_component_Task_Sym
        phy_component_Task_Sym = remoteComponent.getSymbolByID("PHY_TASK_PRIORITY")
        phy_component_Task_Sym.setReadOnly(True)
        global phy_bmm_large_buffers_Sym
        phy_bmm_large_buffers_Sym = remoteComponent.getSymbolByID("PHY_INTEGER_BMMLARGEBUFFERS")
        phy_bmm_large_buffers_Sym.setValue(9)
        phy_bmm_large_buffers_Sym.setReadOnly(True)
        
    elif (connectID == "OT_DeviceSupportDependency"):
        Database.sendMessage(remoteID, "RTC_SUPPORT", {"target":remoteID,
                                                        "source": localComponent.getID(),
                                                        "rtcRequired": False})
        # Database.setSymbolValue(remoteID,"THREADSTACK_LOADED",True)
    
    elif (connectID == "OT_FreeRtosDependency"):
        Database.setSymbolValue("FreeRTOS","FREERTOS_USE_TIMERS",True)
        Database.setSymbolValue("FreeRTOS","FREERTOS_TOTAL_HEAP_SIZE",46080)
        
        
    elif (connectID == "openthread_Capability"):
        # print("Openthread Capability")
        componentids = Database.getActiveComponentIDs()
        # print("componentids:",componentids)
        if "THREAD_CLI" in componentids:
            openthreadroleconfig1.setValue(Database.getSymbolValue("THREAD_CLI","OPEN_THREAD_DEVICE_ROLE_CLI_CONFIG"))


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    
    if (connectID == "OT_USART_dependency"):
        openthreadUartConfig.setValue(False)
    


def finalizeComponent(openthread):
    # pass
    result = Database.connectDependencies([['OPEN_THREAD', 'OT_WolfCrypt_Dependency', 'lib_wolfcrypt', 'lib_wolfcrypt']])
    result = Database.connectDependencies([['lib_crypto', 'LIB_CRYPTO_WOLFCRYPT_Dependency', 'lib_wolfcrypt', 'lib_wolfcrypt']])



def destroyComponent(openthread):
    requiredComponents.extend(["drv_usart","THREAD_CLI"])
    phy_component_Task_Sym.setReadOnly(False)
    phy_bmm_large_buffers_Sym.setReadOnly(False)
    uartTxRingBufferSym.setReadOnly(False)
    TcPrescalerSymbol.setReadOnly(False)
    for comp in requiredComponents:
        Database.deactivateComponents([comp])
    
    
def handleMessage(messageID, args):
    # print(messageID, args)
    if(messageID == 'ANTENNA_GAIN_CHANGE'):
        component = Database.getComponentByID(args['target'])
        if (component):
            customGainValue = component.getSymbolByID('CUSTOM_ANT_GAIN')
            customRegion = component.getSymbolByID('CUSTOM_ANT_REGION')
            for arg in args:
                Log.writeInfoMessage('{:<17}: {}: {}'.format('', arg, args[arg]))
                if('CUSTOM_ANT_GAIN' == arg):
                    customGainValue.setValue(args[arg])
                if('CUSTOM_ANT_REGION' == arg):
                    customRegion.setValue(args[arg])
    
    # elif(messageID == "OPEN_THREAD_CLI_ENABLED"):
        # if openthreadrole.getValue() == 2:
            # print("openthreadParserUpdateCallback")
            # componentids = Database.getActiveComponentIDs()
            # print("componentids:",componentids)
            # Database.connectDependencies([['OPEN_THREAD_CLI','openthread_Dependency','OPEN_THREAD','openthread_Capability']])
            # if "OPEN_THREAD_CLI" in componentids:
                # print("Removing Cli App")
            # Database.deactivateComponents(["OPEN_THREAD_CLI"]) 
            # openthreadUartParser.setValue(False)