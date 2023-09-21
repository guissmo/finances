{ head -n 1 accumulated.csv; tail -n +2 accumulated.csv | sort | uniq; } > accumulated2.csv
mv accumulated2.csv accumulated.csv
{ head -n 1 cats.csv; tail -n +2 cats.csv | sort | uniq; } > cats2.csv
mv cats2.csv cats.csv