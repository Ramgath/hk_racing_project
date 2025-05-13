# src/common/config_loader.py
import yaml
from pathlib import Path

# Define the absolute path to the project root directory.
# This assumes 'config_loader.py' is in 'src/common/'.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

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
        RuntimeError: For other unexpected errors during loading.

    Returns:
        dict: The loaded configuration.
    """
    if not CONFIG_FILE_PATH.exists():
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
        # Re-raise as YAMLError to be specific, but include original exception
        raise yaml.YAMLError(error_message) from e
    except Exception as e:
        # Catch any other unexpected errors during file operations or loading
        error_message = f"An unexpected error occurred while loading configuration from '{CONFIG_FILE_PATH}': {e}"
        raise RuntimeError(error_message) from e


# Example of how to use the loader (you would typically do this in other scripts)
if __name__ == "__main__":
    print(f"Attempting to load configuration from: {CONFIG_FILE_PATH}")
    try:
        config = load_config()

        # Access Google Cloud configurations safely
        google_cloud_config = config.get(
            "google_cloud", {}
        )  # Default to empty dict if 'google_cloud' key is missing

        project_id = google_cloud_config.get("project_id")
        main_dataset_id = google_cloud_config.get("bq_main_dataset_id")
        scraped_raw_dataset_id = google_cloud_config.get("bq_scraped_raw_dataset_id")

        if not config:  # Checks if the loaded config is empty
            print("  Configuration loaded, but it's empty.")
        else:
            print("  Successfully loaded configuration.")

            if project_id:
                print(f"  GCP Project ID: {project_id}")
            else:
                print("  GCP Project ID not found in configuration.")

            if main_dataset_id:
                print(f"  BigQuery Main Dataset ID: {main_dataset_id}")
            else:
                print("  BigQuery Main Dataset ID (bq_main_dataset_id) not found.")

            if scraped_raw_dataset_id:
                print(f"  BigQuery Scraped Raw Dataset ID: {scraped_raw_dataset_id}")
            else:
                print(
                    "  BigQuery Scraped Raw Dataset ID (bq_scraped_raw_dataset_id) not found."
                )

    except FileNotFoundError as e_fnf:
        print(f"ERROR: {e_fnf}")
        print(
            f"Please ensure your '{CONFIG_DIR_NAME}/{CONFIG_FILE_NAME}' file is set up correctly."
        )
    except yaml.YAMLError as e_yml:
        print(f"YAML PARSING ERROR: {e_yml}")
    except RuntimeError as e_rt:
        print(f"RUNTIME ERROR: {e_rt}")
    except (
        Exception
    ) as e_exc:  # Catch-all for any other unexpected errors during example execution
        print(f"An unexpected error occurred during the example usage: {e_exc}")
