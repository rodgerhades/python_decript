print("hello, contosoville!")
#this is a comment that won't be interpreted as a command.

#associate variable town with the value "contosoville"
town = " contosoville "

#print a message about the secret location
print(" the town i am looking for is "+town)

#define a power (function) to chant a phrase
def chant( phrase ):
    #glue three copies together and print it as a message
    print( phrase + phrase + phrase )
    
#invoke the power to chant on the phrase "Contosoville!"
chant(" Contosoville! ")