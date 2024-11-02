# My RESTful API

This project is a simple RESTful API built using Django and Django REST Framework (DRF), without a database. The data is stored in an in-memory list for demonstration purposes.

## Project Setup

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- Django and Django REST Framework

### Installation

1. **Clone the Repository**:
    git clone <your-repository-url>
    cd my_rest_api

2. **Create a Virtual Environment** (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:
    pip install django djangorestframework

4. **Run the Server**:
    python manage.py runserver

5. **Access the API**:
   Open your browser and navigate to `http://127.0.0.1:8000/api/cars/` to access the API endpoints.

---

## API Documentation

This API allows you to manage a collection of cars with basic CRUD (Create, Read, Update, Delete) operations. Below are the available endpoints and example requests.

### Endpoints

1. `GET /api/cars/` - List all cars
2. `POST /api/cars/` - Create a new cars
3. `GET /api/cars/<id>/` - Retrieve a specific car by ID
4. `PUT /api/cars/<id>/` - Update a car by ID
5. `DELETE /api/cars/<id>/` - Delete a car by ID

### Data Structure

Each car entry has the following fields:
- `id` (integer, auto-generated)
- `model` (string)
- `brand` (string)
- `registration_date` (date in 'YYYY-MM-DD' format)

---

## Example Requests Using Postman

### 1. List All Cars

- **Endpoint**: 'GET /api/cars/'
- **Description**: Retrieve a list of all cars.
  
#### Postman Request
1. Open Postman and select **GET** as the HTTP method.
2. Enter `http://127.0.0.1:8000/api/cars/` as the request URL.
3. Click **Send**.

#### Expected Response
```json
[
    {
        "id": 1,
        "model": "Z4",
        "brand": "BMW",
        "registration_date": "2024-11-01"
    },
    {
        "id": 2,
        "model": "C Class",
        "brand": "Mercedes-Benz",
        "registration_date": "2024-11-02"
    }
]
```

---

### 2. Create a New Car

- **Endpoint**: `POST /api/cars/`
- **Description**: Add a new car to the collection.

#### Postman Request
1. Open Postman and select **POST** as the HTTP method.
2. Enter `http://127.0.0.1:8000/api/cars/` as the request URL.
3. In the **Body** tab, select **raw** and **JSON** as the format.
4. Enter the JSON data for the car, for example:
    ```json
    {
        "model": "Z4",
        "brand": "BMW",
        "registration_date": "2024-11-01"
    }
    ```
5. Click **Send**.

#### Expected Response
```json
{
    "id": 1,
    "model": "Z4",
    "brand": "BMW",
    "registration_date": "2024-11-01"
}
```

---

### 3. Retrieve a Car by ID

- **Endpoint**: `GET /api/cars/<id>/`
- **Description**: Retrieve details of a specific car by its ID.

#### Postman Request
1. Open Postman and select **GET** as the HTTP method.
2. Enter `http://127.0.0.1:8000/api/cars/1/` (replace `1` with the desired car ID).
3. Click **Send**.

#### Expected Response
```json
{
    "id": 1,
    "model": "Z4",
    "brand": "BMW",
    "registration_date": "2024-11-01"
}
```

---

### 4. Update a Car by ID

- **Endpoint**: `PUT /api/cars/<id>/`
- **Description**: Update the details of a specific car by its ID.

#### Postman Request
1. Open Postman and select **PUT** as the HTTP method.
2. Enter `http://127.0.0.1:8000/api/cars/1/` (replace `1` with the car ID you want to update).
3. In the **Body** tab, select **raw** and **JSON** as the format.
4. Enter the updated JSON data, for example:
    ```json
    {
        "model": "Boxster S",
        "brand": "Porsche",
        "registration_date": "2024-10-31"
    }
    ```
5. Click **Send**.

#### Expected Response
```json
{
    "id": 1,
    "model": "Boxster S",
    "brand": "Porsche",
    "registration_date": "2024-10-31"
}
```

---

### 5. Delete a Car by ID

- **Endpoint**: `DELETE /api/cars/<id>/`
- **Description**: Delete a specific car by its ID.

#### Postman Request
1. Open Postman and select **DELETE** as the HTTP method.
2. Enter `http://127.0.0.1:8000/api/cars/1/` (replace `1` with the car ID you want to delete).
3. Click **Send**.

#### Expected Response
- Status code `204 No Content` (indicating successful deletion).

---

## Error Handling

The API will respond with appropriate status codes for errors:

- `404 Not Found`: When a car with the specified ID does not exist.
- `400 Bad Request`: For invalid input data during creation or update.
- `405 Method Not Allowed`: If an unsupported HTTP method is used on an endpoint.

---

## Project Structure

```plaintext
my_rest_api/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── my_rest_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```