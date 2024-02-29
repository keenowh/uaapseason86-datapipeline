from googleapiclient.discovery import build

def hello_pubsub():   
 
    service = build('dataflow', 'v1b3')
    project = "uaap-season-86-dp"

    template_path = "gs://dataflow-templates-asia-southeast1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-loadmatchdata",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://uaaps86dataflow_metadata/udf.js",
        "JSONPath": "gs://uaaps86dataflow_metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "uaap-season-86-dp:matchstats.playerandmatchstats",
        "inputFilePattern": "gs://uaapseason86bucket/file.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://uaaps86dataflow_metadata/temp/",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

hello_pubsub()