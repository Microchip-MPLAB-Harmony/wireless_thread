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
import os

#Global list with openthread file list record
global openthreadfileRecords
openthreadfileRecords = []
#Absolute paths to Parse through the repo
global abs_paths
abs_paths = ['openthread\include','openthread\src','openthread'+'\\'+'third_party\mbedtls','openthread'+'\\'+'third_party'+'\\'+'tcplp','openthread\examples','src']
# Dir_cnt = 0

folderpathpos = 0
fileslistpos  = 1

def Traversebyonefolder():
    m = os.getcwd()
    n = m.rfind("\\")
    d = m[0: n+1]
    os.chdir(d)
    
    
def getrelativepath(originalpath,basefolder):
    start = 0
    relativepath = ''
    fullpath = originalpath.split('\\')
    folder = basefolder.split('\\')
    for pos in range(len(fullpath)):
        if str(fullpath[pos]) == str(folder[0]):
            start = pos
            break
    
    for pos in range(start,len(fullpath)):
        if pos < len(fullpath)-1:
            relativepath += (fullpath[pos]+str("/"))
        else:
            relativepath += fullpath[pos]
    
    # print("Relative_path:"+relativepath)
    return relativepath
    

if openthreadfileRecords == []:
    # print("Module.getPath():",Module.getPath())
    original_directory = os.getcwd()
    # print("original Directory"+original_directory)
    os.chdir(Module.getPath())
    openthread_path = os.getcwd()
    # print(openthread_path)
    for path in abs_paths:
        if path == 'src':
            openthread_include =  openthread_path +'\\' +path
        else:
            openthread_include =  openthread_path +'\\' 'third_party'  +'\\' +path
        # print('openthread include:'+openthread_include)
        for (dir_path, dir_names, file_names) in os.walk(openthread_include):
            if 'posix' not in dir_path:
                relative_path = getrelativepath(dir_path,path)
                if len(path.split('\\')) == len(relative_path.split('/')): 
                    localDirList = []
                    localDirList.append(relative_path)
                    if file_names != []:
                        localDirList.append(file_names)
                    openthreadfileRecords.append(localDirList)
                    # print(file_names)
                else:
                    localDirList = []
                    localDirList.append(relative_path)
                    if file_names != []:
                        localDirList.append(file_names)
                    openthreadfileRecords.append(localDirList)
        
    os.chdir(original_directory)
    current_dir = os.getcwd()
    # print("Current Directory"+current_dir)
    
    # for i in range(len(openthreadfileRecords)):
        # print(openthreadfileRecords[i])
        # print('\n')




