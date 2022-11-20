import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_snapshot( Description='snapshot from basevolume using python',
      VolumeId='vol-0afe935815cf593d5')