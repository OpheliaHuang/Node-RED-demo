# Node-RED-Demo
This is a Node-RED project that converts news feed into json format.

## Setup

1. Install Node-RED from `https://nodered.org/`.
2. Open into terminal `cd` into cloned repository.
3. Run Node-RED via command `node-red --port {port-number} news.json`. This will start this Node-RED project with your selected port.
4. Access the result via `http://127.0.0.1:{port-number}/all`


## Current Implementation:

`GET /all` -- Return a list of all news, sorted by latest publish date.

