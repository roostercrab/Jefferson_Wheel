def remove_whitespace(data):
  output = "".join(data.split())
  print(output)

while True:
  data = input("Need input: ")

  remove_whitespace(data)
