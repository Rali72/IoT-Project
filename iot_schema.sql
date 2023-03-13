create database IoT;
use IoT;
create table sites (
	site_id varchar(20) primary key,
	site_name varchar(100)
	);
create table devices (
	device_id varchar(20) primary key,
    device_name varchar(100)
    );
create table users (
	user_id int primary key,
    user_name varchar(100),
    email varchar(100)
    );
create table roles (
	role_id int primary key,
    role_name varchar(50)
    );
create table actions (
	action_id int primary key,
    action_name varchar(50)
    );
create table events (
	Date_time datetime primary key,
    type varchar(50),
    start_time datetime,
    end_time datetime
    );
alter table sites 
add foreign key(device_id)
references devices(device_id);

alter table users
add foreign key(role_id)
references roles(role_id);

create table sites_users(
	site_id varchar(50),
    user_id int,
    primary key (site_id,user_id),
    foreign key(site_id) references sites(site_id),
    foreign key(user_id) references users(user_id)
);

create table user_role(
	user_id int,
    role_id int,
    primary key (user_id, role_id),
    foreign key(user_id) references users(user_id),
    foreign key(role_id) references roles(role_id)
);
create table rol_action(
	role_id int,
    action_id int,
    primary key(role_id,action_id),
    foreign key(role_id) references roles(role_id),
    foreign key(action_id) references actions(action_id)
    
);

