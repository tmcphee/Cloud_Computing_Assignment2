#!/usr/bin/env python

import sys

# [START storage_upload_file]
from google.cloud import storage


def upload_blobs(bucket_name: str, source_file_names: list, destination_blob_names: list) -> None:
    """Uploads a list of files to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_names = ["local/path/to/file-1", ..., "local/path/to/file-n"]
    # destination_blob_name = ["storage-object-name-1", ..., "storage-object-name-n"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Your code is here
    for fn, obj in zip(source_file_names, destination_blob_names):
        blob = bucket.blob(obj)
        blob.upload_from_filename(fn)
        print("File {} uploaded to {}.".format(fn, obj))


# [END storage_upload_file]

if __name__ == "__main__":
    from storage_create_bucket import create_bucket
    # 1. Create a bucket named "comp4312_studentid" on gcp
    bucket_name = "comp4312_1000"
    # Your code is here
    create_bucket(bucket_name=bucket_name)

    # 2. List all files in the 'images/upload/' folder and assign to source_file_names
    import glob
    upload_path = "images/upload/"
    source_file_names = []
    # Your code is here
    source_file_names = glob.glob(upload_path + "*", recursive=True)

    # An example of returned values in source_file_names
    # source_file_names = ['images/upload/dandelion1.jpg', 'images/upload/dandelion2.jpg',
    #                      'images/upload/dandelion3.jpg', 'images/upload/grass1.jpeg',
    #                      'images/upload/grass2.jpeg', 'images/upload/grass3.jpeg']

    # 3. Extract basename of each path in source_file_names to form destination_blob_names
    import os
    destination_blob_names = []
    # Your code is here
    destination_blob_names = [os.path.basename(path) for path in source_file_names]

    # An example of returned values in destination_blob_names
    # destination_blob_names = ['dandelion1.jpg', 'dandelion2.jpg', 'dandelion3.jpg',
    #                           'grass1.jpeg', 'grass2.jpeg', 'grass3.jpeg']

    # 4. Upload files in source_file_names on the bucket_name bucket with names listed in destination_blob_names
    upload_blobs(
        bucket_name=bucket_name,
        source_file_names=source_file_names,
        destination_blob_names=destination_blob_names,
    )
