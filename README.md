# Running Mythical Mysfits Locally

https://github.com/aws-samples/amazon-ecs-mythicalmysfits-workshop

Mythical Myfits is constructed of 3 application tiers. In this repo, all 3 tiers
are configured to run locally in containers.

Static Site <-> Python Api(s) <-> DynamoDB

- When ran locally the static site is fronted by an NGINX reverse proxy. In AWS
  this will be a S3 Static Site.
- The Python API(s) are deployed as a flask container deployed locally. This
  same flask container can be reused in ECS or EKS.
- The DynamoDB is deployed locally following this
  [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html).
  In AWS a managed DynamoDB will be used.

## Deploying the Stack

The `docker-compose.yml` needs to be adjusted for each environment, the Nginx
container is a reverse proxy for files living on the local file system.
Therefore the file path of the `frontend/static` files will need to be updated
to the local directory where this git repo has been cloned.

Deploy the Stack:

```
$ docker-compose up -d --build
```

### Loading the Dynamodb Table

There is a prerequisite that the Dynamodb table is loaded with
some mysfits. Within the `dynamo` directory there is a `create-dynamo.py` and
`load-dynamo.py` script. These scripts will create an empty table, and then
populate the table with mysfits. Note, the `boto3` python package will need to
be installed before running the scripts `pip install boto3`. 

If you a leverage a Local DynamoDB Instance, the variable `MYSFIT_ENV=LOCAL`
will need to be exported before using the scripts. If you do not export this, a
DynamoDB table will be created in AWS, and sample data will be loaded into the
cloud.

### Browse to the Frontpage

The Front Page of Mythical Misfits will be available on `http://localhost:8080`

## Env Variables

There are a few environment variables required when running the API
microservice. They are already defined in the `docker-compose.yml` file. However
when running the API in AWS, they may need to be passed into the container.

- `DDB_TABLE_NAME` - *Required* - The name of the DynamoDB table that has been
  pre-create and loaded with data. If you leverage the `create-dynamo.py` and
  `load-dynamo.py` scripts, the table name wil be mysfits. `DDB_TABLE_NAME=mysfits`.

- `MYSFIT_ENV` - This is not required when running in AWS. However when running
  locally `MYSFIT_ENV=LOCAL` should be exported.

- `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY` - If the api is deployed onto
  AWS, then EKS IRSA or an ECS Task Role will automatically set these variables.
  
  If the container is running locally then these variables will need to be set.
  A local DynamoDB container does not need real AWS credentials, so noddy values
  like those set in the `docker-compose.yml` file will do. If the API is
  communicating with a DynamoDB Table hosted in the cloud, then an Access Key
  and Secret Key with the relevant permissions is required.

## API Image

The Python API Docker Image is hosted on Docker Hub too:

https://hub.docker.com/r/ollypom/mysfits