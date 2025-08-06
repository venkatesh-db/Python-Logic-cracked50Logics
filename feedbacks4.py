
#  Input ,  argumnet variable  coding 
#  Loops 
#  Logic thinking --> Logic's  
#  Condition's 
#  Dict 


def autos(sound,location):
    
    if location == "magestic": #price variable is  depeneent on location variable 
         price=200
         
    elif location == "mg road":
         price=150
         
    # code in side the function block is ensured data is varied location , price 
         
    return price # get down at "mg road" bill given by auto 150 


rets=autos("auto","magestic")
print(rets)

rets=autos("auto","mg road")
print(rets)


def apartment( parcel , floor):
    
    # floor -->  house's  -- > to entire house codnitioon block satisfy name 
    if  parcel ==  "jamesbond" and floor == 3 :
        receievdparcel=True
        return {floor : receievdparcel }
        print(receievdparcel , "3rd floor")
    elif parcel ==  "suresh" and floor == 2 :
          receievdparcel=True
    elif parcel ==  "ramesh" and floor == 1 :
         receievdparcel=True
    

recev=apartment( "jamesbond", 3 )
print("return valiue",recev )


# Logic thinking

# Your family --> mother  ,                         father  

#                mother father | brother sister   mother father||  brother sister

#               [  { }                          ]  [                               ]

#              passedway  alive                   alive  alive 

# count -3 people  alive 
# count -- 90 years old lady 

family={"mother": [ {"ammamamma":True,"age":76 },{"devaraj":False,"age":82 }] , "father": [ {"longamma":True,"age":64} ,{ "jamesbondthata":True,"age":99}  ]  }

'''
for i,j in family.items():
     for k in j :
         if k["ammamamma"] == True:
             count =1
             print( "count",count)
         print("inner loop",k)
     print("smiles",i , j )
'''

family={"mother": [ {"ammamamma":True,"age":76,"alive":True},{"devaraj":False,"age":82,"alive":False }] , "father": [ {"longamma":True,"age":64,"alive":True} ,{ "jamesbondthata":True,"age":99,"alive":True}  ]  }

count=0
for i,j in family.items():
     for k in j :
         if k["alive"] == True:
             count = count +1
         print("inner loop",k)
     print("smiles",i , j )
     
print( "final count",count)