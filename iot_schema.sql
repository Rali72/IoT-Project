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
	event_id int primary key,
	Date_time datetime,type varchar(50),
    start_time datetime,
    end_time datetime
    );
create table devicedata(
	site_id varchar(20),
    device_id varchar(20),
    user_id int,
    event_id int,
    foreign key(site_id) references sites(site_id),
    foreign key(device_id) references devices(device_id),
    foreign key(user_id) references users(user_id),
    foreign key(event_id) references events(event_id)
);
create table role_action(
	user_id int,
    role_id int,
    action_id int,
    foreign key(user_id) references users(user_id),
    foreign key(role_id) references roles(role_id),
    foreign key(action_id) references actions(action_id)
);