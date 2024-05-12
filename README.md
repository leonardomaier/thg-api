# API Documentation

This documentation provides an overview of the API endpoints.

## How to run

If you have Docker installed, just run:

```bash
docker-compose -f docker-compose.yml up --build
```
Otherwise you need to make sure you have `fastapi` (`pip install fastapi`) CLI installed and then run:

```bash
fastapi run app/main.py --port 80
```

## Overview

The API offers two endpoints:
1. `/population`: Retrieves population statistics by state.
2. `/cars-per-household`: Retrieves commute means by gender and vehicles available per household.

## Endpoints

### 1. `/population`

#### Method
- GET

#### URL
- `/population`

#### Description
Retrieves population statistics by state.

#### Response
```json
{
    "Alabama": [
        [
            "2013",
            4799277
        ],
        [
            "2014",
            4817678
        ],
        [
            "2015",
            4830620
        ]
        // ...
    ]
}
```

### 2. `/cars-per-household`

#### Method
- GET

#### URL
- `/cars-per-household`

#### Description
Retrieves vehicles available per household.

#### Response
```json
{
    "data": {
        "labels": ["vehicles_available_1", "vehicles_available_2", ...],
        "quantity": [6533475, 31012262, ...]
    }
}
```

