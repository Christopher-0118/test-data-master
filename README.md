## Prerequisites ##

1. install boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation
1. install pascal voc: https://pypi.org/project/pascal-voc-writer/0.1.4/
1. For every *.py file do ```chmod +xX <filename>.py```

## Running the scritps ##
1. Copy images to /img folder
1. Run uploader.py
1. Run generate_list.py
1. Upload the item_list.yml and categories.yml to ScaLabel
1. Download BDD json from ScaLable under the name ```bdd.json```
1. Run the convert_bdd_to_voc.py
1. Upload the xml files to bucket using uploader.py