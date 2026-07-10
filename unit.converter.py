
print("--------UNIT CONVERTER-------")

available_conversions = [(1,'kg',"gm"),
                         (2,"km","m"),
                         (3,"km","mi"),
                         (4,"miles","foot"),
                         (5,"foot","inches"),
                         ]

print("Available_conversions: ",available_conversions)

for conversion_num, from_units,to_units in available_conversions:
    print(f"{conversion_num}) {from_units} -> {to_units}")

converting = input("Enter the index of conversion to execute: ")
convertion_index = int(converting) - 1

conversion_num,from_units,to_units = available_conversions[convertion_index]
from_value = float(input("Enter value to convert: "))
print("from_value: ", from_value)

if convertion_index == 1:
  to_value = from_value * 1000
  print(from_value,from_units,"=",to_value,to_units)
elif convertion_index == 2:
  to_value = from_value * 1000
  print(from_value,from_units,"=",to_value,to_units)
elif convertion_index == 3:
  to_value = from_value * 0.62
  print(from_value,from_units,"=",to_value,to_units)
elif convertion_index == 4:
  to_value = from_value * 5280
  print(from_value,from_units,"=",to_value,to_units)
elif convertion_index == 5:
  to_value = from_value * 12
  print(from_value,from_units,"=",to_value,to_units)
else:
  print("Invalid index")
