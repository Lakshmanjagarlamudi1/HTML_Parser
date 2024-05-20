# HTML Table Scraper and Data Converter

## Overview

This Python script parses HTML tables containing student and course information, extracts relevant data, and converts it into a structured format using pandas DataFrames. The final data is then saved as a CSV file.

## Features

- **HTML Table Parsing**: The script uses BeautifulSoup to parse HTML tables.
- **Data Extraction**: It extracts student and course information from the HTML tables.
- **Data Conversion**: The extracted data is converted into pandas DataFrames for structured representation.
- **CSV Export**: The structured data is saved as a CSV file for further analysis or processing.

## Dependencies

- **Python 3**
- **BeautifulSoup (bs4)**
- **pandas**
- **re**
- **requests**
- **tabulate**

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/html-table-scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd html-table-scraper
    ```

3. Install required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. This code cannot be used for every HTML file. It is specifically designed for the SNHU student evaluation.
