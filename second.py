# InfluxDB imports
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--temp", type=float)
parser.add_argument("--mask", type=bool)
args = parser.parse_args()


# InfluxDB Init
token = "P7SENJDBCC_VSxiaHTP6phlnljd4ubocxnN4KR7s2uVjmjW_vJVLNXWlQFQpCk9onbFCYEW8dG7-MWFYhTUg3Q=="
org = "awjung2000@comcast.net"
bucket = "IoTProject"

client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com/", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)


average_temp = args.temp
has_mask = args.mask
print(average_temp)
print(has_mask)
point = Point("mem").tag("host", "host1").field("temperature",average_temp,"mask",has_mask).time(datetime.utcnow(), WritePrecision.NS)
write_api.write(bucket, org, point)