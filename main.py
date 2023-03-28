
from db_handler import DbHandler
import configparser

if __name__ == "__main__":
    db_creds = configparser.ConfigParser()
    db_creds.read_file(open(r'db_creds.conf'))
    db_client = DbHandler(db_creds)

    # ... fill the roles and actions table like below...
    # db_client.run_query("INSERT INTO USERS (user_name) VALUES (Riaz)")
    #
    # db_client.run_query("INSERT INTO SITES (site_name) VALUES (home)")
    # db_client.run_query("INSERT INTO SITES (site_name) VALUES (office)")
    # db_client.run_query("INSERT INTO SITES (site_name) VALUES (hotel)")
    #
    # db_client.run_query("INSERT INTO DEVICES (device_name) VALUES (plug)")
    # db_client.run_query("INSERT INTO DEVICES (device_name) VALUES (fridge)")
    # db_client.run_query("INSERT INTO DEVICES (device_name) VALUES (plug)")
    #
    # devices = db_client.run_query_return("SELECT * FROM DEVICES")
    # print(devices)









