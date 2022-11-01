# Athena CLI

## Retrieving data from Amazon Athena via the command line and Drawing Charts via Python Pandas

This code is shared as a 'working example' and would need to be altered to fit your own particular needs.

OS: Built on Mac OS.

## Components

`[1] SQL Script runner -> JSON -> [2] Python Pandas -> Charts in PNG file format`

| Component | Location | Description |
|---|---|---|
| [1] SQL Script runner [bash] | [src/sql](src/sql) | Bash scripts to execute any SQL files in a given folder, against Amazon Athena. The resulting data is transposed to a compact JSON format and saved to a data folder. The JSON file is named to match the original SQL file. [Read more.](src/sql/README.md)  |
| [2] Python scripts | [src/python](src/python) | Python script that reads a JSON data file and processes it via Pandas. A chart is output in PNG file format. Markdown (MD) format can also be output. [Read more.](src/python/README.md) |

## Configuration

The following environment variables need to be set up, to match your Amazon AWS environment:

```
AWS_REGION="eu-north-1"
AWS_WORKGROUP="my-workgroup"
AWS_S3_OUT_PATH="s3://my-query-results/my-workgroup/my-account"
```

## Dependencies

- AWS environment with [Athena](https://aws.amazon.com/athena) database
- [Python and dependencies](src/python/README.md)
- [SQL dependencies](src/python/README.md)

## Related Tools

| What | URL | Comment |
|---|---|---|
| DBeaver | https://dbeaver.io/ | Newer, better than SQL Workbench |
| SQL Workbench | http://www.sql-workbench.eu/downloads.html | Older application - does not work with the new OAuth based authentication mechanism provided by Athena |
| jq | https://stedolan.github.io/jq/ | Command line tool, like XPath for JSON |
| Pandas | https://pandas.pydata.org/ | Python library for data analysis and simple charts |

## Resources

| What | URL |
|---|---|
| ANSI SQL Tutorial | https://riptutorial.com/sql |
| General SQL Tutorial (might not be ANSI) | https://www.w3schools.com/sql/default.asp |

## author

Sean Ryan
