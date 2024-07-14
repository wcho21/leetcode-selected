"""
LISTS.md documentation generator
"""

import json

# user-level config

DOC_HEADING = "Lists"
DOC_HEADING_DESC = "Lists of solved problems.\nA problem may appear in more than one list."

PROBLEMS_JSON = "./problems.json"
LISTS = [
    {
        "name": "Selected Problems",
    },
    {
        "name": "Top Interview Questions",
    },
    {
        "name": "Tricky Problems",
    },
    {
        "name": "Contest Problems",
        "extra_columns": [
            {
                "json_field_name": "contest",
                "column_name": "Contest",
                "align": "left",
            },
        ],
    },
]

README_PATH = lambda problem_num: f"./problems/{problem_num}/README.md"

MARKDOWN_DIFFICULTY_BADGE_COLORS = {
    "Easy": "green",
    "Medium": "yellow",
    "Hard": "red",
}
MARKDOWN_BADGE_URL = "https://img.shields.io/badge/"

# internal config

MARKDOWN_ALIGNS = {
    "left": ":-",
    "center": ":-:",
    "right": "-:",
}
MARKDOWN_LINK_PREFIX = "p"

# markdown generating logic

def generate_markdown(json_file):
    problems = read_problems_json_file(json_file)

    formatted_progress_badge = format_progress_badge(problems)
    formatted_problems = format_problems(problems)

    formatted = "\n\n".join([
        f"# {DOC_HEADING}",
        formatted_progress_badge,
        DOC_HEADING_DESC,
        formatted_problems
    ])

    return formatted

def format_problems(problems):
    formatted_texts = []

    for list_config in LISTS:
        header = f"## {list_config["name"]}" + "\n\n"
        filtered_problems = filter_problems_by_config(problems, list_config)
        problem_list = format_list(filtered_problems, list_config)

        formatted = header + problem_list
        formatted_texts.append(formatted)

    formatted_links = format_links(problems)

    return "\n\n".join(formatted_texts + [formatted_links])

def format_progress_badge(problems):
    url = MARKDOWN_BADGE_URL
    num_problems = len(problems)

    return f"![Progress Badge]({url}Progress-{num_problems}%20Solved-blue)"

def format_links(problems):
    rows = []
    for problem in problems:
        problem_num = problem["number"]
        link_path = README_PATH(problem_num)
        rows.append(format_markdown_link(f"{problem_num}", link_path))

    formatted_rows = "\n".join(rows)
    return formatted_rows

def filter_problems_by_config(problems, list_config):
    tag_name = list_config["name"]
    has_tag_name = lambda problem: tag_name in problem["tags"]
    filtered = list(filter(has_tag_name, problems))

    return filtered

def format_list(problems, list_config):
    extra_columns_config = list_config.get("extra_columns", {})

    # get columns
    column_names = format_column_names(problems, extra_columns_config)
    column_aligns = format_column_aligns(problems, extra_columns_config)
    problem_columns = format_problem_columns(problems, extra_columns_config)

    columns = [column_names, column_aligns] + problem_columns

    # format rows as markdown
    progress_badge = format_progress_badge(problems)
    formatted_rows = list(map(format_markdown_table_row, columns))
    formatted_text = progress_badge + "\n\n" + "\n".join(formatted_rows)

    return formatted_text

def format_column_names(problems, extra_columns_config):
    mandatory_column_names = ["No.", "Note", "Difficulty"]
    extra_column_names = list(map(lambda item: item["column_name"], extra_columns_config))

    column_names = mandatory_column_names + extra_column_names
    return column_names

def format_column_aligns(problems, extra_columns_config):
    mandatory_column_aligns = ["-:", ":-", ":-:"]
    extra_column_aligns = list(map(lambda item: MARKDOWN_ALIGNS[item["align"]], extra_columns_config))

    column_aligns = mandatory_column_aligns + extra_column_aligns
    return column_aligns

def format_problem_columns(problems, extra_columns_config):
    formatted_columns = []

    for problem in problems:
        mandatory_columns = [
            str(problem["number"]),
            format_markdown_linked(problem["name"], problem["number"]),
            format_markdown_difficulty(problem["difficulty"]),
        ]

        extra_columns = format_problem_extra_columns(problem, extra_columns_config)

        columns = mandatory_columns + extra_columns

        formatted_columns.append(columns)

    return formatted_columns

def format_problem_extra_columns(problem, extra_columns_config):
    columns = []

    for config in extra_columns_config:
        json_field = config["json_field_name"]
        column = problem[json_field]
        columns.append(column)

    return columns

def format_markdown_table_row(table_columns):
    return "| " + " | ".join(table_columns) + " |"

def format_markdown_linked(to_link, link_name):
    return f"[{to_link}][{MARKDOWN_LINK_PREFIX}{link_name}]"

def format_markdown_link(link_name, link_path):
    return f"[{MARKDOWN_LINK_PREFIX}{link_name}]: {link_path}"

def format_markdown_difficulty(difficulty):
    url = MARKDOWN_BADGE_URL
    color = MARKDOWN_DIFFICULTY_BADGE_COLORS[difficulty]

    return f"![{difficulty}]({url}{difficulty}-{color})"

def read_problems_json_file(json_file):
    with open(json_file, "r") as f:
        problems = json.load(f)["problems"]
        return problems

# main: print to stdout

print(generate_markdown(PROBLEMS_JSON))
