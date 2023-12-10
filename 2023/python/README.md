# [Advent of Code - 2023](https://adventofcode.com/2023/)

## Intro

> Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
> You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
> Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

## Progress


                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                ⭐️        ' ''...                       10
              .     ~       ### ''.                  
            .      ⭐️   ~ ~ ~ ##### '.                   9 ⭐️⭐️
                      ~ ⭐️ ~ ~ ~ ### :                   8 ⭐️⭐️
             . ~     ~ ~ ~   ##### .'                
              '.. ~ ~ ⭐️ ~ ##### ..'.'''''''''...        7 ⭐️⭐️
                 '''.........'''' ~ .'⭐️. ~  ..  ''.     6 ⭐️⭐️
                            .' ~    '...' ~'  '.~  '.
                            :         ~     '. ⭐️'.~ :   5 ⭐️⭐️
                     ...'''''.         .''.~  '..' .'
                  .''         '..  ~..'⭐️   '. ~ ..'     4 ⭐️⭐️
                .'               '''../......'''     
                :             /\    -/  :            
                '.            -   - /  .'            
                  '..    -     -   ⭐️..'                 3 ⭐️⭐️
        ----@        '''..⭐️......'''                    2 ⭐️⭐️
      ⭐️ ! /^\                                           1 ⭐️⭐️
    



## Running
_These were developed using python 3.12_

Generat a days folder by running
```bash
# This will create a folder based on the day the commadn was run
source day_setup.sh

# This will create a folder based on the day passed in
source day_setup.sh 9
```

They can be run from any location by running:
```
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

To auto generate readme for the day, run `python create_day_readme.py Day01/Day\ 1\ -\ Advent\ of\ Code\ 2023.html`
