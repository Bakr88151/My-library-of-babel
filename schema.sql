CREATE TABLE pages(
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    date NUMERIC DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
);
CREATE INDEX index_content ON pages(content);