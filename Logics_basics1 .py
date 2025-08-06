
# Owner house --> servant1- cook ,servant2-cleaning  
# monthly pay 7000   servant1- 6 working days   servant2- 6 working days 
# outcome --> leaves's taken - 5 1250-7000  monthlysalary 7000 perday-250 


def ownerhouse(): 
    
    # servant salary 
    househelper= [ {"ramya":7000,"work":"goodworker" }  ,{ "divya":7500,"work":"ok"}]
    #requirement how to fit data in specific data structure 
    
    # outcome logic -- variables 
    calculatedays= 25
    payperday =250 
    
    # memory acessing  --> index key 
    # servant1-> index 0 , servant name -> ramya 
    househelper[0]["ramya"] =7000
    
    # we are apying two servant we need two if statement's 
    # Condition        -->  memory acessing
    
    # servant1-> index 0
    # servant2-> index 1
    
    if househelper[0]["work"] == "goodworker":
        fullpay=7000
        print("full pay",fullpay)
    if househelper[1]["work"] == "ok":
        # logics
         househelper[1]["divya"] = payperday * calculatedays
         # servent memory data is overwritten with logic variables memory ]
         # copy of logic data in to househelper index 1 -servant2 
         
         print( househelper)
             
    # loops            ---> memory acessing --> one dict
    for i in househelper: 
        print("loop",i)
        
#ownerhouse()

def Looping():
    
    helpers=["ramya","divya"]
    servants={"ramya":7000,"work":"goodworker" } 
    
    # looping meory acessing. --> index , key or value 

    for i in helpers : # value 
        print(i)
        
    for i,j in enumerate(helpers): #index value 
        print(i,j)
        
    for i in servants.values(): # value 
        print(i)
    
    for i,j in servants.items(): # index, value 
        print(i,j)
        
        
Looping()