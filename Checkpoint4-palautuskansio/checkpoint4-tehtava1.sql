/*Create database named Keittio*/
CREATE DATABASE Keittio;

/*Open database*/
\c keittio;

/*Create table named Astia with parameters id, nimi, lkm*/
Create TABLE IF NOT EXISTS Astia
(id SERIAL PRIMARY KEY,
nimi varchar(255) NOT NULL,
lkm varchar(255));
