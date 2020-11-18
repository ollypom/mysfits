import boto3

dynamo_url = 'http://localhost:9000'
table_name = 'misfits'

dynamodb = boto3.resource('dynamodb',
    endpoint_url=dynamo_url,
    region_name='eu-west-1')

response = dynamodb.create_table(
    TableName = table_name,
    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    KeySchema = [
        {
            'AttributeName': 'MysfitId',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'MysfitId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GoodEvil',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'LawChaos',
            'AttributeType': 'S'
        },        
    ],
    GlobalSecondaryIndexes = [
        {
            'IndexName': 'LawChaosIndex',
            'KeySchema': [
                {
                    'AttributeName': 'LawChaos',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'MysfitId',
                    'KeyType': 'RANGE'
                },                
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput' :{
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            }
        },
        {
            'IndexName': 'GoodEvilIndex',
            'KeySchema': [
                {
                    'AttributeName': 'GoodEvil',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'MysfitId',
                    'KeyType': 'RANGE'
                },                
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput' :{
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            }
        },        
    ]
)

print(response)