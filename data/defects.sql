-- qa_stations table
CREATE TABLE IF NOT EXISTS qa_stations (
	id integer PRIMARY KEY,
	name text NOT NULL,
);

CREATE TABLE IF NOT EXISTS defect_types (
	id integer PRIMARY KEY,
	name text NOT NULL,
);

-- defects table
CREATE TABLE IF NOT EXISTS defects (
	id integer PRIMARY KEY,
	serial_number text NOT NULL,
	location text NOT NULL,
	origin text NOT NULL,
	type text NOT NULL,
	cause text NOT NULL,
	date text NOT NULL,
	time text NOT NULL,
	FOREIGN KEY (found) REFERENCES qa_stations (id)
);