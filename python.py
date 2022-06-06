# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]= 'Andres'
# Change the value 20 in z to 30
z[0]['y']=30


# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(li):
    for x in range (0,len(li)):
        k = list(li[x].keys())
        v = list(li[x].values())
        Sen_print =""
        for i in range (0,len(k)-1):
            Sen_print += (f"{k[i]} _ {v[i]}, ")
        Sen_print += (f"{k[len(k)-1]} _ {v[len(v)-1]}")
        print (Sen_print)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
print(iterateDictionary(students)) 


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    k = key_name
    for x in range(0,len(some_list)):
        print(some_list[x][k])
print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))


# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]),x)
        for i in some_dict[x]:
            print(i)
        print('')

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(printInfo(dojo))
