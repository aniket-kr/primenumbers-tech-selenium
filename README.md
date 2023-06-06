# PrimeNumbers Technologies
**Assignment - Data Engineer (Python)**: This repository hosts the solution to the assignment posted on Internshala for your Job Role.

### Installation
0. [Optional but recommended] Create a virtual environment
    ```sh
    python -m venv venv
    ./venv/Scripts/activate
    ```
1. Clone the repo
   ```sh
   git clone
    ```
2. Install packages
    ```sh
    pip install -r requirements.txt
    ```
3. Run the script
    ```sh
    python main.py
    ```
4. See the scraping result get saved to:
    ```sh
    output/information.csv
    output/information.jsonl
    ```

### Libraries Used
* [selenium](https://pypi.org/project/selenium/)
* [pandas](https://pypi.org/project/pandas/)

### Approach
1. Used selenium to automate the browser and scrape the data.
2. Used pandas to store the data in csv and jsonl format.

### Alternate Approaches
1. Could have used scrapy to scrape the data but scrapy does not support javascript rendering on its own.
2. Using scrapy + splash would have been a good option, but it would have been an overkill for this assignment.
3. Could have used beautifulsoup, but it does not support javascript rendering on its own.

### Author
Made with ❤️ by **Aniket Kumar** ([LinkedIn](https://www.linkedin.com/in/aniket-kumarr/) | [GitHub](https://www.github.com/aniket-kr))