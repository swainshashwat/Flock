class PipelineValidator:
    def __init__(self) -> None:
        print("Validating Pipeline...")
        pass

    def validate(self, pipeline: dict) -> dict:
        if pipeline is None:
            print({"message": "Missing Pipeline"})
            return False
        else:
            print({"message": "Pipeline Validated"})
            return True