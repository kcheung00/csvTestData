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

def randomFirstName():
    names=['Amy_', 'Bob_', 'Mary_', 'John_', ' ', '', 'UNK']

    name = random.choice(names)
    if name == 'UNK' :
        print(f"UNK name = {name}")
    elif name == '':
        print(f"empty name {name}")
    else :
        name = name + ''.join(random.choice(string.ascii_letters) for i in range(5))
    return( name )

def randomMiddleName():
    names=['C', 'B_', ' ', '', 'UNK']

    name = random.choice(names)
    if name == 'UNK' :
        print(f"UNK name = {name}")
    elif name == '':
        print(f"empty name {name}")
    else :
        name = name + ''.join(random.choice(string.ascii_letters))
    return( name )

def randomLastName():
    names=['Brown_', 'Jones_', 'Gate_', 'Job_', '', 'UNK']

    name = random.choice(names)
    if name == 'UNK' :
        print(f"UNK name = {name}")
    elif name == '':
        name = ""
        print(f"empty name {name}")
    else :
        name = name + ''.join(random.choice(string.ascii_letters) for i in range(5))
    return( name )

def randomDateOfBirth():
    year = str(random.randint(1900, datetime.date.today().year))
    month = str(random.randint(1,12)).rjust(2, "0")
    date = str(random.randint(1,31)).rjust(2, "0")
    DOB = str(year) + '-' + str(month) + '-' + str(date)
    return( DOB )

def randomSexValue():
    sexOption=['M', 'F', 'U', '']
    sex = random.choice(sexOption)
    return( sex )

def randomStreet_1():
    types = ['street', 'road', 'blvd', 'lane', 'drive', '', ' ']

    z = random.choice(types)
    if z == '':
        street = ''
    elif z == ' ':
        street = 'UNK'
    else:
        x = str(random.randint(10, 9999))
        y = ''.join(random.choice(string.ascii_letters) for i in range(10))
        # z = random.choice(type)
        street = x + ' ' + y + ' ' + z

    return(street)

def randomStreet_2():
    streets = ['stree two whatever', '', ' ', 'UKN', ' ']
    return(random.choice(streets))

def randomCity():
    cities=['Pleasanton', 'Whatever', 'BOISE City', 'City City', 'UKN', '', ' ']
    city = random.choice(cities)
    return( city )

def randomCountyCode():
    countyCode = str(random.randint(1000,99999)).rjust(5, "0")
    badCode1 = str(random.randint(1,100))
    badCode2 = str(random.randint(100000, 1000010))
    code = [countyCode, badCode1, badCode2, "", ' ', 'UNK']
    return(random.choice(code))

def random2LetterState():
    states=['AL','AK','AS','AZ','AR','CA','CO','CT','DE','DC','FM','FL','GA','GU','HI','ID','UNK',
            'IL','IN','IA','KS','KY','LA','ME','MH','MD','MA','MI','MN','MS','MO','MT','NE','UNK',
            'NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PW','PA','PR','RI','SC',' ',
            'SD','TN','TX','UT','VT','VI','VA','WA','WV','WI','WY', ' ', '']
    state = random.choice(states)
    return(state)

def randomZipCode():
    zipCode = str(random.randint(1001,99999)).rjust(5, "0")
    badCode = str(random.randint(100,9999))
    code = [zipCode, zipCode, badCode, "", ' ', 'UNK']
    return(random.choice(code))

def randomRace():
    raceOptions=['1002-5','2028-9','2076-8','2054-5','2106-3','2131-1','UNK','POL', '', ' ', 'bad boy', '1111-1']
    race = random.choice(raceOptions)
    return(race)

def randomEthnicity():
    ethnicityOptions=['2135-2','2186-5','UNK','POL','',' ','43434-4','bad boy','3434'] 
    ethnicity = random.choice(ethnicityOptions)
    return(ethnicity)

# 1. Should not be dated before the recipient's Date of Birth
# 2. Should not be dated after the date of record submission
# 3. Should not be in 2019 or earlier.
def randomAdminDate():
    year = str(random.randint(2020, datetime.date.today().year+1))
    month = str(random.randint(1,12)).rjust(2, "0")
    date = str(random.randint(1,31)).rjust(2, "0")
    DOB = str(year) + '-' + str(month) + '-' + str(date)
    print(DOB)
    return( DOB )

def random_CodeSet(filename):
    codeFile = open(filename, "r")
    codes = codeFile.read()
    codeList = codes.split("\n")
    codeFile.close()
    code = random.choice(codeList)
    return(code)





with open('template.csv', 'r', encoding='UTF-8-sig') as file:
    reader = csv.DictReader(file, delimiter = '\t')
    header = reader.fieldnames

# print(header)
# print(header[0])
# print(header[1])
# print(len(header))

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
        ("recip_id", random.randint(100000000,999999999)), #required
        ("recip_first_name", randomFirstName()), # missing - UNK
        ("recip_middle_name", randomMiddleName()), # missing - UNK
        ("recip_last_name", randomLastName()), # missing - UNK
        ("recip_dob", randomDateOfBirth()), # required
        ("recip_sex", randomSexValue()), # required
        ("recip_address_street", randomStreet_1()), # missing - UNK
        ("recip_address_street_2", randomStreet_2()), # missing - UNK
        ("recip_address_city", randomCity()), # missing - UNK
        ("recip_address_county", randomCountyCode()), # missing - empty
        ("recip_address_state", random2LetterState()), # missing - empty
        ("recip_address_zip", randomZipCode()), # missing - empty
        ("recip_race_1", randomRace()), # required
        ("recip_race_2", randomRace()), # missing - empty
        ("recip_race_3", randomRace()), # missing - empty
        ("recip_race_4", randomRace()), # missing - empty
        ("recip_race_5", randomRace()), # missing - empty
        ("recip_race_6", randomRace()), # missing - empty
        ("recip_ethnicity", randomEthnicity()), # required
        ("admin_date", randomAdminDate() ), # required
        ("cvx", random_CodeSet("cvx.txt") ), # required
        ("ndc", random_CodeSet("ndc11.txt") ), # reqired of known
        ("mvx", random_CodeSet("mvx.txt")),
        ("lot_number", "343434"),
        ("vax_expiration", "343434"),
        ("vax_admin_site", "343434"),
        ("vax_route", "343434"),
        ("DOSE_NUM", "343434"),
        ("VAX_SERIES_COMPLETE", "343434"),
        ("responsible_org", "343434"),
        ("admin_name", "343434"),
        ("vtrcks_prov_pin", "343434"),
        ("admin_type", "343434"),
        ("admin_address_street", "343434"),
        ("admin_address_street_2", "343434"),
        ("admin_address_city", "343434"),
        ("admin_address_county", "343434"),
        ("admin_address_state", "343434"),
        ("admin_address_zip", "343434"),
        ("vax_refusal", "343434"),
        ("cmorbid_status", "343434"),
        ("serology", "343434"),
    ]))

    