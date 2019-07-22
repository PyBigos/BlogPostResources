import datetime

class Request():
    """Class Definition for a new request"""

    #Fields to check
    floatFlds = ['latitude','longitude']
    dtFlds = ['open_dt','target_dt','closed_dt']
    txtFlds = ['_id', 'case_enquiry_id', 'ontime', 'case_status', 'closure_reason', 'case_title',
               'subject', 'reason', 'type', 'queue', 'department', 'submittedphoto', 'closedphoto',
               'location', 'fire_district', 'pwd_district', 'city_council_district', 'police_district', 'neighborhood',
               'neighborhood_services_district', 'ward', 'precinct', 'location_street_name', 'location_zipcode','source']

    def __init__(self,_id=' ',case_enquiry_id=' ',open_dt='2004-10-27 20:25:31',target_dt='2004-10-27 21:25:31',closed_dt='2004-10-27 22:25:31',
                 ontime=' ',case_status=' ',closure_reason=' ',case_title=' ',subject=' ',reason=' ',type=' ',queue=' ',department=' ',
                 submittedphoto=' ',closedphoto=' ',location=' ',fire_district=' ',pwd_district=' ',city_council_district=' ',
                 police_district=' ',neighborhood=' ',neighborhood_services_district=' ',ward=' ',precinct=' ',
                 location_street_name=' ',location_zipcode=' ',latitude=42.3559557,longitude=71.0819701,source=' '):

        """Pass values to override default values"""
        #Override the default values
        self._id = _id
        self.case_enquiry_id = case_enquiry_id
        self.open_dt = open_dt
        self.target_dt = target_dt
        self.closed_dt = closed_dt
        self.ontime = ontime
        self.case_status = case_status
        self.closure_reason = closure_reason
        self.case_title = case_title
        self.subject = subject
        self.reason = reason
        self.type = type
        self.queue = queue
        self.department = department
        self.submittedphoto = submittedphoto
        self.closedphoto = closedphoto
        self.location = location
        self.fire_district = fire_district
        self.pwd_district = pwd_district
        self.city_council_district = city_council_district
        self.police_district = police_district
        self.neighborhood = neighborhood
        self.neighborhood_services_district = neighborhood_services_district
        self.ward = ward
        self.precinct = precinct
        self.location_street_name = location_street_name
        self.location_zipcode = location_zipcode
        self.latitude = latitude
        self.longitude = longitude
        self.source = source


    @classmethod
    def create(cls,d:dict):
        return cls(**d)

    def toArcpyRow(self,fields):

        retVals = []

        for fld in fields:

            lFld = fld.lower()

            #short fields
            if lFld in self.floatFlds:
                retVals.append(float(self.__dict__[lFld]))

            # Date fields
            if lFld in self.dtFlds and self.__dict__[lFld] != None:
                dt = datetime.datetime.strptime(self.__dict__[lFld],'%Y-%m-%d %H:%M:%S')
                retVals.append(dt)
            elif lFld in self.dtFlds and self.__dict__[lFld] == None:
                dt = datetime.datetime.strptime('2004-10-27 20:25:31', '%Y-%m-%d %H:%M:%S')
                retVals.append(dt)

            if lFld in self.txtFlds:

                if isinstance(self.__dict__[lFld],str):
                    if len(self.__dict__[lFld]) <256:
                        retVals.append(self.__dict__[lFld])
                    else:
                        retVals.append(self.__dict__[lFld][0:255])

                elif isinstance(self.__dict__[lFld],int):
                    sVal = str(self.__dict__[lFld])
                    retVals.append(sVal)
                elif isinstance(self.__dict__[lFld],type(None)):
                    retVals.append('None')

        return retVals