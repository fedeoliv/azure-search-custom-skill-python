# Custom API Skill for Azure Search with Serverless (Python)

## Background

[Cognitive Search](https://docs.microsoft.com/en-us/azure/search/cognitive-search-concept-intro) is an AI feature in Azure Search, used to extract text from images, blobs, and other unstructured data sources - enriching the content to make it more searchable in an Azure Search index. Extraction and enrichment are implemented through cognitive and custom skills attached to an indexing pipeline.

This repository contains an Azure Function (Python HTTP Trigger) that implements the [Web API custom skill interface](https://docs.microsoft.com/en-us/azure/search/cognitive-search-custom-skill-interface#web-api-custom-skill-interface), allowing you to extend Cognitive Search by calling out to an API endpoint providing custom operations.

## Prerequisites

Before you start, you must have the following:

- [Python 3.6](https://www.python.org/downloads/) or later
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) v2.7.1575 or later
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) v2.x or later

For a better development experience it's recommended the use of [Visual Studio Code](https://code.visualstudio.com/) with [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) extensions.

## About the sample

The sample is a framework that can be used for any Azure Search custom skill you want, it is not tied to any specific service except Azure Functions. Key features/advantages:

- Developers only have to worry about the business logic and fill the `values` property as the output.
- Built with [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) schemas, strengthening data consistency by serializing/deserializing objects to primitive Python types and simplifying data validation.

## How to use

```python
import logging
import azure.functions as func
from typing import List
from .models.output import OutputRecord
from .utils.schemas_helper import output_dumps
from .utils.functions_helper import load_request, bad_request, ok

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Custom kill processed a request.')

    req_result: RequestResult = load_request(req)

    if not req_result.valid:
        return bad_request(req_result.error)

    input_skill: InputSkill = req_result.input_skill

    # YOUR CODE HERE

    values: List[OutputRecord] = [] # Update your values property
    output_json, error = output_dumps(values)

    if error:
        return bad_request('Invalid output format')
    
    return ok(output_json)
```

In the Azure Functions main file, there are basically three tasks that need to be done:

1. Read data from `input_skill` and create your logic/processing (e.g. replace words from documents, apply regex, etc)
2. Update the `OutputData` class with the property name you defined on Azure Search. In this sample, the generic property name created was `contractTextProcessed`.
3. Update the `values` list with results from the previous processing.

## Running Unit Tests

The sample uses [unittest](https://docs.python.org/2/library/unittest.html) framework. You can follow the [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing) article to configure your VSCode to run unit tests. Otherwise, you can test through command line:

```sh
python -m unittest discover ./skill/tests
```

**Note:** All tests are under the `skill/tests` folder, so make sure you are not looking only on `skill` folder by default.
