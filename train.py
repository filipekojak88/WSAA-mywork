import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
# print(doc.toprettyxml()) # output to console comment this out once you know it works

# if I want to store the xml in a file.
with open('trains.xml', 'w') as xmlfp:
   doc.writexml(xmlfp)

with open ('week03_train.csv',mode = 'w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        # traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode")[0]
        # traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag)[0]
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)    


           

'''
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude")[0]
    trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
    '''