# Prapanchang API

A FastAPI-based REST API for calculating Hindu calendar (Panchanga) details, festivals, and astrological information.

## Features

- Calculate Panchanga details for any date
- Get festival information for specific dates
- Location-based Panchanga calculations
- Timezone-specific calculations
- Built-in health check endpoint

## API Endpoints

### Get Panchanga Details
```http
GET /v1/panchanga?date=YYYY-MM-DD&timezone=Asia/Kolkata&city=Pune
```

### Get Festivals
```http
GET /v1/festivals?date=YYYY-MM-DD&timezone=Asia/Kolkata&city=Pune
```

### Get Location-based Panchanga
```http
GET /v1/calendars/coordinates/{latitude}/{longitude}/date/{date}?timezone=Asia/Kolkata
```

### Get Timezone Details
```http
GET /v1/timezone/{timezone}/date/{date}
```

### Health Check
```http
GET /v1/health
```

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd prapanchang
```

2. Create and activate virtual environment:
```sh
python3.10 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```sh
./script.sh
```

## Running the Application

### Local Development
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Using Docker
```sh
docker-compose up
```

## API Documentation

Once the application is running, access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

The project uses Bruno for API testing. To run the tests:

```sh
cd bruno_api_collection
bru run --env Local
```

## Dependencies

- FastAPI
- Uvicorn
- Jyotisha
- PySwissEph
- Sanskrit Data
- Additional packages listed in `script.sh`