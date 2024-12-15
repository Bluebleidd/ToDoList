CREATE TABLE your_app_board (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT DEFAULT ''
);

CREATE TABLE your_app_task (
    id SERIAL PRIMARY KEY,
    board_id INTEGER REFERENCES your_app_board(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT DEFAULT '',
    status VARCHAR(10) CHECK (status IN ('TO DO', 'DOING', 'DONE')) NOT NULL DEFAULT 'TO DO'
);