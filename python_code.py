#============================
# by thitipong.s.th  
# compiler python3.6 
# ===========================

# x  = [12,4,5,6,43,4]
# y = [2,23,4,5,6,43]

z = [] 
x = ['B', 'F', 'G', 'H', 'J', 'K']
y = ['S', 'B', 'G', 'I', 'H', 'K']

assert_z = ['S', 'B', 'F', 'G', 'I', 'H', 'J', 'K']

def print_xyz_and_next_match():
  print(" print xyz and next match ") 
  print(" x = " ,x)
  print(" y = " ,y)
  print(" z = " ,z)
  pos1   = get_samech_first_index()
  print("next match  [x , y] = ",  pos1  )
  return pos1 

def get_samech_first_index():
  idx1 = 0 
  for xi in x :
    idx1 = idx1 + 1 
    idy1 = 0
    for yi in y: 
      idy1 = idy1 +1 
      if(xi == yi): 
        #print(xi," " , yi , "POS x y = " , idx1, " " , idy1)
        return [idx1,idy1]

pos1 = print_xyz_and_next_match()
#pos1   = get_samech_first_index()
#print("next match  [x , y] = ",  pos1  )
MAX_LOOP = 15
for int_loop in range(MAX_LOOP): 
  print( " ======= Loop " + str(int_loop+1) + " =============")
  if (pos1[0] != 1 and pos1[1] !=1 ):
    print( " >>> x and y not match at 1  " )
    x0 = x[0]
    y0 = y[0]
    if( x0 < y0 ):
      z1 = x.pop(0)
      print (">>> x0 < y0 " , x0 , " < " , y0 , " pop x " , z1)
    else:
      z1 = y.pop(0)
      print (">>> x0 >= y0 " , x0 , " >= " , y0 , " pop y " , z1 )
    z.append(z1)
  else:
    if(pos1[0]== 1 and pos1[1]!=1 ): # x is match only , pop y 
      y0 = y.pop(0)
      print(" >>>> pop y ", y0)
      z.append(y0)
    elif(pos1[0]!= 1 and pos1[1]==1 ): # y is match only , pop x 
      x0 = x.pop(0)
      print(" >>>> pop x ", x0)
      z.append(x0)
    elif(pos1[0]== 1 and pos1[1]==1 ): # x and y is match , pop x y  
      x0 = x.pop(0)
      y0 = y.pop(0)
      if(x0 != y0 ):
        print("ERROR x0 != y0 ")
        exit() 
      print(" >>>> pop x and y ", x0, " " , y0 )
      z.append(x0) 
    else:
      print( "ERROR unknown case ")
      exit()

  pos1 = print_xyz_and_next_match() 
  if pos1 == None : 
    print(" >> some array empty , Exit loop !!  ")
    break; 

print("=============================")
# ==== after loop until some queue empty  
while len(x)!=0:
  x0 = x.pop(0)
  z.append(x0 ) 
  pos1 = print_xyz_and_next_match() 
while len(y)!=0:
  y0 = y.pop(0)
  z.append(y0 ) 
  pos1 = print_xyz_and_next_match() 
  
print("=============================")
if( z == assert_z):
  print (" calulate ok ")
else: 
  print (" caculate failed ")
