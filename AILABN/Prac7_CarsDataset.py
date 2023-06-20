DAge={'<=30':{'yes':2/5, 'no':3/5},
       '30-40':{'yes':1,'no':0},
       '>40':{'yes':3/5, 'no':2/5}}
DIncome={
    'low':{'yes':3/4,'no':1/4},
    'medium':{'yes':4/6,'no':2/6},
    'high':{'yes':2/4,'no':2/4}
}
DStudent={
    'yes':{'yes':6/7,'no':1/7},
    'no':{'yes':3/7,'no':4/7}
}
DCredit={
    'fair':{'yes':6/8,'no':2/8},
    'excellent':{'yes':3/6,'no':3/6}
}

PYes=9/14
PNo=5/14

age=input('Enter Age from <=30, 30-40, >40 : ')
income=input('Enter income from low, medium, high : ')
student=input('Enter student from yes, no : ')
cr=input('Enter credit rating from fair, excellent : ')

VYes=PYes*(DAge[age]['yes'])*DIncome[income]['yes']*DCredit[cr]['yes']*DStudent[student]['yes'];

VNo=PNo*(DAge[age]['no'])*DIncome[income]['no']*DCredit[cr]['no']*DStudent[student]['no'];
print()
print(VYes/(VYes+VNo));
print(VNo/(VYes+VNo));
print()


if(VYes>VNo):
  print('Buys Computer = Yes')
else:
  print('Buys Computer = No')