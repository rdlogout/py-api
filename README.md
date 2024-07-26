# 🍽️ Food Information Tool: CLI, API, and Web Interface

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Web Interface](#web-interface)
  - [CLI Commands](#cli-commands)
  - [API Endpoints](#api-endpoints)
- [Examples](#examples)
  - [Web Interface Examples](#web-interface-examples)
  - [CLI Examples](#cli-examples)
  - [API Examples](#api-examples)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This project provides a comprehensive Food Information Tool with three interfaces:

1. A web-based user interface
2. A Command Line Interface (CLI) tool
3. A RESTful API

Users can list, search, and retrieve details about various food items, as well as sign up for notifications about specific items.

## 🚀 Features

- 📊 List food items with pagination
- 🔍 Search functionality for food items
- 📋 Detailed view of individual food items
- 📨 Email notification sign-up for specific food items
- 📍 Location-based search using zipcode and distance
- 🖥️ User-friendly web interface
- 💻 Command-line interface for quick access
- 🔗 RESTful API for programmatic access to food data

## 💻 Technology Stack

- **Language**: Python 3.x
- **Web Framework**: Flask
- **Frontend**: HTML, CSS (and any JavaScript libraries if used)
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

### Web Interface

To start the web application:

```
python3 web.py
```

The web interface will be available at `http://localhost:5000`.

### CLI Commands

The CLI tool supports the following commands:

1. **List food items**:

   ```
   python3 cli.py list [--offset OFFSET] [--limit LIMIT] [--query QUERY] [--zipcode ZIPCODE] [--max_distance MAX_DISTANCE]
   ```

2. **Get food item by ID**:

   ```
   python3 cli.py get <food_id>
   ```

3. **Sign up for notifications**:
   ```
   python3 cli.py notify <food_id> <email>
   ```

### API Endpoints

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

3. **Sign Up for Notifications**
   - `POST /notify/<food_id>`
   - Form Data:
     - `email` (string): Email address for notification

## 📝 Examples

### Web Interface Examples

1. **Browse Food Items**:

   - Navigate to `http://localhost:5000`
   - Use the pagination controls at the bottom of the page to browse through items

2. **Search for Food Items**:

   - Enter a search term in the search box
   - Optionally, enter a zipcode and max distance for location-based search
   - Click the "Search" button

3. **View Food Item Details**:

   - Click on a food item's name or image to view its details

4. **Sign Up for Notifications**:
   - On a food item's detail page, enter your email in the notification form
   - Click "Notify Me" to sign up for notifications about that item

### CLI Examples

1. List all food items:

   ```
   python3 cli.py list
   ```

2. Search for food items with a query:

   ```
   python3 cli.py list --query "apple" --limit 10
   ```

3. Get details of a specific food item:

   ```
   python3 cli.py get 12345
   ```

4. Sign up for notifications:

   ```
   python3 cli.py notify 12345 user@example.com
   ```

5. Search for food items near a specific location:
   ```
   python3 cli.py list --zipcode 90210 --max_distance 20
   ```

### API Examples

1. List all food items:

   ```
   GET http://localhost:5000/api
   ```

2. Search for food items with a query:

   ```
   GET http://localhost:5000/api?q=apple&limit=10
   ```

3. Get details of a specific food item:

   ```
   GET http://localhost:5000/api/12345
   ```

4. Sign up for notifications:

   ```
   POST http://localhost:5000/notify/12345
   Content-Type: application/x-www-form-urlencoded

   email=user@example.com
   ```

5. Search for food items near a specific location:
   ```
   GET http://localhost:5000/api?zipcode=90210&max_distance=20
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
