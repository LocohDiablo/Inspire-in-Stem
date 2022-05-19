#learning about list
motorcycle_owner = "Mojo Jojo "
plate_number =['H1234','Y1234','S1234']
motorcycle = [ 'honda' , 'yamaha' , 'suzuki']
print(motorcycle[0])
# accessing list items using index
# print(motorcycle)
# motorcycle[1]= "Bugatti"#changing element in a ist



print(str(motorcycle[0]) + str(plate_number[0])) 
print(str(motorcycle[1]) + str(plate_number[1]))
#print(str(motorcycle[2]) + str(plate_number[2]))
#deleting an item from a list-- del
#del motorcyce[0] # deleting an item
#print(motorcycle
#popped_motorcycle =motorcycle.pop
 #pop removes the last index
#print(popped_motorcycle)
#task-- print a statement My name Mojo Jojo and I own a mortocycle plate number 
print("My name is {} and I own a {}  {}".format(motorcycle_owner,motorcycle[1],plate_number[1]))
#Removing an item from a list
motorcycle.remove("honda")
print(motorcycle)


#Loops
school = ['Joy' , 'Hope' ,'Mercy' ,'Happy']
pupil = ['Peace' ,'Patience' ,'Amani' , 'Charity']
print(f"I am {pupil[0]} from {school[0]} school")
print(f"I am {pupil[1]} from {school[1]} school")
print(f"I am {pupil[2]} from {school[2]} school")

#Simplified
for pupil in pupil:
 print(f'hello I am pupil {pupil}')