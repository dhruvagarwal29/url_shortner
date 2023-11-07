
# URL Shortener

Welcome to the URL Shortener project! This simple Python-based web application allows you to shorten long URLs into concise and easy-to-share links. The application is built using Flask and MySQL and is deployed on [PythonAnywhere](http://dhruvresume.pythonanywhere.com/).

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Deployment](#deployment)

## Overview

URL Shortener is a web application that takes a long URL as input and generates a short, unique identifier for it. This allows you to share URLs more conveniently, especially when dealing with character limitations or simply to make links cleaner and more user-friendly.

## Features

- Shorten long URLs into concise, easy-to-share links.
- View the original URL by visiting the shortened URL.
- Utilizes Flask for the web framework and MySQL for data storage.
- Deployed on PythonAnywhere for easy access.

## Getting Started

To run this URL Shortener project locally, you will need Python and the following packages:

- Flask
- Flask-MySQLdb
- MySQL (or another database of your choice)

Make sure you have these packages installed, and then you can start the application by running the `main.py` script.

```bash
python main.py
```

## Usage

1. Access the URL Shortener web application by visiting the local URL: `http://localhost:5000/`.

2. Enter a long URL that you want to shorten in the provided input field.

3. Click the "Shorten" button to generate a shortened URL.

4. The application will display the shortened URL, which you can now use to access the original URL.

## Deployment

The URL Shortener is deployed on [PythonAnywhere](http://dhruvresume.pythonanywhere.com/). You can access the live version of the application there.


Happy URL shortening!
