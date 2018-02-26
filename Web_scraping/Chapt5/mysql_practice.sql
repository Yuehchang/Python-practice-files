CREATE DATABASE scraping;

USE scraping;

CREATE TABLE pages ( id BIGINT(7) NOT NULL AUTO_INCREMENT, title VARCHAR(200),
content VARCHAR(10000), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));

DESCRIBE pages;

INSERT INTO pages (title, content) VALUES ('Test page title', 'This is some test page content. It can be up to 10,000 characters long.');

INSERT INTO pages (id, title, content, created) VALUES (3, 'Test page title', 'This is some test page content. It can be up to 10,000 characters long.', '2014-09-21 10:25:32');

SELECT * FROM pages WHERE id =2; 
SELECT * FROM pages WHERE title LIKE '%test%';

#Preparation for Unicode
ALTER DATABASE scraping CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

SELECT * FROM pages;

#############Six degree connection
CREATE DATABASE wikipedia;

USE wikipedia;

CREATE TABLE wikipedia.pages (id INT NOT NULL AUTO_INCREMENT, url VARCHAR(255) NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));

CREATE TABLE wikipedia.links (id INT NOT NULL AUTO_INCREMENT, fromPageId INT NULL, toPageId INT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));

ALTER DATABASE wikipedia CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE pages CHANGE url url VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

SELECT * FROM wikipedia.pages;
SELECT * FROM wikipedia.links;





