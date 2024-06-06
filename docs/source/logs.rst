Logs
============

Filter
-----------------

Filter interface.
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.filter_interface.IFilter.filter

AccessResource
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.access_resource.AccessResource.filter

AccessResourceBitstream
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.access_resource_bitstream.AccessResourceBitstream.filter

SearchResource
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.search_resource.SearchResource.filter

WebResource
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.web_resource.WebResource.filter

WithIPv6Address
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.with_ipv6address.WithIPv6Address.filter

WithoutIpAddress
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.filter.without_ipaddress.WithoutIpAddress.filter

Forwarder
-----------------

Forwarder ìnterface
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: src.logs.forwarder.forwarder_interface.IForwarder.forward

InfluxDbForwarder
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder.forward

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder.close

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_log_tags

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_log_fields

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._get_influxdb_client_write

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._get_influxdb_credentials

.. autofunction:: src.logs.forwarder.influxdb_forwarder.InfluxDbForwarder._set_timestamp

Transformer
-----------

AddDefaultIpAddress
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.transformer.add_default_ipaddress.AddDefaultIpAddress.transform

AddLabel
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.transformer.add_label.AddLabel.transform

AddResourceIdLabel
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.transformer.add_resource_id_label.AddResourceIdLabel.transform

RemoveIPv6Address
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.transformer.remove_ipv6address.RemoveIPv6Address.transform

ToJSON
~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: src.logs.transformer.to_json.ToJSON.transform
