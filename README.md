# 🍽️ Food Information CLI Tool

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This project is a Command Line Interface (CLI) tool that provides information about various food items. It allows users to list, search, and retrieve details about different foods, as well as sign up for notifications about specific items.

## 🚀 Features

- 📊 List food items with pagination
- 🔍 Search functionality for food items
- 📋 Detailed view of individual food items
- 📨 Email notification sign-up for specific food items
- 📍 Location-based search using zipcode and distance

## 💻 Technology Stack

- **Language**: Python 3.x
- **Libraries**: argparse, tabulate, json
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

### Commands

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

### Examples

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
