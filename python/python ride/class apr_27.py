#page no.50 problems

#9
'''l=[1,5,6,2,5,10,6,20,30,18,5]
r=[]
for i in l:
	if i not in r:
		r.append(i)
	
print(r)'''


#pg.no.60     prbm :   # 6



"""my_dict = {'data1':100,'data2':54,'data3':247}
r=1
for i in my_dict:
    r=r*my_dict[i]
print(r)"""



#pg.no. 60      #7


'''d = {'Red': 1, 'Green': 2, 'Blue': 3}
for i in d:
    print(i,'corresponds to ',d[i])'''
    
    
    
   #pg.no. 6     #8 
   
'''d = {4: 1, 5: 2, 6: 3}
x=d.keys()
print(sorted(x))'''
   
   
   
#9

'''d={}
s='rguktbasar'
for i in s:
   d[i]=s.count(i)
   
print(d)'''



#10

'''d={'raju':[30,40,50,60],'ravi':[100,70,60,40],'ramesh':[80,80,70,90],'rakesh':[90,90,100,70]}
total={}
for i in d:
    total[i]=sum(d[i])
    
print(total)
for j in total:
    if(total[j]==max(total.values())):
        print('topper is ',j,'marks is',total[j])'''
        
        
#5  

'''student_data = {'id1':

{'name': ['Sara'],

'class': ['V'],'subject_integration': ['english, math, science']

},

'id2':

{'name': ['David'],

'class': ['V'],

'subject_integration': ['english, math, science']

},

'id3':

{'name': ['Sara'],

'class': ['V'],

'subject_integration': ['english, math, science']

},

'id4':

{'name': ['Surya'],

'class': ['V'],

'subject_integration': ['english, math, science']

}}

r={}
for i,j in student_data.items():
    if(j not in r.values()):
        r[i]=j
        
print(r)'''
        
    