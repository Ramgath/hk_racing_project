# src/common/config_loader.py
import yaml
from pathlib import Path

# import os # We need os for os.environ.get, os.path.isfile, os.path.expanduser

# Define the absolute path to the project root directory.
# This assumes 'config_loader.py' is in 'src/common/'.
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Define the path to the actual configuration file (not the example)
CONFIG_FILE_NAME = "config.yaml"
CONFIG_DIR_NAME = "config"
CONFIG_FILE_PATH = PROJECT_ROOT / CONFIG_DIR_NAME / CONFIG_FILE_NAME

# Define the path to the example configuration file
EXAMPLE_CONFIG_FILE_PATH = (
    PROJECT_ROOT / CONFIG_DIR_NAME / f"{CONFIG_FILE_NAME}.example"
)


def load_config() -> dict:
    """
    Loads the project configuration from config/config.yaml.

    Raises:
        FileNotFoundError: If config.yaml is not found. It advises the user
                           to copy and configure config.yaml.example.
        yaml.YAMLError: If there's an error parsing the YAML file.

    Returns:
        dict: The loaded configuration.
    """
    if not CONFIG_FILE_PATH.exists():  # Path.exists() is fine
        error_message = (
            f"Configuration file not found at: {CONFIG_FILE_PATH}\n"
            f"Please create it by copying the example file "
            f"'{EXAMPLE_CONFIG_FILE_PATH}' to '{CONFIG_FILE_PATH}' "
            f"and then update it with your specific settings."
        )
        raise FileNotFoundError(error_message)

    try:
        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
        if config_data is None:  # Handle empty YAML file case
            print(f"Warning: Configuration file '{CONFIG_FILE_PATH}' is empty.")
            return {}
        return config_data
    except yaml.YAMLError as e:
        error_message = (
            f"Error parsing YAML configuration file '{CONFIG_FILE_PATH}': {e}"
        )
        raise yaml.YAMLError(error_message) from e
    except Exception as e:
        error_message = f"An unexpected error occurred while loading configuration from '{CONFIG_FILE_PATH}': {e}"
        raise RuntimeError(error_message) from e


# Example of how to use the loader (you would typically do this in other scripts)
if __name__ == "__main__":
    # The F401 for 'os' at the top of the file (line 4) implies 'os' might not be used.
    # However, the original version of this example block might have used os.path or os.environ
    # For now, 'os' is kept for os.environ.get() if you plan to use it for credentials.
    # If you don't use os.environ.get() or any other os functions in this file, remove 'import os'.

    print(
        f"Attempting to load configuration from: {CONFIG_FILE_PATH}"
    )  # This f-string has a placeholder
    try:
        config = load_config()

        google_cloud_config = config.get("google_cloud", {})
        project_id = google_cloud_config.get("project_id")
        dataset_id = google_cloud_config.get("bq_dataset_id")

        if project_id:
            # Line 76: F541 fix
            print("  Successfully loaded configuration.")
            print(f"  GCP Project ID: {project_id}")  # This f-string has a placeholder
        else:
            # Line 79: F541 fix
            # For E713 on line 79: check if there's a 'not ... in ...' condition nearby or within this block.
            # If the error was for a line like 'if not key in dict:', change to 'if key not in dict:'.
            print("  GCP Project ID not found in configuration or config is empty.")

        if dataset_id:
            print(
                f"  BigQuery Dataset ID: {dataset_id}"
            )  # This f-string has a placeholder
        else:
            # Line 84: F541 fix
            # For E713 on line 84: similar to above, check for 'not ... in ...'.
            print("  BigQuery Dataset ID not found in configuration.")

    except FileNotFoundError as e:
        print(f"ERROR: {e}")  # This f-string has a placeholder
        print("Please ensure your 'config/config.yaml' file is set up correctly.")
    except yaml.YAMLError as e:
        print(f"YAML PARSING ERROR: {e}")  # This f-string has a placeholder
    except RuntimeError as e:
        print(f"RUNTIME ERROR: {e}")  # This f-string has a placeholder
    except Exception as e:
        print(
            f"An unexpected error occurred during the example usage: {e}"
        )  # This f-string has a placeholder
