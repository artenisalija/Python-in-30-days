#Code that Shows Python Version
import sys #importing sys module to access system-specific parameters and functions
print("Python version") #Displaying the Python version
print(sys.version) #Printing the version of Python being used
print("Version info.") #Displaying detailed version information
print(sys.version_info) #Printing detailed version information as a tuple

#Code that Shows Operating System Information
import platform #printing platform module to access underlying platform’s data
print("Operating System Information") #Displaying Operating System Information
print(platform.platform()) #Printing the platform information
print("System:", platform.system()) #Printing the system/OS name
print("Release:", platform.release())  #Printing the release version of the OS
print("Version:", platform.version()) #Printing the version of the OS

#Code that Shows Current Date and Time
from datetime import datetime #printing datetime module to work with dates and times
now = datetime.now() #printing current date and time
print("Current Date and Time") #Displaying Current Date and Time
print(now.strftime("%Y-%m-%d %H:%M:%S")) #Printing the current date and time in a specific format

#Code that show Envioronment Variables
import os #printing os module to interact with the operating system
print("Environment Variables")  #Displaying Environment Variables
for key, value in os.environ.items():   #Iterating through environment variables
    print(f"{key}: {value}")    #Printing each environment variable and its value
