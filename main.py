import atexit
import sys
import os
from DTO import Order, Hat, Supplier

if os.path.exists("database.db"):
    os.remove("database.db")
from Repository import *


def main(argv):
    repo = Repository(argv)
    atexit.register(repo.close)
    repo.create_tables()
    configFile = argv[1]
    ordersFile = argv[2]
    output = argv[3]
    readFile(configFile, repo)
    orders(ordersFile, output, repo)


def readFile(configFile, repo):
    with open(configFile) as file:
        sizes = file.readline().replace("\n", "").split(",")
        numOfHat = sizes[0]
        numOfSuppliers = sizes[1]
        for i in range(0, int(numOfHat)):
            hat = file.readline().replace("\n", "").split(",")
            repo.hats.insert(Hat(*hat))
        for i in range(0, int(numOfSuppliers)):
            supplier = file.readline().replace("\n", "").split(",")
            repo.suppliers.insert(Supplier(*supplier))


def orders(ordersFile, output, repo):
    outputFile = open(output, "a")
    with open(ordersFile) as file:
        orderId = 1
        for line in file:
            order = line.replace("\n", "").split(",")
            location = order[0]
            topping = order[1]
            hat = repo.hats.find(topping)
            repo.hats.update(hat.id)
            supplier = repo.suppliers.find(hat.supplier)
            repo.orders.insert(Order(orderId, location, hat))
            outputFile.write(str(topping) + "," + supplier.name + "," + str(location)+"\n")
            orderId += 1


if __name__ == '__main__':
    main(sys.argv)
