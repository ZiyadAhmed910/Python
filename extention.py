filename = input("Input the Filename: ")
extn = filename.split(".")
if extn[-1] == 'py' :
  print("The extension of the file is : python")
elif extn[-1] =='c':
  print("The extension of the file is : c lang")
else :
  print ("The extension of the file is : " + repr(extn[-1]))
