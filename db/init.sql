CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    status TEXT NOT NULL,
    applied_on DATE DEFAULT CURRENT_DATE
);
