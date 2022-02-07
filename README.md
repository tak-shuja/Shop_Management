Project name: Shop_Management
Author: Shuja Tak
Description: This program will help you to manage all the customers with ease.


[+] How to use?

1. In terminal type: git clone https://www.github.com/tak-shuja/shop_management.git
2. Start mysql server.
3. Create a user and add a password.
4. Run the following queries in mysql terminal:
    1 "create databse customers;"
    2. "use customers;"
    3. "create table customers(
        id int not null auto_increment,
        name varchar(40) not null,
        adderess varchar(40) not null,
        paid varchar(10) not null,
        unpaid varchar(10) not null,
        primary key(id)
        );

    4. create table authentication(
        name varchar(20) not null,
        password varchar(25) not null
    );

    5. insert into authentication (name,password) values(
        "your_username, your_password")
        );

        This will be your username and password to delete records.

4. Run main.py

