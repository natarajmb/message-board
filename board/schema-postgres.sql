DROP TABLE IF EXISTS post;

CREATE TABLE post
(
    id      SERIAL PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author  TEXT      NOT NULL,
    message TEXT      NOT NULL
);