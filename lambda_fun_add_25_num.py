input_number = int(input("enter the number: "))
def lambda_add(input_number):
    add_25 = lambda x: x + 25
    result = add_25(input_number)
    print(result)
lambda_add(input_number)
#output - suppose input number is 25 then the output would be 50
