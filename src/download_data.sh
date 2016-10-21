#!/bin/bash

# Documentation:
# https://www.opendataphilly.org/dataset/opa-property-assessments/resource/3084509c-82ad-4718-8ab2-474196eff98b

# This is how you count, if needed
# https://data.phila.gov/resource/tqtk-pmbv.json?$select=owner_1,count(owner_1)&$group=owner_1&owner_1=CITY%20OF%20PHILADELPHIA

data_dir="../data/"
mkdir -p $data_dir

current_date=$(date +"%Y_%m_%d")
while read phila_alias
do
  curl "https://data.phila.gov/resource/tqtk-pmbv.csv?\$limit=50000&\$order=parcel_number&owner_1=${phila_alias}" | tail -n +2 >> ${data_dir}/${current_date}_city_owned.csv
done < ./phila_aliases.txt
