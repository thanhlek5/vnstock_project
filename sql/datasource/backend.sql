CREATE TABLE IF NOT EXISTS sectors (
	sector_id SERIAL PRIMARY KEY, 
	sector_code INT, 
	sector_name VARCHAR(255),
	sector_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT sector_unique UNIQUE (sector_code,sector_name)
);
CREATE TABLE IF NOT EXISTS industry_groups(
	group_industry_id SERIAL PRIMARY KEY,
	group_industry_sector_id INT,
	group_industry_code INT,
	group_industry_name VARCHAR(225),
	group_industry_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT group_industry_unique UNIQUE (group_industry_name,group_industry_code),
	CONSTRAINT fk_group_industry_sector_id FOREIGN KEY (group_industry_sector_id) REFERENCES sectors(sector_id)
);
CREATE TABLE IF NOT EXISTS industries(
	industry_id SERIAL PRIMARY KEY, 
	industry_group_id INT, 
	industry_code INT, 
	industry_name VARCHAR(225), 
	industry_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT industry_unique UNIQUE (industry_name,industry_code),
	CONSTRAINT fk_industry_group_id FOREIGN KEY (industry_group_id) REFERENCES industry_groups(group_industry_id)
);
CREATE TABLE IF NOT EXISTS subindustries(
	subindustry_id SERIAL PRIMARY KEY, 
	subindustry_industry_id INT, 
	subindustry_code INT, 
	subindustry_name VARCHAR(225),
	subindustry_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT subindustry_unique UNIQUE (subindustry_code,subindustry_name),
	CONSTRAINT fk_sub_industry_id FOREIGN KEY (subindustry_industry_id) REFERENCES industries(industry_id)
);
CREATE TABLE IF NOT EXISTS stock_groups(
	stock_group_id SERIAL PRIMARY KEY,
	stock_group_code CHAR(10),
	stock_group_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS exchanges(
	exchange_id SERIAL PRIMARY KEY, 
	exchange_code CHAR(10),
	exchange_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 
CREATE TABLE IF NOT EXISTS companies(
	company_id SERIAL PRIMARY KEY, 
	company_name VARCHAR(225), 
	company_profile TEXT, 
	company_issue_share BIGINT, 
	company_charter_capital BIGINT, 
	company_financial_ratio_issue_share BIGINT, 
	company_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS tickers(
	ticker_id SERIAL PRIMARY KEY, 
	ticker_exchange_id INT, 
	ticker_company_id INT, 
	ticker_sub_id INT, 
	ticker_group_id INT, 
	ticker_type CHAR(50),
	ticker_time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	CONSTRAINT fk_ticker_exchange_id FOREIGN KEY (ticker_exchange_id) REFERENCES exchanges(exchange_id),
	CONSTRAINT fk_ticker_company_id FOREIGN KEY (ticker_company_id) REFERENCES companies(company_id),
	CONSTRAINT fk_ticker_subindustry_id FOREIGN KEY (ticker_sub_id) REFERENCES subindustries(subindustry_id),
	CONSTRAINT fk_ticker_group_id FOREIGN KEY (ticker_group_id) REFERENCES stock_groups(stock_group_id)
);
CREATE INDEX idx_ticker_time_stamp ON tickers(ticker_time_stamp);
CREATE INDEX idx_ticker_company_id ON tickers(ticker_company_id);
CREATE INDEX idx_ticker_exchange_id ON tickers(ticker_exchange_id);
CREATE INDEX idx_ticker_subindustry_id ON tickers(ticker_sub_id);
CREATE INDEX idx_ticker_group_id ON tickers(ticker_group_id);







