# LeetCode Scraper

The `leetcode-scraper` is a Python project for extracting problem data from LeetCode, storing it in a SQLite database, and performing analytics on the collected data. It is designed to parse HTML page where all problems are listed for a particular company. Then extract relevant problem details, and provide tools for analysis and insights into problems based on various metrics such as difficulty and frequency.

## Project Structure

The project is divided into five main Python files, each with a specific role:

- `Constants.py`: This file contains the constants used throughout the code, such as URLs, database paths, and any other fixed values.
- `Database.py`: Manages database connections, the creation of tables, and the insertion and retrieval of `ProblemEntry` instances from the database.
- `ProblemEntry.py`: Defines the `ProblemEntry` class that represents a LeetCode problem with attributes like title, URL link, tags, acceptance, difficulty, and frequency.
- `parse.py`: Provides functionality to parse a given HTML file using BeautifulSoup and extract problem data into `ProblemEntry` instances.
- `analyze.py`: Contains functions and logic for analyzing the problem data, such as calculating the most frequent tags or selecting random problems for further study.

## Features

- HTML table parsing with BeautifulSoup
- Data manipulation and storage using SQLite
- Object-oriented approach for handling problem entries
- Analysis tools for aggregated data insights

## Usage

To use this project:

1. Ensure you have Python3 installed on your machine.
2. Install the required packages: `beautifulsoup4` and `sqlite3`.
3. Run `parse.py` to parse an HTML file and extract problem data and save to SQLite DB
4. Execute `analyze.py` for extracting the problems and data analysis tasks on those problems.

Please refer to the individual Python files for more detailed usage instructions and documentation of functions.

## Requirements

- Python 3.x
- beautifulsoup4
- sqlite3 (included in the standard Python library)

To install the necessary third-party packages, you can use:

```bash
pip install beautifulsoup4
```

## Contributing

Contributions to the `leetcode-scraper` are welcome. Please ensure you adhere to the following guidelines:

- Follow the existing coding style.
- Write clear, concise commit messages.
- Make sure your code has been thoroughly tested.
- Open a pull request with a detailed description of your changes.

## License

This project is open-sourced under the [MIT License](LICENSE).

---

For more information, questions, or feedback, feel free to [open an issue](https://github.com/sdsunjay/leetcode-scraper/issues).

