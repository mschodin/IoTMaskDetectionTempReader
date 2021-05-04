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
token = "6ZIma7oJs7RJRs2yX_iKrSLG-fbeXprCVYA1Lxw-nAf4YhN6TF1ldvCCNUz5cMl67fdfkObltP1tg6LYoGYxyQ=="
org = "awjung2000@comcast.net"
bucket = "IoT Presentation"

client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com/", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)


average_temp = args.temp
has_mask = args.mask
print(average_temp)
print(has_mask)

mask = 1 if has_mask else 0
data = "mem,host=host1 hasmask={0},temperature={1}".format(mask, average_temp)
write_api.write(bucket, org, data)
