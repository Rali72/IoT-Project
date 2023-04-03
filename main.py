
from db_handler import DbHandler
import configparser

from init_values import sites, actions, users, devices, roles, role_action


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

    for role in roles:
        exists = db.run_query_return(f"SELECT count(*) FROM ROLES WHERE role_name='{role}';")
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            db.run_query(f"INSERT INTO ROLES(role_name) VALUES('{role}')")

    for role_act in role_action:
        exists = db.run_query_return(f"SELECT count(*) FROM ROLE_ACTION WHERE role_id='{role_act[0]}';")
        role_name = role_act[0]
        role_actions = role_act[1]
        if exists[0][0] == 0:  # don't add user if already exists (only for development purpose)
            for action in role_actions:
                insert_query =f"""INSERT INTO role_action (role_id, action_id) VALUES (
                (SELECT role_id FROM roles WHERE role_name = '{role_name}'),
                (SELECT action_id FROM actions WHERE action_name = '{action}'));"""
                db.run_query(insert_query)



def populateSchema(db):
    is_db_exists = db.run_query_return("show databases;")
    if 'iot' not in [d[0].lower() for d in is_db_exists]:
        with open('iot_schema.sql', 'r') as file:
            script = file.read()
            db.run_query(script)
    else:
        print('database already exists...')


if __name__ == "__main__":
    db_creds = configparser.ConfigParser()
    db_creds.read_file(open(r'db_creds.conf'))
    db_client = DbHandler(db_creds)

    populateSchema(db_client)
    # there is a bug, this only works if the database already exist
    initData(db_client)
    db_client.commit()
    print(db_client.run_query_return('select * from role_action'))








