class employee():
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destructor Called")

def Create_obj():
    print("Making Object...")
    obj = employee()
    print("function end...")
    return obj

print("Calling Create_obj() function...")
obj = Create_obj()
print("Program End")
