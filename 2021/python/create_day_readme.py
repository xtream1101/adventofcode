import os
import re
import sys
import parsel
import jinja2
import html2text

cb_format_pattern = re.compile(r'(`.+?`)', re.S)


def fix_inline_code_formatting(text):
    """Used to fix formatting of when inline code tags have bold tags `**bold**` inside
    """
    text = cb_format_pattern.sub(lambda m: m.group().replace('**', '`**`'), text)
    # Now clean up the double tick marks making sure not to replace the triple ticks
    text = re.sub(r'([^`])``([^`])', r'\1\2', text)
    return text


tests = [
    (
        'example, `**2**` password',
        'example, **`2`** password'
    ),
    (
        '- `1-3 a: **a**b**c**de` is **valid**: position `1` contains `a` and position `3` does not.',
        '- `1-3 a: `**`a`**`b`**`c`**`de` is **valid**: position `1` contains `a` and position `3` does not.'
    ),
    (
        'so the correct answer is `**514579**`.',
        'so the correct answer is **`514579`**.'
    ),
    (
        '```\nfoo\nbar\n```',
        '```\nfoo\nbar\n```'
    ),
]

for test in tests:
    test_output = fix_inline_code_formatting(test[0])
    try:
        assert test_output == test[1]
    except AssertionError:
        print("Test Failed!!!")
        print(f" Input: {test[0]}")
        print(f"Output: {test_output}")
        print(f"Expected: {test[1]}")
        sys.exit(1)

# First remove un needed style tag
with open(sys.argv[1], 'r') as f:
    prefix_regex = re.compile('<style data-savepage-href="/static/highcontrast.css.*</style>', re.MULTILINE|re.DOTALL)
    cleaned = re.sub(prefix_regex, '', f.read())
with open(sys.argv[1], 'w') as f:
    f.write(cleaned)

# Parse the content
problems = parsel.Selector(text=open(sys.argv[1]).read()).css('article.day-desc')

day_title = problems[0].css('h2::text').extract_first().replace('---', '').strip()

# Remove headers from the problem text. Use the one in the Readme's template
h2t = html2text.HTML2Text()
problem_part1 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[0].extract()).strip())
problem_part2 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[1].extract()).strip())

tm = jinja2.Template(open('Day_README.md.j2').read())
readme_template = tm.render(
    day_title=day_title,
    problem_part1=fix_inline_code_formatting(problem_part1),
    problem_part2=fix_inline_code_formatting(problem_part2),
)

# Save new readme to the days folder
with open(f'{os.path.dirname(sys.argv[1])}/README.md', 'w') as f:
    f.write(readme_template)
