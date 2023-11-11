import json
import os
import time
import sys
import re


def handleWindows(extra_seconds):
    local_settings = r"{}\Balsamiq\Balsamiq Wireframes\LocalSettings.json".format(
        os.getenv("APPDATA")
    )

    with open(local_settings) as reader:
        json_data = json.load(reader)
    json_data["DefaultSelectionColorRGBA"] = int(time.time()) + extra_seconds
    json_data["DisableCheckForUpdates"] = True
    json_data["AutomaticUpdate"] = False

    with open(local_settings, "w") as outfile:
        json.dump(json_data, outfile)


years = int(300) # cuántos años quieres el balsamiq gratis

if sys.platform.startswith("win"):
    handleWindows(years * 365 * 24 * 60 * 60)
else:
    print("Tu S.O. no se soporta")
    exit(0)

print("****************************************************************")
print(f"* Tienes {years * 365} días de prueba")
print("****************************************************************")
