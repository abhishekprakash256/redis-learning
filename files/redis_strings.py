"""
working with strings in redis db

"""

import redis



#make the connection

r = redis.Redis(host='localhost', port=6379, db=0)


#setting one value

r.set('Name', 'Abhi')

#setting multiple values

r.mset({"University" : "Florida State University" ,"Semster":"6th", "major" :"CS"})


#checking with for exists

if (r.exists("University")):
	print(r.get("University"))
else:

	print("Value not found")

r.incrby('address', 300)

#inscrease the value by 300 

r.incrby('address',300)

#printing the value

print(r.get('address'))





