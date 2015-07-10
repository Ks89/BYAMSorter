#
#Copyright 2015 Stefano Cappa
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#

__author__ = 'Stefano Cappa'

ipswList = []

iphoneList = []
ipadList = []
ipodList = []
appletvList = []
otherList = []


# read file and put lines in a list
with open('ipswlista.txt', 'r') as f:
    for line in f:
        ipswFile = ''
        resplittedElem = line.split('___')[0].split('/')
        if '.ipsw' in resplittedElem[5]:
            ipswFile = resplittedElem[5]
        elif '.ipsw' in resplittedElem[6]:
            ipswFile = resplittedElem[6]
        elif '.ipsw' in resplittedElem[8]:
            ipswFile = resplittedElem[8]
        elif '.ipsw' in resplittedElem[9]:
            ipswFile = resplittedElem[9]

        if 'iPad' in ipswFile:
            ipadList.append(line)
        elif 'iPod' in ipswFile:
            ipodList.append(line)
        elif 'AppleTV' in ipswFile:
            appletvList.append(line)
        elif 'iPhone' in ipswFile:
            iphoneList.append(line)
        else:
            otherList.append(line)


ipadList.sort(key=lambda s: s.split("___")[-2])
ipodList.sort(key=lambda s: s.split('___')[-2])
appletvList.sort(key=lambda s: s.split('___')[-2])
iphoneList.sort(key=lambda s: s.split('___')[-2])
otherList.sort(key=lambda s: s.split('___')[-2])


with open('newFile.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write(''.join(iphoneList))
    myfile.write(''.join(ipadList))
    myfile.write(''.join(ipodList))
    myfile.write(''.join(appletvList))
    myfile.write(''.join(otherList))