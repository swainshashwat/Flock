class Parameter:
    def __init__(self):
        self.parameter_dict = {
                "TRANSFORMERS.MODEL_NAME": {
                    "name" : "TRANSFORMER_MODEL.MODEL_NAME",
                    "description" : "Transformer model name",
                    "type" : "list",
                    "range" : ['llama2-7b', 'llama2-13b', 'wizardlm', 'bloom','falcon'],
                    "default": "llama2-7b"
                },
                "EMBEDDING.MODEL_NAME" : {
                    "name" : "EMBEDDING.MODEL_NAME",
                    "description" : "Emebedding model name",
                    "type" : "list",
                    "range" : ['hkunlp/instructor-base'],
                    "default": "hkunlp/instructor-base"
                },
                "OUTPUT.TRANSFORMERS.TEMPERATURE" : {
                    "name" : "OUTPUT_PARAMETERS.TEMPERATURE",
                    "description" : "Higher temperature values (e.g., 0.8 to 1.0) lead to more diverse and random output. Lower values (e.g., 0.2 to 0.5) make the output more focused and deterministic.",
                    "type" : "percentage",
                    "range" : [0,1],
                    "default": 0.0
                },
                "OUTPUT.TRANSFORMERS.TOP_P" : {
                    "name" : "OUTPUT_PARAMETERS.TOP_P",
                    "description" : "Higher top_p values (e.g., 0.8 to 1.0) allow more words to be considered, potentially resulting in more varied output. Lower values (e.g., 0.1 to 0.5) limit the set of words and may produce more controlled responses.",
                    "type" : "percentage",
                    "range" : [0, 1],
                    "default" : 0.95
                },
                
                "OUTPUT.TRANSFORMERS.REPETITION_PENALTY" : {
                    "name" : "OUTPUT_PARAMETERS.REPETITION_PENALTY",
                    "description" : "A higher repetition penalty (e.g., 1.2 or greater) increases the penalty for repeating words, encouraging the model to generate less repetitive text. Lower values reduce the effect of repetition penalties.",
                    "type" : "float",
                    "range" : [1, float("inf")],
                    "default" : 1.15     
                },
                "INPUT.TRANSFORMERS.SPLIT_CHUNK_SIZE" : {
                    "name" : "INPUT_PARAMETERS.SPLIT_CHUNK_SIZE",
                    "description" : "Smaller split chunk sizes (e.g., a few words or a sentence) allow for fine-grained processing but might result in more disjointed or fragmented output. Larger split chunk sizes (e.g., a few paragraphs) provide more context but could approach or exceed the model's input length limits.",
                    "type" : "integer",
                    "range" : [1 , float("inf")],
                    "default" : 800
                },
                "INPUT.TRANSFORMERS.SPLIT_OVERLAP" : {
                    "name" : "INPUT_PARAMETERS.SPLIT_OVERLAP",
                    "description" : "The split size needs to be smaller than the model's maximum input length. It could range from a few tokens to just below the maximum input length, depending on how much overlap you want between adjacent chunks for context continuity.",
                    "type" : "integer",
                    "range" : [0 , float("inf")],
                    "default" : 0
                }
        }

    def get_input_parameters(self):
        group_name = "INPUT"
        return list(filter(lambda x: group_name in x, self.parameter_dict.keys()))
    
    def get_output_parameters(self):
        group_name = "OUTPUT"
        return list(filter(lambda x: group_name in x, self.parameter_dict.keys()))