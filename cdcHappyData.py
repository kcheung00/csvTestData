import argparse
import csv
import datetime
import random
import string

parser = argparse.ArgumentParser(description="Generate PDX Snowflake TSV test data. Header Template File is template.csv")

parser.add_argument("outFile", help="Output File Name")
parser.add_argument("numRecord", type=int, help="Number of Records")

args = parser.parse_args()

print("TSV Test Data file {} contain {}".format(args.outFile, args.numRecord))
print("Out File = " + args.outFile)
print("Num Record = " + str(args.numRecord))

def randomIntRightPad0(iStart, iEnd, digit ):
    value = str(random.randint(iStart,iEnd)).rjust(digit, "0")
    return(value)

def random_Recip_Id(strIndex):
    return( randomIntRightPad0(1000, 9999, 4) + ' ' + strIndex.rjust(8, "0") )

def random_Name(strName, strIndex):
    return( strName + '-' + strIndex )

def randomMiddleName():
    names=['middle', 'UNK']
    name = random.choice(names)
    if name != 'UNK' :
        name = ''.join(random.choice(string.ascii_letters))
    return( name )

def randomDateOfBirth():
    year = str(random.randint(1900, datetime.date.today().year))
    month = str(random.randint(1,12)).rjust(2, "0")
    date = str(random.randint(1,31)).rjust(2, "0")
    DOB = str(year) + '-' + str(month) + '-' + str(date)
    return( DOB )

def randomSexValue():
    sexOption=['M', 'F', 'U']
    sex = random.choice(sexOption)
    return( sex )

def randomStreet_1():
    types = ['street', 'road', 'blvd', 'lane', 'drive']
    z = random.choice(types)
    x = str(random.randint(10, 9999))
    y = ''.join(random.choice(string.ascii_letters) for i in range(10))
    street = x + ' ' + y + ' ' + z
    return(street)

def randomStreet_2():
    streets = ['stree two whatever','UKN']
    return(random.choice(streets))

def randomRace():
    raceOptions=['1002-5','2028-9','2076-8','2054-5','2106-3','2131-1','UNK','POL']
    race = random.choice(raceOptions)
    return(race)

def randomEthnicity():
    ethnicityOptions=['2135-2','2186-5','UNK','POL','43434-4'] 
    ethnicity = random.choice(ethnicityOptions)
    return(ethnicity)

def random_CodeSet(filename):
    codeFile = open(filename, "r")
    codes = codeFile.read()
    codeList = codes.split("\n")
    codeFile.close()
    code = random.choice(codeList)
    return(code)

def randomLotNumber():
    options = ['FC3180','FE3590','026D21A','012F21A','FC3184','FF2590','FC3180','023C21A','023C1A','FF2593']
    return(random.choice(options) )

def randomAdminSite():
    options = ['LT','LA','LD','LG','LVL','LLFA','RT','RA','RD','RG','RVL','RLFA']
    return(random.choice(options) )

def randomVaxRoute():
    options = ['C38238','C28161','C38284','C38276','C38288','C38676','C38299','C38305']
    return(random.choice(options) )






with open('template.csv', 'r', encoding='UTF-8-sig') as file:
    reader = csv.DictReader(file, delimiter = '\t')
    header = reader.fieldnames

writer = csv.DictWriter(open(args.outFile, "w"), fieldnames=header, delimiter='\t')
writer.writeheader()

# for fieldname in header:
#     print(fieldname)

for i in range(0, args.numRecord):
    writer.writerow(dict([
        ("vax_event_id", str(random.randint(1000000,9999999))
                     + ''.join(random.choice(string.ascii_uppercase) for i in range(2))
                     + str(random.randint(1000,9999))
        ), # required
        ("ext_type", "I"), # required
        ("pprl_id", ""),   # required - retired
        ("recip_id", random_Recip_Id(str(i))), #required
        ("recip_first_name", random_Name("FirstName", str(i))), # missing - UNK
        ("recip_middle_name", randomMiddleName()), # missing - UNK
        ("recip_last_name", random_Name("LastName", str(i))), # missing - UNK
        ("recip_dob", randomDateOfBirth()), # required
        ("recip_sex", randomSexValue()), # required
        ("recip_address_street", randomStreet_1()), # missing - UNK
        ("recip_address_street_2", randomStreet_2()), # missing - UNK
        ("recip_address_city", "Streamwood"), # missing - UNK
        ("recip_address_county", "17031"), # missing - empty
        ("recip_address_state", "IL"), # missing - empty
        ("recip_address_zip", "60107"), # missing - empty
        ("recip_race_1", randomRace()), # required
        ("recip_race_2", randomRace()), # missing - empty
        ("recip_race_3", randomRace()), # missing - empty
        ("recip_race_4", randomRace()), # missing - empty
        ("recip_race_5", randomRace()), # missing - empty
        ("recip_race_6", randomRace()), # missing - empty
        ("recip_ethnicity", randomEthnicity()), # required
        ("admin_date", datetime.date.today() ), # required
        ("cvx", random_CodeSet("cvx.txt") ), # required
        ("ndc", random_CodeSet("ndc11.txt") ), # reqired of known
        ("mvx", random_CodeSet("mvx.txt")),
        ("lot_number", randomLotNumber()),
        ("vax_expiration", "2021-12-20"),
        ("vax_admin_site", randomAdminSite()),
        ("vax_route", randomVaxRoute()),
        ("DOSE_NUM", "3"),
        ("VAX_SERIES_COMPLETE", "YES"),
        ("responsible_org", "Albertsons Companies"),
        ("admin_name", "SAFEWAY PHARMACY #2713"),
        ("vtrcks_prov_pin", "AB1002794"),
        ("admin_type", "17"),
        ("admin_address_street", randomStreet_1()),
        ("admin_address_street_2", randomStreet_2()),
        ("admin_address_city", "BOWIE"),
        ("admin_address_county", "24033"),
        ("admin_address_state", "MD"),
        ("admin_address_zip", "20720"),
        ("vax_refusal", "No"), # required
        ("cmorbid_status", "UNK"), # required
        ("serology", "UNK"), # required
    ]))

    