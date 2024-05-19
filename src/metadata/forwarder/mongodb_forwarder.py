from src.metadata.forwarder.forwarder_interface import IForwarder

import os
import json
from pathlib import Path
from typing import Optional
from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDbForwarder(IForwarder):

    mongodb_url: Optional[str] = None
    mongodb_database_name: Optional[str] = None
    mongodb_collection_name: Optional[str] = None

    mongoDbClient: Optional[MongoClient] = None
    mongoDbCollection: Optional[Collection] = None

    @classmethod
    def forward(cls, metadata_path: Path) -> int:

        collection = cls._get_mongodb_collection()
        metadata_list = cls._preprocess_metadata(metadata_path)
        collection.insert_many(metadata_list)

        return 0

    @classmethod
    def close(cls) -> None:
        if cls.mongoDbClient is not None:
            cls.mongoDbClient.close()

    @classmethod
    def _preprocess_metadata(cls, metadata_path: Path) -> list:
        with open(metadata_path, 'r', encoding='utf-8') as file:
            metadata_list = json.load(file)
            for metadata in metadata_list:
                if 'metadata' in metadata:
                    updated_metadata = {}
                    for key, value in metadata['metadata'].items():
                        updated_key = key.replace('.', '-')
                        updated_metadata[updated_key] = value
                    metadata['metadata'] = updated_metadata
        return metadata_list

    @classmethod
    def _get_mongodb_credentials(cls) -> None:
        cls.mongodb_url = os.environ.get('MONGODB_URL')
        cls.mongodb_database_name = os.environ.get('MONGODB_DATABASE')
        cls.mongodb_collection_name = os.environ.get('MONGODB_COLLECTION')

    @classmethod
    def _get_mongodb_collection(cls) -> Collection:
        if cls.mongoDbClient is None:
            cls._get_mongodb_credentials()
            cls.mongoDbClient = MongoClient(cls.mongodb_url)
            cls.mongoDbCollection = cls.mongoDbClient[cls.mongodb_database_name][cls.mongodb_collection_name]

        return cls.mongoDbCollection
