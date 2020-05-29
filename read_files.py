employee_file = open("employees.txt", 'r')


for employee in employee_file.readlines():
# print(employee_file.read())
# print(employee_file.readline())
  # print(employee_file.readlines()[0])
  print(employee)

employee_file.close()
