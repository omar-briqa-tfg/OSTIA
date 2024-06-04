Metadata
============
Filter
-----------------

Filter interface.
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.filter.filter_interface.IFilter.filter

RecordDeleted
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.filter.record_deleted.RecordDeleted.filter

Forwarder
-----------------

FileSystemForwarder
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.forwarder.filesystem_forwarder.FileSystemForwarder.forward

.. autofunction:: src.metadata.forwarder.filesystem_forwarder.FileSystemForwarder._get_subfolder

MongoDbForwarder
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.forwarder.mongodb_forwarder.MongoDbForwarder.forward

.. autofunction:: src.metadata.forwarder.mongodb_forwarder.MongoDbForwarder.close

.. autofunction:: src.metadata.forwarder.mongodb_forwarder.MongoDbForwarder._preprocess_metadata

.. autofunction:: src.metadata.forwarder.mongodb_forwarder.MongoDbForwarder._get_mongodb_credentials

.. autofunction:: src.metadata.forwarder.mongodb_forwarder.MongoDbForwarder._get_mongodb_collection

OAI-PMH
-----------------

OAIClient
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.oaipmh.oaiclient.OAIClient.get_records

Parser
-----------------

Parser Interface
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.parser.parser_interface.IParser.parse

DimParser
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.metadata.parser.dim_parser.DimParser.parse
