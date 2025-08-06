
# Life of developer starts  

#  excerise        --> actvity 
#  data --> symbol ( syntax)
#. reading data from others --> question --> variables   whatexcerisedo

whatexcerisedo ="yoga"
gymname="gym"


#  breakfast        --> actvity 
# data --> symbol ( syntax) "" , 
#. reading data from others -->
#. tuple 

breakfast= ("idly","chapti","sambar","chetani")
carrierbox=("snacks","food","sweet","tigfien")


#  travel to offcie   --> actvity 

#data 

fromstation="indiranagar"
tostation="mg road"
price=40

metro =[ [ 1,2,3 ], [1,2,3] , [1,2,3 ]   ]
print(metro[0])
metro[0].append(4)
print(metro[0])

metro[2].append(7)
print(metro)

metro[0].remove(2)
print(metro)

#  office space        --> actvity 

officecabs={ "dennis" : "sde2" , "laxman":"sde3 "  }
print(officecabs)
officecabs["dennis"] = "sde3";
print(officecabs)
officecabs.update({"venkatesh":"sed3"})
print(officecabs)

#  actual work         --> actvity 

company={"usa bank":[ {"dennis": ["ticket1","ticket2" ] }, { "venakt":"tocket4"},{"laxmi":"ticket5"}  ] }
 
print (company["usa bank"])

print (company["usa bank"][1]["venakt"])

for i in company.values():
     for j in i:
        print("employyes \n",j)
    


# code reusablity is called function is called activity 

def excerise():

    whatexcerisedo ="yoga"
    gymname="gym"
    

def  officespace():
     
    officecabs={ "dennis" : "sde2" , "laxman":"sde3 "  }
    print(officecabs)
    officecabs["dennis"] = "sde3";
    print(officecabs)
    officecabs.update({"venkatesh":"sed3"})
    print(officecabs)