phonebook = {
    "Sai": "9876543210",
    "Rahul": "9123456789",
    "Anu": "9988776655"
}
ask=input("enter the name:")
if ask in phonebook:
    print("Phone Number:", phonebook[ask])
else:
    print("Contact not found")
myself = {
    "name": "...",
    "age": ...,
    "college": "...",
    "branch": "...",
    "favorite_language": "Python"
}
for kay,value in myself.items():
    print(kay,value)