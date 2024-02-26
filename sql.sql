create database shop;
create table customer
(First_Name char(50) not null,
Last_Name char(50),
Address char(50),
City char(50),
Country char(50)
);
use shop;
create table Members
(Member_ID int(50) not null primary key auto_increment,
Name nvarchar(50),
Email varchar(50),
Password varchar(50)
);
insert into Members(Member_ID,Name,Email,Password) values(NULL,'王小明','min@gmail.com','asd123');
insert into Members(Member_ID,Name,Email,Password) values(NULL,'王二明','min2@gmail.com','asd1234');
insert into Members values(null,'陳小三','chen3@gmail.com','chen33333333');
create table Products(
Product_ID int(50) not null primary key auto_increment,
Product_Name nvarchar(50),
Description text,
Price int(50),
Amount int(50),
Image nvarchar(50),
Date date,
Member_ID int(50),
foreign key(Member_ID) references Members(Member_ID)
);
insert into Products values(NULL,'紅筆','特別的紅筆',10,1,'/images/1','2024-01-18',1);
insert into Products values(NULL,'藍筆','特別的藍筆',10,1,'/images/2','2024-01-18',2);
insert into Products values(NULL,'黑筆','特別的黑筆',15,2,'/images/3','2024-01-18',1);
insert into Products values(NULL,'ADATA隨身碟','16GB',15,2,'/images/3','2024-01-19',2);
insert into Products values(NULL,'味全礦泉水','味全牌子的',10,100,'/images/3','2024-02-02',2);
insert into Products values(NULL,'愛之味麥茶','好喝的愛之味麥茶',20,30,'/images/3','2024-02-02',3);
insert into Products values(NULL,'藍芽耳機','雜牌LBT',500,5,'/images/3','2024-02-02',5);
insert into Products values(NULL,'光泉鮮乳','好喝又健康的鮮乳',150,5,'/images/3','2024-02-02',5);
insert into Products values(NULL,'林鳳營鮮乳','濃醇香',130,5,'/images/3','2024-02-02',5);
insert into Products values(NULL,'abc milk','omg',220,5,'/images/20','2024-02-05',5);
insert into Products values(NULL,'義美無加糖豆奶1000ml','1000ml,超好喝.',35,5,'./public/shop_static/picture/12/1.jpg','2024-02-17',5);
create table Carts(
Cart_ID int(50) not null primary key auto_increment,
Price int(50),
Amount int(50),
Member_ID int(50),
Product_ID int(50),
foreign key(Member_ID) references Members(Member_ID),
foreign key(Product_ID) references Products(Product_ID)
);
insert into Carts values(NULL,'');
insert into Carts values(NULL,10,1,8,1);
insert into Carts values(NULL,15,1,8,4);
insert into Carts values(NULL,10,15,7,6);
insert into Carts values(NULL,150,2,7,9);
create table Orders(
Order_ID int(50) not null primary key auto_increment,
Order_MID nvarchar(50) not null,
Price int(50),
Amount int(50),
Name nvarchar(50),
Phone int(50),
Address nvarchar(50),
Notes nvarchar(120),
Datetime datetime,
Product_ID int(50),
Seller_ID int(50),
Buyer_ID int(50),
foreign key(Product_ID) references Products(Product_ID),
foreign key(Seller_ID) references Members(Member_ID),
foreign key(Buyer_ID) references Members(Member_ID)
);
select * from Orders;
alter table Orders add Name nvarchar(50) after Amount;
alter table Orders add Notes nvarchar(120) after Address;
alter table Orders add Phone int(50) after Name;
alter table Orders add Order_MID int(50) after Order_ID;
ALTER TABLE Orders MODIFY COLUMN Order_MID nvarchar(50);
alter table Orders modify column Order_MID int(50) NOT NULL auto_increment ;
ALTER TABLE Orders CHANGE Order_MID Order_MID int(50) NOT NULL AUTO_INCREMENT;
alter table Orders modify Order_MID int(50) auto_increment;
TRUNCATE table Orders;
desc Orders;
alter table Orders add Address nvarchar(50) after Phone;
alter table Orders drop Name;
insert into Orders values(null,'random',100,100,'測試',0912345678,'台北市忠孝東路','筆記','2024-01-19 07:00:00',14,2,8);
insert into Orders values(null,15,1,'2024-01-19 07:00:00',3,1,2);
insert into Orders values(null,15,1,'2024-01-19 07:00:00',3,1,2);

drop table ;
truncate table Carts;
show databases;
use shop;
show tables;
select Email,Password from Members;
select Password,Name from Members where Email = "abc4@gmail.com";
select * from Members;
select Password from Members where Member_ID='8';
select * from Members where Member_ID='8';
update Members set Name='老67676' where Member_id=8;
select * from Products;
insert into Products values(NULL,'55','1',10,10,'','2024-02-20',8);
select * from Products where Product_ID=8;
delete from Products where Product_ID=24;
select * from Products where Member_ID=8;
select Product_ID from Products where Member_ID=1;
select Amount from Products where Product_ID=10;
delete from Products where Product_ID=22;
delete from Carts where Member_ID=8;
update Carts set Amount=2 where Member_ID=8 and Product_ID=10;
select * from Carts;
select * from Carts where Member_ID=8;
select * from Carts inner join Products on Carts.Product_ID=Products.Product_ID;
select Carts.Cart_ID,Carts.Price,Carts.Amount,Carts.Member_ID,Carts.Product_ID,Products.Product_Name,Products.Image from Carts inner join Products on Carts.Product_ID=Products.Product_ID where Carts.Member_ID=8;
select * from Orders;
select * from Orders where Buyer_ID=8;
describe Members;
update Products set Image ='./public/shop_static/picture/11/1.jpg' where Product_ID='11';
select Products.Product_ID,Products.Product_Name,Products.Description,Products.Price,Products.Amount,Products.Image,Products.Date,Products.Member_ID,Members.Name from Products inner join Members on Products.Member_ID=Members.Member_ID  where Product_ID=8;
select Orders.Order_ID,Orders.Order_MID,Orders.Price,Orders.Amount,Orders.Name,Orders.Phone,Orders.Address,Orders.Notes,Orders.Datetime,Orders.Product_ID,Orders.Seller_ID,Orders.Buyer_ID,Members.Name,Products.Product_Name from (Orders inner join Members on Orders.Seller_ID=Members.Member_ID) inner join Products on Orders.Product_ID=Products.Product_ID where Buyer_ID=8;
delete from Orders where Order_MID='YzuboyrMUg';


create user 'weichih-shop'@'%' identified by 'weichih-shop';
grant all privileges on shop.* to 'weichih-shop'@'%';

insert into customer (First_Name, Last_Name, Address, City, Country)
value ('王','小明','taiwan','','taipei')






