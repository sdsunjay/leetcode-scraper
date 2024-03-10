import sys

from bs4 import BeautifulSoup

from ProblemEntry import ProblemEntry
from Database import Database
from Constants import Constants

def extract_table_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the <table> tag
    start = content.find('<table')
    end = content.find('</table>', start)

    if start != -1 and end != -1:
        table_content = content[start:end + 8]  # 8 is the length of '</table>'

        # Remove the <thead> from the table content
        thead_start = table_content.find('<thead')
        thead_end = table_content.find('</thead>', thead_start)

        if thead_start != -1 and thead_end != -1:
            # Remove the thead section from the table content
            table_content = table_content[:thead_start] + table_content[thead_end + 8:]

        return True, table_content
    else:
        return False, "Table tag not found."

def extract_frequency(row):
    # Find the td element with label containing "Frequency"
    freq_td = row.find('td', {'label': lambda L: L and 'Frequency' in L})
    if freq_td:
        # Extract the width percentage from the style attribute of the progress-bar div
        progress_bar = freq_td.find('div', class_='progress-bar')
        if progress_bar and 'style' in progress_bar.attrs:
            style = progress_bar['style']
            # Assuming the style attribute contains width: xx%; extract the numerical value
            start = style.find('width: ') + len('width: ')
            end = style.find('%;', start)
            percentage = float(style[start:end])
            # Convert percentage to decimal for frequency
            return percentage / 100
    return 0

def extract_id(row):
    problem_id = row.find("td", {"label": "#"})
    return problem_id["value"]

def extract_title_and_url(row):
    # Use find to get the first td element with label 'Title'
    title_td = row.find('td', {'label': 'Title'})
    # Now, find the first <a> tag within title_td to access its contents and href
    title_a = title_td.find('a')
    title = title_a.text
    url_link = title_a['href']
    return title, url_link

def extract_tags(row):
    tags_td = row.find("td", {"label": "Tags"})
    tags = [tag.text for tag in tags_td.find_all("a")]
    return tags

def extract_difficult(row):
    difficulty_span = row.find("span", class_="label")
    difficulty = difficulty_span.text.strip() if difficulty_span else ""
    return difficulty

def extract_acceptance(row):
    acceptance_td = row.find("td", {"label": "Acceptance"})
    acceptance = acceptance_td["value"]
    return acceptance

def parse(soup):
    """
    Extract table data from the provided BeautifulSoup object.

    Parameters:
    - soup (BeautifulSoup): The parsed HTML content using BeautifulSoup.

    Returns:
    - list: A list of lists containing the extracted table data.
    """
    # Initialize a counter to store tag frequencies
    problems = []
    # Iterate through each row in the table
    for row in soup.find_all('tr'):
        if not row.find('td', {'label': 'Title'}):
            print(row)
            continue
        frequency = extract_frequency(row)
        tags = extract_tags(row)
        difficulty = extract_difficult(row)
        acceptance = extract_acceptance(row)
        title, url_link = extract_title_and_url(row)
        problem_id = extract_id(row)

        problems.append(ProblemEntry(problem_id, title, url_link, tags, acceptance, difficulty, frequency))
    return  problems

# This function would be used after you've parsed the problems into a list of ProblemEntry objects
def print_problems(problems):
    # Print the header row
    print(f"{'#':<3} {'Title':<30} {'Tags':<50} {'Acceptance':<12} {'Difficulty'} {'Frequency'}")

    # Print each problem row
    for problem in problems:
        tags = ', '.join(problem.tags)  # Join all tags into a single string
        print(f"{problem.problem_id:<4} {problem.title:<30} {tags:<50} {problem.acceptance:<12} {problem.difficulty} {problem.frequency}")

def main():
    # Check if the argument is provided
    if len(sys.argv) < 2:
        print("Usage: python parse.py <Company Name>")
        return 1

    # Read the company_name argument
    company_name = sys.argv[1]
    company_name = company_name.lower()
    if company_name not in Constants.valid_companies:
        print(f"{company_name} is not a valid company")
        return 1

    flag, raw_html = extract_table_from_html(f"{company_name}/table.html")

    # Parse the HTML
    soup = BeautifulSoup(raw_html, 'html.parser')
    problems = parse(soup)

    database = Database(company_name)
    database.init_db()
    database.insert_problems(problems)

    # Suppose 'problems' is a list of ProblemEntry objects, call the function to print them
    # print_problems(problems)

if __name__ == '__main__':
    main()
