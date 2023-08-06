import os
#  Give cwd as desktop
userprofile = os.environ['USERPROFILE']
print(userprofile)

desktop = os.path.join(userprofile, 'Desktop')
print(desktop)  # --> C:\Users\Dabba\Desktop
