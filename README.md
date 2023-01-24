# JobExtractor

## Introduction
This is a multiprocessed program to grab job from internet. Web-scrapping is performed using selenium. The obtained result will store into a csv file.

## Compile
To start the program, simply run the following commend.
```commandline
python FindElement.py [target keyword] [csv_path]
```

## Error handling
An error message will be stored at `./log/JobExtractor_DATE.log`

## Requirements
### Chromedriver
It should be the same version as the google chrome you are using.
Please find the download link [here](https://chromedriver.chromium.org/downloads)