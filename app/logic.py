from queries import execute_query
import time
import datetime

def attempt_login(username, password):
    cmd = "SELECT password FROM Users WHERE username = %s"
    ret = execute_query(cmd, (username, ))
    if ret and password in ret[0]:
        return True
    return False
    
def get_crimes(username):
    cmd = "SELECT lat, longitude, crime_desc, premis_desc, weapon_desc FROM Crimes NATURAL JOIN CrimeType NATURAL JOIN WeaponType NATURAL JOIN PremisType LIMIT 500"
    res = execute_query(cmd)
    ret = []
    for crime in res:
        if (crime[2] == None):
            continue
        info = f"Crime: {crime[2]}\nWeapon: {crime[4]}\nPremis: {crime[3]}"
        ret.append({"lat": crime[0], "lon": crime[1], "info": info})
    return ret
    
def desc_to_code(table:str, desc:str):
    res = execute_query(f"SELECT {table.lower()}_code FROM {table}Type WHERE {table.lower()}_desc = {desc}")
    return res[0][0]
def get_timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    print(attempt_login("User999", "password645"))