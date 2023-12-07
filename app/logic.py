from queries import execute_query, call_proc
import time
import datetime

def attempt_login(username, password):
    cmd = "SELECT password FROM Users WHERE username = %s"
    ret = execute_query(cmd, (username, ))
    if ret and password in ret[0]:
        return True
    return False


crime_dict = {}
res = execute_query("SELECT * FROM CrimeType")
for r in res:
    crime_dict[r[0]] = r[1]

weapon_dict = {}
res = execute_query("SELECT * FROM WeaponType")
for r in res:
    weapon_dict[r[0]] = r[1]
   
premis_dict = {} 
res = execute_query("SELECT * FROM PremisType")
for r in res:
    premis_dict[r[0]] = r[1]

def get_crimes(username, limit):
    cmd = f"getAll"
    stuff = [username, 0, ]
    res = call_proc(cmd, stuff)
    ret = []
    for crime in res:
        if (crime[2] == None):
            continue
        info = f"Crime: {crime_dict[crime[3]]}<br>Weapon: {weapon_dict[crime[5]]}<br>Premis: {premis_dict[crime[4]]}"
        ret.append({"lat": crime[1], "lon": crime[2], "info": info})
    return ret
    
def desc_to_code(table:str, desc:str):
    res = execute_query(f"SELECT {table.lower()}_code FROM {table}Type WHERE {table.lower()}_desc = {desc}")
    return res[0][0]

def get_timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    print(attempt_login("User999", "password645"))
    username = "Kyle"
    cmd = f"getAll"
    stuff = [username, 0, ]
    res = call_proc(cmd, stuff)
    print(res)