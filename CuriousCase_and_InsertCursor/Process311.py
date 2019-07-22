import arcpy
import json
from urllib import request
import urllib.parse
from requestUtil import Request



# Front part of request url
site = 'https://data.boston.gov/api/3/action/datastore_search?'

# Additional url parameters
params = {'resource_id':"2968e2c0-d479-49ba-a884-4ef523ada3c0",'limit':'10000'}

paramEncode = urllib.parse.urlencode(params)

url = site + paramEncode

fileobj = request.urlopen(url)

reqData = fileobj.read()

reqDataJson = json.loads(reqData)


fc = r"C:\projects\Mass\Boston311\Boston311.gdb\ServiceRequests"


#Get the fields from an existing Featureclass
flds = [fld.name for fld in arcpy.ListFields(fc)]

#remove OID and Shape
flds.remove("OBJECTID")
flds.remove("Shape")
flds.append("SHAPE@XY")


#create the cursor
icur = arcpy.da.InsertCursor(fc,flds)

# Shape@XY is not an attribute of the data
flds.remove("SHAPE@XY")

#for reqs in reqDataJson['value']:
for reqs in reqDataJson['result']['records']:
    #reqs.pop('_full_text')
    # create an instance of the Request class
    rptRequest = Request.create(reqs)

    # use the method to sequence the class properties into a list
    iRow = rptRequest.toArcpyRow(flds)

    # add the service request geometry
    geom =(float(rptRequest.longitude),float(rptRequest.latitude))

    # append the geomtery
    iRow.append(geom)

    # create the new feature
    icur.insertRow(iRow)

    print("added to the featureclass")

del icur



