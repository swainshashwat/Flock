import json
from pathlib import Path

class PipelineWrapper:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def create_config(self, model_name, tasks, options=None):
        config = {
            "model_name": model_name,
            "tasks": tasks,
            "options": options or {}
        }

        with open(self.config_file_path, "w") as config_file:
            json.dump(config, config_file, indent=4)

# Usage example
if __name__ == "__main__":
    config_path = "pipeline_config.json"
    pipeline = PipelineWrapper(config_path)
    pipeline.create_config("my_model", ["task1", "task2"], options={"param": "value"})
