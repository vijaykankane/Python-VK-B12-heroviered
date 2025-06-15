import configparser
import json
import os

def parse_config(config_file):
    config_data = {}
    config = configparser.ConfigParser()

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

    config.read(config_file)

    for section in config.sections():
        config_data[section] = {}
        for key in config[section]:
            config_data[section][key] = config[section][key]

    return config_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Configuration data saved to {output_file}")

if __name__ == "__main__":
    try:
        config_file = 'config.ini'
        output_file = 'config_data.json'

        config_data = parse_config(config_file)
        print("Configuration File Parser Results:\n")
        for section, values in config_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
            print()

        save_to_json(config_data, output_file)

    except Exception as e:
        print(f"Error: {e}")
