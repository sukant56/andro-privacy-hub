"""
GPS spoofing is done with Magisk/Xposed modules.
Automation example (if app supports broadcast intents):

import os
def set_fake_location(lat, lon):
    os.system(f"am broadcast -a com.lerist.fakelocation.set --es lat '{lat}' --es lon '{lon}'")
    print(f"Set fake location to {lat},{lon}")

# Usage: set_fake_location("37.7749", "-122.4194") # San Francisco
# Use Tasker or Python (with Termux:API) to rotate location every N seconds.
"""
