Project name: Shop_Management.
Author: Shuja Tak.
Description: This program will help you to manage all the customers with ease.


[+] How to use?

* In terminal type: git clone https://www.github.com/tak-shuja/shop_management.git
* Start mysql server.
* Create a user and add a password.
* Run the following queries in mysql terminal:  
    * "create databse customers;"
    * "use customers;"
    * "create table customers(
        id int not null auto_increment,
        name varchar(40) not null,
        adderess varchar(40) not null,
        paid varchar(10) not null,
        unpaid varchar(10) not null,
        primary key(id)
        );

    * create table authentication(
        name varchar(20) not null,
        password varchar(25) not null
    );

    * insert into authentication (name,password) values(
        "your_username, your_password")
        );

        This will be your username and password to delete records.

4. Run main.py

