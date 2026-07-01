import os
import mimetypes

from azure.storage.blob import (
    BlobServiceClient,
    ContentSettings,
)

from config import *

blob_service = BlobServiceClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING
)

container = blob_service.get_container_client(
    AZURE_CONTAINER_NAME
)


def upload_file(filepath):

    blob_name = os.path.basename(filepath)

    content_type = (
        mimetypes.guess_type(filepath)[0]
        or "application/octet-stream"
    )

    blob = container.get_blob_client(blob_name)

    with open(filepath, "rb") as f:

        blob.upload_blob(
            f,
            overwrite=True,
            content_settings=ContentSettings(
                content_type=content_type
            ),
        )

    return blob.url