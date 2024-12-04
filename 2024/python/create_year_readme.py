import os
import pathlib
import sys
import parsel
import jinja2
import html2text
from test.test_ctypes.test_pep3118 import Complete

template_path = pathlib.Path(os.path.dirname(sys.argv[0]), "YEAR_README.md.j2")
output_path = pathlib.Path(os.path.dirname(sys.argv[0]), "README.md")


def fix_formatting(text):
    text = text.replace(
        '<span class="calendar-mark-complete">*</span>',
        '<span class="calendar-mark-complete">⭐️</span>',
    )
    text = text.replace(
        '<span class="calendar-mark-verycomplete">*</span>',
        '<span class="calendar-mark-verycomplete">⭐️</span>',
    )
    return text


h2t = html2text.HTML2Text()
h2t.ignore_links = True
calendar_html = parsel.Selector(text=open(sys.argv[1]).read()).css(".calendar")
calendar_html.css("#calendar-countdown").drop()


# Check if a day is not complete
for el in calendar_html.css("a"):
    if el.css(".calendar-complete"):
        # Remove the 2nd star from showing
        star_el = el.css("span.calendar-mark-verycomplete").drop()

raw_html = calendar_html[0].extract().strip()
raw_html = fix_formatting(raw_html)
progress = h2t.handle(raw_html)


tm = jinja2.Template(open(template_path).read())
readme_template = tm.render(
    progress=progress,
)

with open(output_path, "w") as f:
    f.write(readme_template)
