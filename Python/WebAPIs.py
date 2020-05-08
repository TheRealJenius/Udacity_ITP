import requests # allows the use of web apis to gather data from the internet

r = requests.get("https://api.github.com/events") # assigning the object to a variable to make it easier to use

if r.status_code == 200: #checking the status code will ensure the program doesn't crash
    print("That was a valid URL")
    print(r.text) # prints out the data in the requests object (appears in a JSON format)
elif r.status_code == 404:
    print("The webpage could not be found, sorry")

else:
    print("Something went wrong...")
    #if a try statment is being used, the exception error is called 'requests.exceptions.ConnectionError'

print("Now to see the values in the code:")
giteve = r.json() #decodes the JSON data into data Python understands and sets it as a dictionary
print(giteve)
print("\nNow for the first dictionary in the list: ")
print(giteve[0])

for something in giteve[0]:
    print(something, giteve[0][something])
