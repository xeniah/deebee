from lib.TableNoIndex import  TableNoIndex
from lib.TableWithIndex import TableWithIndex
import time

testRange = 500000

###############################
tni = TableNoIndex()
r = {"name": "Orion", "age": "28", "height": 188, "weight": 80}


for i in range(testRange):
    res = tni.insert(r)

print("get by id")
res = tni.getById(1)

start = int(round(time.time() * 1000))
print("find by name")
res = tni.getByAttribute("name", "Orion")
end = int(round(time.time() * 1000))
print("Res length: " + str(len(res)))
print(str(end - start) + "ms")

#Res length: 1000000000
#161807ms
################################

twi = TableWithIndex()
twi.createIndex("name")
r = {"name": "Newton", "age": "82", "height": 171, "weight": 80}
for i in range(testRange):
    twi.insert(r)

start = int(round(time.time() * 1000))
print("find by name")
res = twi.getByAttribute("name", "Newton")
end = int(round(time.time() * 1000))
print("Res length: " + str(len(res)))
print(str(end - start) + "ms")

# find by name
# Res length: 1000000000
# 164554ms
#
#