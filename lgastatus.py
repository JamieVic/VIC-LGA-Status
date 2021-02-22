import csv, urllib.request

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSshBgCbldwtXKoqWsumyzaG6Q063vWGLEmZWDkdjK49MVf7YvcVso4v8yrPfo8CN1t_Q4Hp8TF_MPm/pub?gid=1798358420&single=true&output=csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
zoneReader = csv.reader(lines, delimiter = ",")
lga = input("Search LGA: ").capitalize()
for cols in zoneReader:
    if lga in cols[1]:
        if cols[2] == "green":
            print("Eligible for a permit. No test or self-quarantine required.")
        elif cols[2] == "orange":
            print("Eligible for a permit. Test required within 72 hours of arrival, self-quarantine until negative test received.")
        elif cols[2] == "red":
            print("Not eligible for a permit without an exception, Specified Worker Permit, transit permit or exemption.")
        else:
            print("LGA not found.")
