Logs
============

Filter
-----------------

Filter interface.
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: src.logs.filter.filter_interface.IFilter.filter

AccessResource
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.access_resource.AccessResource.filter

AccessResourceBitstream
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.access_resource_bitstream.AccessResourceBitstream.filter

SearchResource
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.search_resource.SearchResource.filter

WebResource
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.web_resource.WebResource.filter

WithIPv6Address
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.with_ipv6address.WithIPv6Address.filter

WithoutIpAddress
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete.

.. autofunction:: src.logs.filter.without_ipaddress.WithoutIpAddress.filter

Forwarder
-----------------

Forwarder ìnterface
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: src.logs.forwarder.forwarder_interface.IForwarder.forward

InfluxDbForwarder
~~~~~~~~~~~~~~~~~~~~~~~

TODO: complete

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder.forward

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder.close

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_log_tags

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_log_fields

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._get_influxdb_client_write

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._get_influxdb_credentials

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_timestamp

Transformer
-----------
