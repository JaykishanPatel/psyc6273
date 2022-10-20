# Functions and classes can be imported defined in modules and imported in different scripts.
# As your project grows in complexity, you might end up with several modules.
# Instead of having your modules spread throughout your experiment's main directory,
# you might want to gather them into one same 'lib' directory. And import them so:

import mylib.mymod as mmod
import mylib.classes as cl

mmod.addit(20,30)
print(mmod.earth_radius_km)

# create a staircase object, i.e., an instance of the staircase class
s = cl.Stair(up=1, down=2)
student = cl.Observer(name = "Sam", age = "24")
