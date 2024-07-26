# 🍽️ Food Information CLI Tool and API

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [CLI Commands](#cli-commands)
  - [CLI Examples](#cli-examples)
- [API Documentation](#api-documentation)
  - [Endpoints](#endpoints)
  - [API Examples](#api-examples)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This project provides both a Command Line Interface (CLI) tool and a RESTful API that offer information about various food items. Users can list, search, and retrieve details about different foods, as well as sign up for notifications about specific items.

## 🚀 Features

- 📊 List food items with pagination
- 🔍 Search functionality for food items
- 📋 Detailed view of individual food items
- 📨 Email notification sign-up for specific food items
- 📍 Location-based search using zipcode and distance
- 🔗 RESTful API for programmatic access to food data

## 💻 Technology Stack

- **Language**: Python 3.x
- **Web Framework**: Flask
- **CLI Libraries**: argparse, tabulate, json
- **Data Source**: Custom FoodRepository class

## 🏁 Getting Started

### Prerequisites

- Python 3.x
- pip3 (Python package manager)

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```

## 🖥️ Usage

### CLI Commands

The CLI tool supports the following commands:

1. **List food items**:

   ```
   python cli.py list [--offset OFFSET] [--limit LIMIT] [--query QUERY] [--zipcode ZIPCODE] [--max_distance MAX_DISTANCE]
   ```

2. **Get food item by ID**:

   ```
   python cli.py get <food_id>
   ```

3. **Sign up for notifications**:
   ```
   python cli.py notify <food_id> <email>
   ```

### CLI Examples

1. List all food items:

   ```
   python cli.py list
   ```

2. Search for food items with a query:

   ```
   python cli.py list --query "apple" --limit 10
   ```

3. Get details of a specific food item:

   ```
   python cli.py get 12345
   ```

4. Sign up for notifications:

   ```
   python cli.py notify 12345 user@example.com
   ```

5. Search for food items near a specific location:
   ```
   python cli.py list --zipcode 90210 --max_distance 20
   ```

## 📘 API Documentation

### Endpoints

The API provides the following endpoints:

1. **List Food Items**

   - `GET /api`
   - Query Parameters:
     - `offset` (int): The offset for pagination (default: 0)
     - `limit` (int): The number of items to retrieve (default: 24)
     - `q` (string): Search query
     - `zipcode` (string): Zipcode for location-based search
     - `max_distance` (int): Maximum distance in miles (default: 40)

2. **Get Food Item by ID**

   - `GET /api/<food_id>`
   - Path Parameters:
     - `food_id` (string): The ID of the food item

3. **Sign Up for Notifications**
   - `POST /notify/<food_id>`
   - Path Parameters:
     - `food_id` (string): The ID of the food item
   - Form Data:
     - `email` (string): Email address for notification

### API Examples

1. List all food items:

   ```
   GET /api
   ```

2. Search for food items with a query:

   ```
   GET /api?q=apple&limit=10
   ```

3. Get details of a specific food item:

   ```
   GET /api/12345
   ```

4. Sign up for notifications:

   ```
   POST /notify/12345
   Content-Type: application/x-www-form-urlencoded

   email=user@example.com
   ```

5. Search for food items near a specific location:
   ```
   GET /api?zipcode=90210&max_distance=20
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

[Specify your license here]

---

Developed with ❤️ by [Your Name/Organization]
