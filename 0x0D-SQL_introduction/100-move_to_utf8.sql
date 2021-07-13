-- move to utf8
CREATE TABLE first_table(
    id int(11) DEFAULT NULL,
    name varchar(256)
    CHARACTER SET utf8
    COLLATE=utf8mb4_unicode_ci
)
