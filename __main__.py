"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('vcu-bucket-072625')

next_bucket = s3.Bucket('bucket-umd-2507')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
