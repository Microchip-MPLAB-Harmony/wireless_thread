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

def Traversebyonefolder(m):
    # m = os.getcwd()
    n = m.rfind("\\")
    d = m[0: n+1]
    print("Traveresed_path",d)
    # os.chdir(d)
    return d
    
    
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
    thirdpartyopenthreadDir = Traversebyonefolder(openthread_path)
    for path in abs_paths:
        if path == 'src':
            openthread_include =  openthread_path +'\\' +path
        else:
            openthread_include =  thirdpartyopenthreadDir +'\\' +path
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




