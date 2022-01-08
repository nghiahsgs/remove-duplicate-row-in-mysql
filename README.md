# remove-duplicate-row-in-mysql
remove duplicate row in mysql

## Now I have a table that have 5m rows
<img src="Screenshot_2.png"/>

## Here is 5 first sample datas
<img src="Screenshot_1.png"/>

## Now I want to see what uid is duplicate
<img src="Screenshot_3.png"/>

```sql
SELECT 
    uid, COUNT(uid)
FROM
    user_info
GROUP BY 
    uid
HAVING 
    COUNT(uid) > 1;
```

It taks 15s to show duplicated UID

## Run file index.py to remove duplicated UID
```
python index.py
```