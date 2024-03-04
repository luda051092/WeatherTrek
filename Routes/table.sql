-- City Table
CREATE TABLE City (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    population INTEGER,
    region VARCHAR(255),
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL (9, 6) NOT NULL,
    elevation DECIMAL(8,2),
);

-- WeatherCondition Table
CREATE TABLE WeatherCondition (
    id SERIAL PRIMARY KEY,
    condition_name VARCHAR(255) NOT NULL,
    description TEXT,
    icon_url VARCHAR(255),
);

-- Forecast Table
CREATE TABLE Forecast (
    id SERIAL PRIMARY KEY,
    city_id INTEGER REFERENCES City(id),
    weather_condition_id INTEGER REFERENCES WeatherCondition(id),
    temperature DECIMAL(5, 2) NOT NULL,
    feels_like DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    wind_speed DECIMAL(5, 2),
    precipitation DECIMAL(5, 2),
    timestamp TIMESTAMP NOT NULL,
    
);

-- HistoricWeather Table
CREATE TABLE HistoricWeather (
    historic_weather_id SERIAL PRIMARY KEY,
    city_id INTEGER REFERENCES City(id) ON DELETE CASCADE,
    weather_condition_id INTEGER REFERENCES WeatherCondition(id) ON DELETE CASCADE,
    temperature DECIMAL(5, 2) NOT NULL,
    humidity DECIMAL(5, 2),
    wind_speed DECIMAL(5, 2),
    precipitation DECIMAL(5, 2),
    timestamp TIMESTAMP NOT NULL,
    CONSTRAINT fk_city_historic_weather FOREIGN KEY (city_id) REFERENCES City(id) ON DELETE CASCADE,
    CONSTRAINT fk_weather_condition_historic_weather FOREIGN KEY (weather_condition_id) REFERENCES WeatherCondition(id) ON DELETE CASCADE
);


-- User Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL, -- Hashed and Salted
    city_location VARCHAR(255),
    post_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Comment Table
CREATE TABLE Comment (
    comment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_comment FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);


