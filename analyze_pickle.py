from collections import namedtuple
import pickle
import time

# http://www.cisce.org/locate-search.aspx?country=0&state=0&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate
CisceSchoolFields = [
        'name', # Name of institution
        'code', # Unique registration code
        'address', # Postal Address
        'state', # State (or Foreign City/Country)
        'off_ph_no', # Office phone number
        'off_ph_no_2', # Optional office phone number
        'fax_no', # Fax number
        'email', # Email 
        'website', # Website
        'gender', # Gender of the students of the school (e.g. Co-educational, Boys, Girls)
        'res_type', # Residential type (e.g. Day, D/R)
        'aff_type', # Affiliation type (e.g. Provisional, Permanent)
        'is_icse', # Is Class XII ICSE exam
        'is_isc', # Is Class XII ISC exam 
        'is_cve', # Is Center for Vocational Education (CVE)
        'princi_name', # Principal Name
]
CisceSchool = namedtuple('CisceSchool', CisceSchoolFields)


RES_FILE_P = 'schools.p'
print('Reading {0}...'.format(RES_FILE_P))
start = time.time()
with open(RES_FILE_P, 'rb') as f:
  data = pickle.load(f)
print('Loaded {0} rows in {1:0.2f} seconds.'.format(len(data), time.time() - start))
