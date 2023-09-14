# function to greet user
def hello():
  print("Hello, user!")

# function to take values and make a list
def pack(a,b,c):
    return [a,b,c]

#function to print sentences about what was eaten for lunch
def eat_lunch(a_list):
    if len(a_list) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(a_list)):
            if i == 0:
                print(f"First I eat {a_list[0]}")
            else:
                print(f"Then I eat {a_list[i]}")

# calling functions
hello()
print(pack("shoes", "shirts", "pants"))
eat_lunch([])
eat_lunch(["yogurt", "sandwich", "chips", "fruit snacks"])