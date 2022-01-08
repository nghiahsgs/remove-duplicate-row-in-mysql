from utils_db import *
L_uid = [
    "100021968148403",
    "100023829460547",
    "100024662138138",
    "100029134202409",
    "100033738591790",
    "100036261524350",
    "100038246016276"
]
for uid in L_uid:
    print('uid',uid)
    L= User_info.select().where(User_info.uid == uid)
    for l in L[1:]:
        l.delete_instance()
        l.save()