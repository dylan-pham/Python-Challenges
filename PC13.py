import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(server.system.listMethods())
print(server.phone("Bert")) # from python challenge 12, check PC13.jpg, "Bert is evil"

# 555-ITALY