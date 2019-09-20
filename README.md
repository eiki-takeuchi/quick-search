# quick-search

quick-search is a command-line tool that allows Google Search. Search results are displayed with a title, link, and content. It provides interactive command, and the user can track with numbers. quick-search uses Google Custom API so that you will be charged in proportion to the number of searches. 

*Twitter Search is available. 

<img src="https://i.gyazo.com/bfc1c55318f75366205913a674fd381a.png" width="600" style="display: block;margin-left: auto;margin-right: auto;">

# Concept

quick-search eliminates options and command-specific usage as much as possible to reduce learning costs. The basic design is “simple” and “easy to see”, and can be used intuitively.

# Environment

Currently, only below environemt is validated. 

|Tool/OS/Service|Version|
|:-----------|:------------|
|python|python3.5 or later|
|OS|CentOS6 or later|
|Google Custom Search API|https://cloud.google.com/?hl=ja|

# Installation

```
# Git clone.
$ git clone git@github.com:eitake0002/quick-search.git

# Install libraries. 
$ pip install -r requirements.txt

# Set up Google API. 
$ export SEARCH_ENGINE_ID=[Search Engine ID]
$ export GOOGLE_API_KEY=[GCP Access Key]

# Execution
$ python quick-search [Search Word]

# Simple execution by setting up alias. 
$ alias q='python ~/quick-search/quick-search.py'
$ q [Search Word]
```

# Usage

```
# Structure
$ ./quick-search [query]

# Example
$ ./quick-search test query
```

# Installation and usage to Twitter search. 

Twitter search require keys. Please refer to below link. 

Twitter REST API Usage
https://syncer.jp/Web/API/Twitter/REST_API/

```
$ export ACCESS_TOKEN=[access_token]
$ export ACCESS_TOKEN_SECRET=[access_token_secret]
$ export CONSUMER_KEY=[consumer_key]
$ export CONSUMER_SECRET=[consumer_secret]

$ python tweet-search.py [query]

# Setting up alias. 
$ alias t="python ~/tweet-search.py"

```

# Interactive Options

Interactive options are provides below. Search result will be show 5 as default. 

|Option|Description|Others|
|:-----------|:------------|:--------------|
|Enter| Next ||
|Search number result|Displaying specified number||
|[Search number result]c|Display result with Chrome Browser. Ex. 1c|Only MacOS|
|[Search number result]b|Display result with Firefox Brower. Ex. 1b|Only MacOS|
|q|Quit||

# Advanced Setting

You can customize search condition, and environment by setting up params.yaml.

|Parameter|Description|Default|
|:-----------|:------------|:------------|
|result_num|Specify search result. |20|
|stop_num|Stop specified times. |5|
|summary_num|Specify number of summary word of search result. |300|
|multi_process|Displaying search result parallelly. |False|
