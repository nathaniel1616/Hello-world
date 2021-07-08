import os
os.chdir(r'C:\Users\yeboa\Desktop')

folder_names = 'pathology hvp GOC neuro disp_optics'.split()

# making folders
for folder in folder_names:
    os.rmdir(folder)