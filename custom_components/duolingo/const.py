"""Constants for integration_blueprint."""
# Base component constants
NAME = "Duolinguist"
DOMAIN = "duolingo"
VERSION = "0.1.1"

ISSUE_URL = "https://github.com/wilwac/duolinguist/issues"

# Platforms
BINARY_SENSOR = "binary_sensor"
PLATFORMS = [BINARY_SENSOR]

# Configuration and options
CONF_USERNAME = "username"
CONF_JWT = "jwt"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
