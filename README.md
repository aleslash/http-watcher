# http-watcher
Http rest api endpoint monitoring written in python

The idea is to use lambda functions to create an easy way of calling API rest endpoints.

The first goal is to call GET APIs.

With that send these informations to a time-series database. The idea is to start collection some metric data to use later.

Most probable metric structure:

```
http_endpoint_monitoring_total
```
With probable labels
```
expected_status_code="2xx|3xx|4xx|5xx"
received_status_code="2xx|3xx|4xx|5xx"
method="GET|POST|PATCH"
uri="http://xxx"
test_status="success|failure"
```
