# Custom API Skill for Azure Search with Serverless (Python)

## Background

[Cognitive Search](https://docs.microsoft.com/en-us/azure/search/cognitive-search-concept-intro) is an AI feature in Azure Search, used to extract text from images, blobs, and other unstructured data sources - enriching the content to make it more searchable in an Azure Search index. Extraction and enrichment are implemented through cognitive and custom skills attached to an indexing pipeline.

This repository contains an Azure Function (Python HTTP Trigger) that leverages the Custom Web API skill feature, allowing you to extend Cognitive Search by calling out to an API endpoint providing custom operations.

## Prerequisites

Before you start, you must have the following:

- [Python 3.6](https://www.python.org/downloads/) or later
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) v2.7.1575 or later
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) v2.x or later

For a better development experience it's recommended the use of [Visual Studio Code](https://code.visualstudio.com/) with [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) extensions.
