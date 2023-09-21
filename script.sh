cat $1 | (tail -n +1 $1 | sort)  | head -n -1 >> accumulated.csv
cat new_cats.csv | (tail -n +1 $1 | sort) >> cats.csv
