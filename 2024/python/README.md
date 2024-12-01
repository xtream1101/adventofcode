# [Advent of Code - 2023](https://adventofcode.com/2023/)

## Intro

> The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.
> As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.
> Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!


## Progress


           .--'~ ~ ~|        .-' ⭐️       \  /     '-.   1 ⭐️⭐️
        .--'        |        |                      |   2
                                                        3
                                                        4
                                                        5
                                                        6
                                                        7
                                                        8
                                                        9
                                                       10
                                                       11
                                                       12
                                                       13
                                                       14
                                                       15
                                                       16
                                                       17
                                                       18
                                                       19
                                                       20
                                                       21
                                                       22
                                                       23
                                                       24
                                                       25
    




## Running

_These were developed using python 3.12_

Generate a days folder by running

```bash
# This will create a folder based on the day the commadn was run
source day_setup.sh

# This will create a folder based on the day passed in
source day_setup.sh 9
```

They can be run from any location by running:

```bash
python Day01/1-1.py
```

Using `ruff` to format and lint the code

```bash
# Auto format and lint
ruff format .

# Just lint and get warnings
ruff .
```


## Notes

I am aware that hyphens are not good python file names since it means they cannot be imported. I am using them in AOC because I wanted a way to prevent me from reusing code from other files. This way each day/part stays fully standalone.

I am getting the html with styles as a single file by using the browser extension **Save Page WE**
- Chrome: https://chrome.google.com/webstore/detail/save-page-we/dhhpefjklgkmgeafimnjhojgjamoafof?hl=en-US
- Firefox: https://addons.mozilla.org/en-US/firefox/addon/save-page-we/

To auto generate readme for the day, run `python create_day_readme.py Day01/Day\ 1\ -\ Advent\ of\ Code\ 2024.html`
