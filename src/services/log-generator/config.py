import os

DEFAULT_CONFIG = {
    "LOG_RATE": 5, 
    "LOG_TYPES": ["INFO", "WARNING", "ERROR", "DEBUG"],
    "LOG_DISTRIBUTION": {
        "INFO": 70,
        "WARNING": 20,
        "ERROR": 5,
        "DEBUG": 5
    },
    "OUTPUT_FILE": "/logs/generated_logs.log",
    "CONSOLE_OUTPUT": True
}

# Load configuration from environment variables
config = {
    "LOG_RATE": int(os.environ.get("LOG_RATE", DEFAULT_CONFIG["LOG_RATE"])),
    "LOG_TYPES": os.environ.get("LOG_TYPES", ",".join(DEFAULT_CONFIG["LOG_TYPES"])).split(","),
    "OUTPUT_FILE": os.environ.get("OUTPUT_FILE", DEFAULT_CONFIG["OUTPUT_FILE"]),
    "CONSOLE_OUTPUT": os.environ.get("CONSOLE_OUTPUT", str(DEFAULT_CONFIG["CONSOLE_OUTPUT"])).lower() == "true"
}

# Set log distribution
LOG_DISTRIBUTION = {}
for log_type in config["LOG_TYPES"]:
    env_key = f"LOG_DIST_{log_type}"
    if log_type in DEFAULT_CONFIG["LOG_DISTRIBUTION"]:
        LOG_DISTRIBUTION[log_type] = int(os.environ.get(env_key, DEFAULT_CONFIG["LOG_DISTRIBUTION"][log_type]))
    else:
        LOG_DISTRIBUTION[log_type] = int(os.environ.get(env_key, 0))

config["LOG_DISTRIBUTION"] = LOG_DISTRIBUTION