CREATE TABLE IF NOT EXISTS training_images (
	date			VARCHAR(40) 		NOT NULL,
	color			VARCHAR(10)			NOT NULL,
	img				BYTEA				NOT NULL,
	
	CONSTRAINT pk_train_date PRIMARY KEY (date)
);

CREATE TABLE IF NOT EXISTS datasets_by_date (
	dataset			SERIAL,
	date			VARCHAR(40) 		NOT NULL,

	CONSTRAINT pk_data_set PRIMARY KEY (dataset)
);

CREATE TABLE IF NOT EXISTS datasets_content (
	id				SERIAL,				
	color			VARCHAR(10) 		NOT NULL,
	rgb				integer[3]			NOT NULL,
	dataset			int					NOT NULL,
	
	CONSTRAINT pk_cont_id PRIMARY KEY (id),
	CONSTRAINT fk_cont_data FOREIGN KEY (dataset) REFERENCES datasets_by_date(dataset)
);

DROP TABLE IF EXISTS masks;
CREATE TABLE masks (
	color			VARCHAR(10),				
	hsv_min			integer[3] 			NOT NULL,
	hsv_max			integer[3]			NOT NULL,
	
	CONSTRAINT pk_masks_color PRIMARY KEY (color)
);
	
INSERT INTO masks (color, hsv_min, hsv_max)
VALUES
	('Blue', '{91, 90, 50}', '{102, 255, 128}'),
	('Yellow', '{18, 119, 116}', '{30, 255, 255}'),
	('Green', '{49, 148, 48}', '{70, 255, 156}'),
	('Orange', '{0, 160, 134}', '{7, 255,  255}'),
	('Red', '{91, 181, 109}', '{179,  255, 173}'),
	('Pink', '{163, 145, 108}', '{168, 255, 217}');