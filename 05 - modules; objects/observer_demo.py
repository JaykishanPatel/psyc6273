import observer

student = observer.Observer(name = 'Sam', age = 21)
prof = observer.Observer(name = 'Anna', age = 43)

print("Obserber %s is %i years old" %(student.name, student.age))
print("Obserber %s is %i years old" %(prof.name, prof.age))

xpstep = 0
while student.runxp == True:
    student.time4break(xpstep)
    xpstep+=1
print("Experiment for %s stopped at %i "%(student.name, xpstep))

xpstep = 0
while prof.runxp == True:
    prof.time4break(xpstep)
    xpstep+=1
print("Experiment for %s stopped at %i "%(prof.name, xpstep))