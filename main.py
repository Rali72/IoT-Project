
from db_handler import DbHandler
import configparser

from init_values import sites, actions, users, devices


def initData(db):
    for site in sites:
        exists = db.run_query_return(f"SELECT count(*) FROM SITES WHERE site_name='{site}';")
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            db.run_query(f"INSERT INTO SITES(site_name) VALUES('{site}')")

    for user in users:
        exists = db.run_query_return(f"SELECT count(*) FROM USERS WHERE user_name='{user}';")
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            db.run_query(f"INSERT INTO USERS(user_name) VALUES('{user}')")

    for device in devices:
        exists = db.run_query_return(f"SELECT count(*) FROM DEVICES WHERE device_name='{device}';")
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            db.run_query(f"INSERT INTO DEVICES(device_name) VALUES('{device}')")

    for action in actions:
        exists = db.run_query_return(f"SELECT count(*) FROM ACTIONS WHERE action_name='{action}';")
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            db.run_query(f"INSERT INTO ACTIONS(action_name) VALUES('{action}')")

    # TODO populate role_actions table


def populateSchema(db):
    is_db_exists = db.run_query_return("show databases;")
    if 'iot' not in [d[0].lower() for d in is_db_exists]:
        pass
        # TODO read the iot_schema.sql file and run it against database
    else:
        print('database already exists...')


if __name__ == "__main__":
    db_creds = configparser.ConfigParser()
    db_creds.read_file(open(r'db_creds.conf'))
    db_client = DbHandler(db_creds)

    populateSchema(db_client)
    initData(db_client)

    db_client.commit()









