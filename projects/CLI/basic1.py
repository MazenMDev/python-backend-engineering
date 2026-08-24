# add, search, update, delete

users = {}
while(True):
  print(users)
  action = input(
  """
    1.Add
    2.Search
    3.Update
    4.Delete

    write quit to exit
  """
  )


  if action == "1":
    name = input("Please Enter User Name: ")
    phone = input("Please Enter User phone number: ")
    email = input("Please Enter User email: ")
    users[name] = {"phone" : phone, "email": email}

  elif action == "2":
    nameToSearch = input("Please Enter the name you would like to search: ")
    if nameToSearch in users:
      print(users.get(nameToSearch))
    else: print("user not found")

  elif action == "3":
    nameToUpdate = input("Please Enter the name you would like to update: ")
    if nameToUpdate in users:
      newName = input("Please enter the new name: ")
      newPhone = input("Please enter the new phone: ")
      newEmail = input("Please enter the new email: ")
      users[newName] = {"phone": newPhone, "email": newEmail}
      if nameToUpdate != newName:
        users.pop(nameToUpdate)
    else: print("user not found")

  elif action == "4":
    nameToDelete = input("Please Enter the name you would like to delete: ")
    if nameToDelete in users:
      users.pop(nameToDelete)
    else: print("user not found")

  elif action == 'quit':
    break
