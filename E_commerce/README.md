# MerchFlow API Documentation

## Overview

Welcome to the MerchFlow API Documentation! MerchFlow is your all-in-one eCommerce engine, built to handle everything from user accounts to product management, order processing, and beyond. With a robust backend powered by **Django**, a reliable **MySQL** database, and seamless collaboration through **Git** and **GitHub**, MerchFlow ensures a smooth, scalable, and efficient experience for developers and users alike.

Imagine effortlessly integrating your eCommerce operations into your application. Whether you're managing customer accounts, creating product catalogs, or automating order fulfillment, MerchFlow has you covered. Its clean, consistent API design makes it a breeze to get started, so you can focus on building amazing shopping experiences.

Key Features:

- **User Management**: Create, update, and manage customer accounts securely.
- **Product Catalog**: Organize and retrieve products with ease.
- **Order Management**: Handle orders, payments, and shipping seamlessly.
- **Category Listings**: Keep your inventory structured with categories.

Dive in and explore the powerful capabilities of the MerchFlow API. We've packed it with features to supercharge your eCommerce platform while keeping things intuitive for developers. Let the shopping revolution begin!

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [Rate Limiting](#rate-limiting)
4. [Endpoints](#endpoints)
   - [Accounts](#accounts)
   - [Categories](#categories)
   - [Products](#products)
   - [Orders](#orders)
5. [Request and Response Formats](#request-and-response-formats)
6. [Error Handling](#error-handling)
7. [Best Practices](#best-practices)
8. [FAQ](#faq)
9. [Contact Support](#contact-support)

---

## Getting Started

### Base URL

The API is hosted at the following base URL:

```
https://api.example.com/v1
```

### Prerequisites

- You need an API key to access the endpoints.
- Ensure your application handles HTTP requests and JSON responses.

---

## Authentication

The API supports multiple authentication schemes:

- **JWT Authentication**
- **Basic Authentication**
- **Cookie Authentication**

Include your API key or authentication token in the `Authorization` header of each request.

### Example

```http
Authorization: Bearer YOUR_API_KEY
```

---

## Rate Limiting

The API enforces rate limits to ensure fair usage:

- **Limit**: 1000 requests per hour per user.
- **Headers**: Rate limit information is included in the response headers.

Example headers:

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950
X-RateLimit-Reset: 1672531200
```

---

## Endpoints

### Accounts

#### List Accounts

**URL**: `/api/accounts/`

**Method**: `GET`

**Authentication**: Required (JWT, Basic, or Cookie)

**Description**: Retrieve a list of all user accounts.

**Response**:

```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
]
```

#### Create Account

**URL**: `/api/accounts/`

**Method**: `POST`

**Authentication**: Required

**Request Body** (JSON):

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "password2": "password123"
}
```

**Response**:

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

---

#### Retrieve Account Details

**URL**: `/api/accounts/{id}/`

**Method**: `GET`

**Authentication**: Required

**Description**: Retrieve details of a specific user by ID.

**Response**:

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

#### Update Account

**URL**: `/api/accounts/{id}/`

**Method**: `PUT` or `PATCH`

**Authentication**: Required

**Request Body** (JSON):

```json
{
  "email": "new_email@example.com"
}
```

**Response**:

```json
{
  "id": 1,
  "username": "john_doe",
  "email": "new_email@example.com"
}
```

#### Delete Account

**URL**: `/api/accounts/{id}/`

**Method**: `DELETE`

**Authentication**: Required

**Response**: HTTP 204 No Content

---

### Categories

#### List Categories

**URL**: `/api/categories/`

**Method**: `GET`

**Authentication**: Required

**Description**: Retrieve a list of all categories.

**Response**:

```json
[
  {
    "id": 1,
    "name": "Electronics",
    "slug": "electronics"
  }
]
```

#### Create Category

**URL**: `/api/categories/`

**Method**: `POST`

**Authentication**: Required

**Request Body** (JSON):

```json
{
  "name": "Electronics",
  "slug": "electronics"
}
```

**Response**:

```json
{
  "id": 1,
  "name": "Electronics",
  "slug": "electronics"
}
```

---

### Products

#### List Products

**URL**: `/api/products/`

**Method**: `GET`

**Authentication**: Required

**Description**: Retrieve a list of all products.

**Response**:

```json
[
  {
    "id": 1,
    "name": "Smartphone",
    "price": "699.99"
  }
]
```

#### Add Product to Cart

**URL**: `/api/products/{slug}/add-to-cart/`

**Method**: `POST`

**Authentication**: Required

**Request Body** (JSON):

```json
{
  "quantity": 2
}
```

**Response**:

```json
{
  "product": "Smartphone",
  "quantity": 2,
  "price": "699.99"
}
```

---

### Orders

#### Create Order

**URL**: `/api/orders/`

**Method**: `POST`

**Authentication**: Required

**Request Body** (JSON):

```json
{
  "items": [{"product_id": 1, "quantity": 2}],
  "shipping_address": "123 Main St"
}
```

**Response**:

```json
{
  "id": 1,
  "status": "pending",
  "total_amount": "1399.98"
}
```

---

## Request and Response Formats

### Request Headers

| Header          | Description                             |
| --------------- | --------------------------------------- |
| `Authorization` | Bearer token for authentication.        |
| `Content-Type`  | Set to `application/json` for POST/PUT. |

### Response Status Codes

| Status Code | Description                    |
| ----------- | ------------------------------ |
| `200`       | Request was successful.        |
| `201`       | Resource created successfully. |
| `204`       | No content.                    |
| `400`       | Bad request.                   |
| `401`       | Unauthorized access.           |
| `403`       | Forbidden action.              |
| `404`       | Resource not found.            |
| `500`       | Server error.                  |

---

## Error Handling

Errors follow a standard format:

```json
{
  "error": "Error message",
  "code": 400,
  "details": "Additional information (optional)."
}
```

---

## Best Practices

1. Use appropriate HTTP methods for each action (`GET`, `POST`, `PUT`, `DELETE`).
2. Leverage pagination for large data sets using `limit` and `offset` query parameters.
3. Handle errors gracefully and log them for debugging.
4. Cache responses where appropriate to reduce API calls.

---

## FAQ

### How do I reset my API key?

Visit the API settings page and click "Reset API Key."

### What is the maximum payload size?

The maximum payload size is 1 MB per request.

### Can I use the API without authentication?

No, authentication is mandatory for all requests.

---

## Contact Support

For further assistance, contact our support team:

- **Email**: [princeazuka99@gmail.com](mailto\:princeazuka99@gmail.com), [elmahallawy6@gmail.com](mailto\:elmahallawy6@gmail.com)
- **Phone**: +2348130718156, +201121404813
- **Hours**: Mon-Fri, 9 AM - 5 PM (GST+1)

---

Thank you for using the MerchFlow API!

