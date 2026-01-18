import os
print("===Environment Variable is Passed to Conatiner===\n")

for key,val in os.environ.items():
    print(key,"\n",val,"\n")
