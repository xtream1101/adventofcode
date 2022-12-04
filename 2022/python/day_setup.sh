
# Need to use `source day_setup.sh`, NOT bash or ./ otherwise `cd` will not work

DAY=$(date -d "$D" '+%-d')
DAY2=$(date -d "$D" '+%d')

DAY_FOLDER="Day${DAY2}"

mkdir -p $DAY_FOLDER

# Do not overwrite if a file exists
cp -n script_template.py "${DAY_FOLDER}/${DAY}-1.py"

touch "${DAY_FOLDER}/${DAY}-2.py"
touch "${DAY_FOLDER}/test_input.txt"
# Could use cookies and wget to get my actual input but this is good enough for now
touch "${DAY_FOLDER}/input.txt"

cd "${DAY_FOLDER}"
