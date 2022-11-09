# workshop08.py  Lecture 8 workshop problems

# The Keeling curve shows the atmospheric concentration of carbon dioxide
# from 1958 to the present. This data is given in the accompanying file
# keeling.csv. Fit a curve (choose any curve you think might make a good fit)
# to the interpolated concentration (seventh column) versus the decimal year
# (fourth column). Plot the data and the fitted curve.

# If you would like suggestions about how to do this, here are some steps
# you could take.

# 1. Use np.loadtxt() to load the data from keeling.csv. Note that the data
# file uses an unusual comment character, and has comma-separated values.
# In the resulting DataFrame, keep just the two columns that you will need.

# 2. If you plot the data, you will see that there are some missing values,
# indicated by negative CO2 concentrations. Use boolean indexing to remove
# these rows.

# 3. Often a good approach to a complex problem is to start with a simplified
# version. The data is clearly not linear, but try starting with a linear
# fit anyway, i.e., y = p[0]*x + p[1], where p is an array of parameters.
# Use a sum-of-squares error function. Whether your fitting routine works or
# not may depend on your initial guess as to the parameters, so try something
# that's at least in the right ballpark, such as the parameters for a straight
# line through the first and last data points.

# 4. Next try improving the fit by using a more flexible fitting function.
# Try a second-order polynomial: y = p[0]*(x**2) + p[1]*x + p[2]. You could
# use an initial guess with p[0]=0, and the other two parameters initialized
# as in the linear fit.

# 5. Now try also fitting the annual variation that is evident in the data.
# Fit a second-order polynomial plus sinusoidal variation with a period of
# one year: y = p[0]*(x**2) + p[1]*x + p[2] + p[3]*np.sin(2*np.pi*x-p[4]).
# Parameter p[3] controls the amplitude of the sine wave, and p[4] controls
# the phase, i.e., at what time during the year the curve peaks.
