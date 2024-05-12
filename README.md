# API Documentation

This documentation provides an overview of the API endpoints.

## How to run

If you have Docker installed, just run the command below in the root folder:

```bash
docker-compose -f docker-compose.yml up --build
```
Otherwise you need to make sure you have `fastapi` (`pip install fastapi`) CLI installed and then run in the root folder:

```bash
fastapi run app/main.py --port 80
```
The API should be available at `http://localhost:80`

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
## Notes

It's a straightforward FastAPI application that consumes an external API. The endpoints don't have any GET parameters available for input, as we already define the parameters in the external API endpoints. Mapping all of these would be too time-consuming.

I've introduced a new GET parameter to the `/population` endpoint:

```js
{ 'geo': '04000US01,04000US12,04000US06' }
```

This filters data for Alabama, Florida, and California, saving us from looping through the entire array.

Next, I processed the response to make it more user-friendly for display in the frontend. In `utils.py`, you'll find the `extract_population_by_year` function, which organizes the final result like this:

```json
{
    "Alabama": [
        ["2013", 4799277],
        ["2014", 4817678],
        ["2015", 4830620]
        // ...
    ]
}
```

This function ensures that data is displayed in ascending order from 2013 to 2021.

I followed a similar approach for the `/cars-per-household` endpoint, resulting in a format like this:

```json
{
    "data": {
        "labels": ["vehicles_available_1", "vehicles_available_2", ...],
        "quantity": [6533475, 31012262, ...]
    }
}
```

This simplifies passing data to the chart component in the UI.

Due to time constraints, I chose not to prioritize writing tests or implementing linting tools and similar tasks. However, we can discuss these further in a meeting. My aim was to keep things as simple as possible and fulfill the requirements outlined in the document.
