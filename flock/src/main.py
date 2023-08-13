import uvicorn
from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import List, Dict
import requests, json
import subprocess

import magic

from pipelineManager.pipelineValidator import PipelineValidator

pipeline_validator = PipelineValidator()
app = FastAPI()

@app.get('/')
def root():
    return {"message": "App is running! :)"}

@app.post("/create-pipeline/")
def create_pipeline_config(data: List[str], pipeline_config: dict):
    try:
        if pipeline_validator.validate(pipeline_config):

            # Save pipeline config to a temporary YAML file -- TBD -- Save in MongoDB
            with open("pipelines/temp_pipeline_config.yml", "w") as pipeline_json_file_path:
                json.dumps(pipeline_config, pipeline_json_file_path)
        
            # Data processing data_processing.py script with subprocess
            subprocess.run(["python", "data_processing.py", "temp_pipeline_config.yml"])

            return {"message": "Data processing completed."}
    
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/upload-from-link/")
def upload_from_link(link: str):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            content_type = response.headers.get("content-type")
            if "pdf" in content_type.lower():
                # Process PDF content
                pdf_content = response.content
                # Process the PDF content here
                return {"message": "PDF content received and processed."}
            elif "text" in content_type.lower() or "html" in content_type.lower():
                # Process text or HTML content
                text_content = response.content.decode("utf-8")
                # Process the text or HTML content here
                return {"message": "Text or HTML content received and processed."}
            else:
                return {"error": "Unsupported content type."}
        else:
            return {"error": "Unable to fetch content from link."}
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch content from link."}
    
@app.post("/upload-from-directory/")
def upload_from_directory(files: List[UploadFile] = File(...)):
    try:
        for file in files:
            content_type = magic.Magic()
            file_type = content_type.from_buffer(file.file.read())

            if "pdf" in file_type.lower():
                # Process PDF file
                pdf_content = file.file.read()

            elif "text" in file_type.lower() or "html" in file_type.lower():
                # Process text or HTML file
                text_content = file.file.read().decode("utf-8")
                # Process the text or HTML content here

            else:
                return {"error" : f"Unsupported file type: {file_type}"}
            

        return {"message": f"Uploaded and processed {len(files)} files from directory."}


    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
