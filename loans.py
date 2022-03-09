import zipfile
import json
import io
import csv


race_lookup = {
    "1": "American Indian or Alaska Native",
    "2": "Asian",
    "21": "Asian Indian",
    "22": "Chinese",
    "23": "Filipino",
    "24": "Japanese",
    "25": "Korean",
    "26": "Vietnamese",
    "27": "Other Asian",
    "3": "Black or African American",
    "4": "Native Hawaiian or Other Pacific Islander",
    "41": "Native Hawaiian",
    "42": "Guamanian or Chamorro",
    "43": "Samoan",
    "44": "Other Pacific Islander",
    "5": "White",
}
class Applicant:
    def __init__(self, age, race):
        self.age = age
        self.race = set()
        
        for r in race:
            if(r in race_lookup.keys()):
                self.race.add(race_lookup[r])
    def __repr__(self):
        list_of_races = list(self.race)
        return f"Applicant('{self.age}', {list_of_races})"
    def lower_age(self):       
        if('>' in self.age):
            return self.age.replace('>','')
        if('<' in self.age):
            return self.age.replace('<','')
        if("-" in self.age):
            x =self.age.split("-")
        return int(x[0])
    def __lt__(self, other):
        if(int(self.lower_age)<int(other.lower_age)):
            return True
        else:
            return False
class Loan:
    def __init__(self, values):
        if(values["loan_amount"] == "NA" or values["loan_amount"] == "Exempt"):
            self.loan_amount = float(-1);
        else:
            self.loan_amount = float(values["loan_amount"])
        if(values["property_value"] == "NA" or values["property_value"] == "Exempt"):
            self.property_value = float(-1);
        else:
            self.property_value = float(values["property_value"])
        if(values["interest_rate"] == "NA" or values["interest_rate"] == "Exempt"):
            self.interest_rate = float(-1);
        else:
            self.interest_rate = float(values["interest_rate"])
            
        #set_of_races
        set_of_races = set()
        if(values["applicant_race-1"] != ''):
            set_of_races.add(values["applicant_race-1"])
        if(values["applicant_race-1"] != ''):
            set_of_races.add(values["applicant_race-1"])
        if(values["applicant_race-1"] != ''):
            set_of_races.add(values["applicant_race-1"])
        if(values["applicant_race-1"] != ''):
            set_of_races.add(values["applicant_race-1"])
        if(values["applicant_race-1"] != ''):
            set_of_races.add(values["applicant_race-1"])
            
        #applicants list
        self.applicants = [Applicant(values["applicant_age"],set_of_races)]
        
        #if coapplicant exists
        if(values["co-applicant_age"] != "9999"):
            set_of_coraces = set()
            if(values["co-applicant_race-1"] != ''):
                set_of_coraces.add(values["co-applicant_race-1"])
            if(values["co-applicant_race-1"] != ''):
                set_of_coraces.add(values["co-applicant_race-1"])
            if(values["co-applicant_race-1"] != ''):
                set_of_coraces.add(values["co-applicant_race-1"])
            if(values["co-applicant_race-1"] != ''):
                set_of_coraces.add(values["co-applicant_race-1"])
            if(values["co-applicant_race-1"] != ''):
                set_of_coraces.add(values["co-applicant_race-1"])
            self.applicants.append(Applicant(values["co-applicant_age"], set_of_coraces))
        
def yearly_amounts(self, yearly_payment):
    # TODO: assert interest and amount are positive
    result = []
    amt = self.loan_amount

    while amt > 0:
        yield am
        result.append(amt)
        # TODO: add interest rate multiplied by amt to amt
        amt += amt * self.interest_rate / 100
        # TODO: subtract yearly payment from amt
        amt -= yearly_payment
    #return result
def __str__(self):
    return f"<Loan: {self.interest_rate}% on ${self.property_value} with{len(self.applicants)} applicant(s)>"

def __repr__(self):
    return f"<Loan: {self.interest_rate}% on ${self.property_value} with {len(self.applicants)} applicant(s)>"

class Bank:
    def __init__(self, bank_name):
        self.loans = []
        self.lei = ""
        with open("banks.json") as banks:
            for bank in json.load(banks):
                if bank["name"] == bank_name:
                    self.lei = bank["lei"]
        zf = zipfile.ZipFile("wi.zip")
        with zf.open("wi.csv") as wi_csv:
            reader = csv.DictReader(io.TextIOWrapper(wi_csv))
            for row in reader:
                if row["lei"] == self.lei:
                    self.loans.append(Loan(row))

    def __getitem__(self, item):
        return self.loans[item]

    def __len__(self):
        return len(self.loans)
