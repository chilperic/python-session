#!/usr/bin/env python
'''
Data structures
1. list
2. Dictionnaries
3.
'''
#function to sort groceries
def sort_gro(inp):
      if  type(inp) is list and  len(inp)!=0:
            print 22
      
       

groceries=['bananas','strawberries','apples','bread','armel']
#1.a
groceries.append('champagne')
#1.b
groceries.remove('armel')


#print sorted(groceries)

print sort_gro(groceries)
    #create a dictionaries  
Catalog ={
'Apples':7.3,
'Bananas':5.5,
'Bread':1.0,
'Carrots':10.0,
'Champagne':20.90,
'Strawberies':32.6
}
print Catalog
#2.c
Catalog['Strawberies']=63.43 #change the value inside the dictionnarie
#2.d
Catalog['chicken']=6.5 #to add in dictionaries
#del Catalog ['Bread']#remove  
print Catalog
for i in Catalog.keys():
      print i
#3.b
in_stock=Catalog.keys()
always_in_stock=tuple(in_stock)

print always_in_stock

print 'Come to shoprite! we always sel:'

for i in range( len(always_in_stock)):
      print i+1,':',always_in_stock[i],'\n'
      
      
#challenge question

Catalog_2 ={
'Apples':7.1,
'Bananas':5.0,
'Bread':2.0,
'Carrots':9.0,
'Champagne':20.0,
'Strawberies':30.6
}

main_Catalog ={'current_shop':Catalog,
        'other_shop':Catalog_2
}
