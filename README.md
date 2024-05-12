# API Documentation

This documentation provides an overview of the API endpoints.

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

#### Request Parameters
- `drilldowns`: Specifies the level of detail for the data (e.g., 'State').
- `measures`: Specifies the type of measure to retrieve (e.g., 'Population').
- `geo`: Specifies the geographic regions to retrieve data for.

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

#### Request Parameters
- `measure`: Specifies the type of measures to retrieve (e.g., 'Commute Means by Gender').
- `geo`: Specifies the geographic regions to retrieve data for.
- `drilldowns`: Specifies the level of detail for the data (e.g., 'Vehicles Available').
- `year`: Specifies the year for which data is requested.

#### Response
```json
{
    "data": {
        "labels": ["vehicles_available_1", "vehicles_available_2", ...],
        "quantity": [6533475, 31012262, ...]
    }
}
```

