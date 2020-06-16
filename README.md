# IE-GalleryProject

create database, user in mysql commands:
create database gallery;
create user gallery_user@localhost identified by '1234';
grant all privileges on gallery.* to gallery_user@localhost;
flush privileges;