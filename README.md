<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# MOVIE-SCRAPER

<em>Discover, Explore, and Relive Movies Effortlessly</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/NixsDK/Movie-Scraper?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/NixsDK/Movie-Scraper?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/NixsDK/Movie-Scraper?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## 📄 Table of Contents

- [Overview](#-overview)
- [Getting Started](#-getting-started)
    - [Prerequisites](#-prerequisites)
    - [Installation](#-installation)
    - [Usage](#-usage)
    - [Testing](#-testing)
- [Features](#-features)

---

## ✨ Overview

Movie-Scraper is an open-source tool crafted to simplify the process of collecting, managing, and querying movie data. It integrates web scraping, database management, and search functionalities into a cohesive package for developers working on movie catalog applications.

**Why Movie-Scraper?**

This project empowers developers to automate movie data collection, organize information efficiently, and build feature-rich movie exploration tools. The core features include:

- **🛠️ Data Scraping:** Automate extraction of movie details from IMDb URLs, ensuring accurate and scalable data collection.
- **📊 Database Management:** Set up and maintain a robust SQLite database for storing and retrieving movie information.
- **🔍 Flexible Search:** Query movies by title, genre, or rating, supporting dynamic filtering and comparison.
- **🎬 Curated Datasets:** Leverage curated lists like the top 250 movies for ranking, recommendations, and content filtering.
- **⚙️ Environment & Logging:** Seamless integration with environment configs and logging for reliable operation.
- **🚀 Easy Setup:** Scripts facilitate quick database initialization and bulk data imports, accelerating project development.

---

## 📌 Features

|      | Component       | Details                                                                                     |
| :--- | :-------------- | :------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | <ul><li>Python-based scraper and data processing scripts</li><li>File-driven workflow using text and SQL files</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Modular Python scripts with functions for scraping and data parsing</li><li>Consistent naming conventions</li></ul> |
| 📄 | **Documentation** | <ul><li>Basic README with project overview</li><li>Comments within scripts, minimal external docs</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Reads from local text files ('top_250_movies.txt', 'movies.txt')</li><li>Uses SQL for data storage and retrieval</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate scripts for scraping, data processing, and database interaction</li><li>Functions encapsulate core logic</li></ul> |
| 🧪 | **Testing**       | <ul><li>No explicit testing framework detected</li><li>Potential for unit tests in Python scripts</li></ul> |
| ⚡️  | **Performance**   | <ul><li>File I/O operations may be bottlenecked by sequential reads/writes</li><li>Limited concurrency or optimization techniques observed</li></ul> |
| 🛡️ | **Security**      | <ul><li>No authentication or security measures implemented</li><li>Local file access only</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Python standard library</li><li>SQL database (likely SQLite or similar)</li><li>Text files as data sources</li></ul> |

---

### 📑 Project Index

<details open>
	<summary><b><code>MOVIE-SCRAPER/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates user interaction for managing a movie database by enabling searches, additions, and data scraping<br>- Coordinates core functionalities such as querying movies by various criteria, adding new entries, and retrieving detailed information from IMDb, integrating environment configurations and logging to support seamless operation within the overall application architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/dump.sql'>dump.sql</a></b></td>
					<td style='padding: 8px;'>- Defines the structure and initial dataset for a movies database, enabling efficient storage, retrieval, and management of movie information within the applications architecture<br>- Facilitates data organization for features like search, filtering, and analysis, supporting the overall goal of delivering a comprehensive movie catalog experience<br>- The script also highlights error handling during database transactions.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- scripts Submodule -->
	<details>
		<summary><b>scripts</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ scripts</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/top_250_movies.txt'>top_250_movies.txt</a></b></td>
					<td style='padding: 8px;'>- Overview of <code>scripts/top_250_movies.txt</code>This file serves as a curated dataset of the top 250 movies, capturing essential metadata such as titles, genres, release years, and ratings<br>- Within the overall architecture, it functions as a foundational data source that supports features like movie ranking, recommendation, and filtering<br>- By providing a standardized and easily accessible list of highly-rated films, this file enables the application to deliver curated content and insights aligned with user preferences and system objectives.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/search_movies.py'>search_movies.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates movie data retrieval by enabling searches across a local database and a static top 250 movies list<br>- Supports filtering by title, genre, or minimum rating, integrating user input for dynamic querying<br>- Serves as a core component for a movie exploration application, providing flexible data access and comparison between stored and external movie datasets.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/movies.txt'>movies.txt</a></b></td>
					<td style='padding: 8px;'>- Provides a curated list of movies with their genres, release years, and ratings, serving as a foundational dataset for filtering, sorting, or analyzing film-related features within the broader application architecture<br>- It supports functionalities like content recommendation, user rating aggregation, and genre-based categorization, enhancing the systems ability to deliver tailored movie experiences.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/setup_database.py'>setup_database.py</a></b></td>
					<td style='padding: 8px;'>- Establishes and manages the SQLite database infrastructure for the project, ensuring the movies and migrations tables are created and maintained<br>- Facilitates tracking of database schema changes through migration records, supporting reliable setup and version control within the overall application architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/scrape_movies.py'>scrape_movies.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates automated extraction of movie details from IMDb URLs and stores the data into a local SQLite database<br>- Supports bulk scraping of predefined movie links, ensuring structured data collection of titles, genres, release years, and ratings<br>- Integrates web scraping with database management to enable scalable, organized movie data curation within the overall project architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/NixsDK/Movie-Scraper/blob/master/scripts/add_movie.py'>add_movie.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates the addition of movie records into the database, supporting both individual entries and bulk imports from a file<br>- Integrates seamlessly within the project’s architecture by populating the movies database, enabling efficient data management and setup for features like search, filtering, and recommendations in the overall movie catalog system.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 📋 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Conda

### ⚙️ Installation

Build Movie-Scraper from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/NixsDK/Movie-Scraper
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Movie-Scraper
    ```

3. **Install the dependencies:**

**Using [conda](https://docs.conda.io/):**

```sh
❯ conda env create -f conda.yml
```

### 💻 Usage

Run the project with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
python {entrypoint}
```

### 🧪 Testing

Movie-scraper uses the {__test_framework__} test framework. Run the test suite with:

**Using [conda](https://docs.conda.io/):**

```sh
conda activate {venv}
pytest
```

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
