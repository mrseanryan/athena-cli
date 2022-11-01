# SQL README

These SQL scripts are used to dump aggregated data from Athena into JSON files in this repo, for later processing.

The output of each SQL script is saved to a same-named JSON file, under the [data](../../data/) folder.

The JSON files are later processed with the [the Python scripts](../python/README.md).

## Automatic (scripted) Execution

0. Install AWS CLI tool

Create the appropriate credentials file.

It should look something like this:

```
> cat ~/.aws/credentials
[default]
aws_access_key_id = BLAH123
aws_secret_access_key = BLAH678/BLAH91011

work_group = rnd
```

1. Configure the [go.sh](./go.sh) script for your account, replacing the values for the AWS variables:

- AWS_REGION
- AWS_WORKGROUP
- AWS_S3_OUT_PATH

2. At a Unix terminal, execute `./go.sh`

## Manual Execution

Alternatively, the same SQL scripts can be executed in a tool like DBeaver and then the JSON copy-pasted into the appropriate samed-named JSON file, for the Python chart scripts to pick up.

## Commit the data to git, for re-use

The data is saved as JSON files in this repository.

Check that any numeric fields are still numeric.
(else, you will need to update the consuming Python chart scripts).

Use git to commit the JSON files.

## Update the charts

The Python charting scripts can be executed via [the Python scripts](../python/README.md).

## FAQ

1 - why not use Python library X instead of the AWS CLI?

An advantage of the AWS CLI is that we can decide which Athena REST API call to invoke. This can be important if you are working against a 3rd party Athena database, or an Athena database with restricted access.

2 - UnrecognizedClientException when querying Athena.

```
An error occurred (UnrecognizedClientException) when calling the StartQueryExecution operation: The security token included in the request is invalid.
```

This can be something simple, for example adding a ; at the end of the secret token (I did this!)
OR more seriously if the Athena environment you are accessing does not allow that particular REST call.

## References (Athena Clients)

- AWS CLI - simple, can decide what command to run (important for permissions)
ref = https://sysadmins.co.za/using-the-aws-cli-tools-to-interact-with-amazons-athena-service/

- python boto - setup first via cli

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

- Java

https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html

https://docs.aws.amazon.com/athena/latest/ug/code-samples.html#create-a-client-to-access-athena

- AWS sdk

https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/athena

https://github.com/awsdocs/aws-doc-sdk-examples
