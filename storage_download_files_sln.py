#!/usr/bin/env python

import sys

# [START storage_download_file]
from google.cloud import storage


def download_blobs(bucket_name: str, source_blob_names: list, destination_file_names: list) -> None:
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_names = ["storage-object-name-1", ..., "storage-object-name-n"]
    # destination_file_names = ["local/path/to/file-1", ..., "local/path/to/file-n"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Your code is here
    for fn, obj in zip(destination_file_names, source_blob_names):
        blob = bucket.blob(obj)
        blob.download_to_filename(fn)

        print("Blob {} downloaded to {}.".format(obj, fn))


# [END storage_download_file]

if __name__ == "__main__":
    from storage_list_files import return_blobs
    # 1. List all files in the bucket "comp4312_studentID" on gcp and assign to source_blob_names
    bucket_name = "comp4312_1000"
    source_blob_names = []
    # Your code is here
    source_blob_names = return_blobs(bucket_name)

    # An example of returned values in source_blob_names
    # source_blob_names = ['dandelion1.jpg', 'dandelion2.jpg', 'dandelion3.jpg',
    #                      'grass1.jpeg', 'grass2.jpeg', 'grass3.jpeg']

    # 2. Create paths to save all files in source_blob_names and store in destination_file_names
    import os
    download_path = "images/download/"
    destination_file_names = []
    # Your code is here
    destination_file_names = [os.path.join(download_path, path) for path in source_blob_names]

    # An example of returned values in destination_file_names
    # destination_file_names = ['images/download/dandelion1.jpg', 'images/download/dandelion2.jpg',
    #                           'images/download/dandelion3.jpg', 'images/download/grass1.jpeg',
    #                           'images/download/grass2.jpeg', 'images/download/grass3.jpeg']

    # 3. Download files on the bucket_name bucket with names listed in source_blob_names
    #    and save to paths in destination_file_names
    download_blobs(bucket_name=bucket_name,
                   source_blob_names=source_blob_names,
                   destination_file_names=destination_file_names)

    # 4. Delete the bucket "comp4312_studentID" on gcp
    from storage_delete_bucket import delete_bucket
    # Your code is here
    delete_bucket(bucket_name=bucket_name, force=True)


