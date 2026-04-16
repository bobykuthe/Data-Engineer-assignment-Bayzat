from datetime import datetime
import json

def transform(msg):
    try:
        data = json.loads(msg)

        name = data.get("name", "") + " " + data.get("surname", "")

        if "route" in data:
            first = data["route"][0]
            last = data["route"][-1]

            return {
                "id": data["id"],
                "mail": data["mail"],
                "name": name,
                "trip": {
                    "departure": first["from"],
                    "destination": last["to"],
                    "start_date": datetime.strptime(first["started_at"], "%m/%d/%Y %H:%M:%S"),
                    "end_date": datetime.strptime(last["started_at"], "%m/%d/%Y %H:%M:%S")
                }
            }

        if "locations" in data:
            locs = data["locations"]

            return {
                "id": data["id"],
                "mail": data["mail"],
                "name": name,
                "trip": {
                    "departure": locs[0]["location"],
                    "destination": locs[-1]["location"],
                    "start_date": datetime.fromtimestamp(locs[0]["timestamp"]),
                    "end_date": datetime.fromtimestamp(locs[-1]["timestamp"])
                }
            }

    except:
        return None
