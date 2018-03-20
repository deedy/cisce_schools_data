# CISCE Schools Data

[CISCE](https://en.wikipedia.org/wiki/Council_for_the_Indian_School_Certificate_Examinations) is one of the two national level boards of education in India (alongwith [CBSE](https://en.wikipedia.org/wiki/Central_Board_of_Secondary_Education)).
While CBSE is a government board, CISCE is a private board.
Every year, over **300,000** students take the ICSE (Class X) and the ISC (Class XII) board examination in India (and several schools abroad).
The sister repository to this, contains the [cbse_schools_data](https://github.com/deedy/cbse_schools_data).

As of **2018**, there are **2,341** schools affiliated with the CISCE (out of which only 7 are outside India).
The details of each of these schools can be fetched from the [CISCE School Directory](http://www.cisce.org/locate-search.aspx?country=0&state=0&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate).

## Instructions

The main contribution of this project is to scrape, parse, clean, document, dump and open the data for all of these schools. 
The scraping, parsing and cleaning code is not in this repository.

 - `README_DATA` contains a protocol buffer like documentation for the data and lists each of the fields, including which ones are required and optional, the degree to which the optional ones are present, as well as the type and enum definitions of each field.
 - `analyze_csv.py` reads the `csv` file in Python and prepares it for analysis.
 - `schools.csv` the csv file - 501KB
 - `analyze_pickle.py` reads the `pickle` file in Python and prepares it for analysis.
 - `schools.p` the pickle file - 722KB
 
## Short Documentation

There are 16 total fields per school, a total of 38k data points. For full documentation, see `README_DATA`. 

 - `required string name` Name of the school
 - `required string code` 5-digit unique code for school (e.g. AP001)
 - `required string address` Postal Address
 - `required State state` Indian State or Union Territory (or Country/City if international - DUBAI, INDONESIA, SHARJAH, SINGAPORE, THAILAND)
 - `optional Phone off_ph_no` Office Phone number. Integral phone number that may be prefixed with '+'.
 - `optional Phone off_ph_no_2` Office Phone number 2. Integral phone number that may be prefixed with '+'.
 - `optional Phone fax_no` Fax number. Integral phone number that may be prefixed with '+'.
 - `optional string email` Email address
 - `optional string website` Website of the school
 - `required Gender gender` Gender of the school students (e.g. Co-ed, Boys, Girls)
 - `optional ResidentialType res_type` Residential Type (e.g. D/R, Day)
 - `required AffiliationType aff_type` Affiliation type of the school (e.g Permanent, Provisional)
 - `required bool is_icse` Does this school administer ICSE (Class X examinations)
 - `required bool is_isc` Does this school administer ISC (Class XII examinations)
 - `required bool is_cve` Does this school administer CVE (Certificate of Vocational Education)
 - `required string princi_name` Name of the principal.

 # License 
 This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
