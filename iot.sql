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
