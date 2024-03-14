from collections import defaultdict
import sys
import random
import click

from Constants import Constants
from Database import Database
from ProblemEntry import ProblemEntry

def get_problems_by_difficulty(problems, difficulty):
    return [problem for problem in problems if problem.difficulty.lower() == difficulty]

def get_most_frequent_tags(problems):
    tag_counter = defaultdict(int)
    for problem in problems:
        # Update the counter with the tags found in the current cell
        for tag in problem.tags:
            tag_counter[tag] += 1  # Assuming we increment by 1 for each occurrence of the tag
    # Now get the 10 most frequent tags
    most_frequent_tags = sorted(tag_counter, key=tag_counter.get, reverse=True)[:10]
    return most_frequent_tags

def get_problems_with_top_tags(problems, most_frequent_tags):
    # Filter problems by whether they contain any of the most frequent tags
    filtered_problems = [p for p in problems if any(tag in p.tags for tag in most_frequent_tags)]
    return filtered_problems

def select_random_problems(filtered_problems, count=10):
    # Randomly select 'count' problems from the list
    return random.sample(filtered_problems, min(count, len(filtered_problems)))

@click.command()
@click.option('--company-name', type=click.Choice(['facebook', 'amazon', 'google', 'apple', 'jpmorgan', 'uber', 'linkedin', 'microsoft', 'adobe','nvidia'], case_sensitive=False), help='Company name.')
@click.option('--difficulty', type=click.Choice(['easy', 'medium', 'hard', 'all'], case_sensitive=False), default='all', help='Question difficulty level.')
def cli(company_name, difficulty):
    """Process the company name and difficulty level."""
    click.echo(f"Company: {company_name}, Difficulty: {difficulty}")

    database = Database(company_name)
    problems = database.get_problems()
    if difficulty != "all":
        problems = get_problems_by_difficulty(problems, difficulty)
    most_frequent_tags = get_most_frequent_tags(problems)
    filtered_problems = get_problems_with_top_tags(problems, most_frequent_tags)
    selected_problems = select_random_problems(filtered_problems)

    base_url = 'https://leetcode.com'

    # Print the titles and URL links of the selected problems
    for problem in selected_problems:
        print(f"Title: {problem.title}, URL Link: {base_url}{problem.url_link}")

if __name__ == '__main__':
    cli()
