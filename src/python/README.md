# python README

These scripts process JSON that was dumped from the SQL scripts at [sql](../sql/README.md).

The JSON is under the [data](../../data/) folder.

Charts are output to [charts](../../charts/) folder.

## Dependencies

- matplotlib 3.5.2
- numpy 1.23.1
- pandas 1.4.3

`python3 -m pip install matplotlib==3.5.2 numpy==1.23.1 pandas==1.4.3 tabulate-0.9.0`

## Execution

`./go.sh`

Check the charts:
- check they WERE updated (the file timestamps are recent)
- that they look OK
- they have data for the previous month (NOT usually this month, since that would be a partial month).

tip: if you use git to push to a branch, then in `github` you can see a diff of the charts before/after.
