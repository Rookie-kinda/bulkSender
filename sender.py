from bulkSender import whatsend, dataHandler
from time import time


d = dataHandler("E:\مسجد العادل(دورة القران الكريم)\hadaba.xlsx", "excel")
data = d.check_siblings()

wa = whatsend(30)

nums = ["01151891134", "01151891134","01151891134","01151891134","01151891134","01151891134","01151891134","01151891134","01151891134","01151891134"]

# print(len(nums))
s = time()
for i in nums:
    wa.sendmsg(i, "test1")
e = time()

print(e - s)