# Solution Considerations: File Scanning and Content Moderation

## File Formats and Extraction

- We have file formats: **image, audio, and video**.
- **All files should go through security scanning as a pre-requisite.**
- We need the ability to extract information from these files.

## Solutions Architecture

Things to think about for the solution:
- Solutions should be **modular**, i.e., function-based.
- There should be **ability to restart from any step** in the process.
- We want to enable **reuse of functions**. For example:
  - Use *image to text* for both direct image files and video-extracted images.
  - Use *video to images*, then apply *image to text*.
  - Use *video to audio* and then *audio to text*.
- Solutions should be **scalable to large files**.
- The **video to image** step will generate a large number of images.

## Orchestration & Integration

- We have different services (APIs, microservices) that need to utilize these functions.
- We need a way to **orchestrate these functions**.
- The functions can be **synchronous or asynchronous** (with polling where needed).
- We need the ability to **track the progress of each step**.
- We need the ability to **communicate the state back to the calling service**.

## Azure Cloud Usage

- **All of these need to utilize Azure cloud services.**

## Example Workflows

- All files should go through security scan first:  
  `[Blob Storage] -> [Security Scan Function] -> [Scan Output]`

- For images:  
  `[Blob Storage] -> [Image to metadata function] -> [Metadata Output]`  
  `[Blob Storage] -> [Image to text function] -> [Text Output]`

- For audio:  
  `[Blob Storage] -> [Audio to metadata function] -> [Metadata Output]`  
  `[Blob Storage] -> [Audio to text function] -> [Text Output]`

- For video:  
  `[Blob Storage] -> [Video to metadata function] -> [Metadata Output]`  
  `[Blob Storage] ->`  
  `    -> [Video to image function]`  
  `        -> [Image Storage]`  
  `    -> [Image to text function]`  
  `        -> [Text Output]`  
  `    -> [Video to audio function]`  
  `        -> [Audio to text function]`  
  `            -> [Text Output]`

## Multi-Customer Environment

- We have **many customers and they will use these services**.
- We need the **ability to run these processes in isolation from each other**, so that one customer’s usage does not impact another’s.
- We need the **ability to set limits on resource usage per customer**.
- We need the **ability to set parallelism per customer**.
- **Monitor the usage per customer**.

## Stateless Functions & Data Storage

- Functions should be **stateless**. Since we need to perform I/O, there will be some state involved, but as long as we use file id you can still consider them stateless.
- **All file data will be in blob storage. File info will be in Cosmos DB.**
  - When a file is uploaded via the API, the file will be stored in blob storage.
  - File metadata will be stored in Cosmos DB (requires separate collections).
- When a file goes through functions, **logs need to be maintained (append-only logs)**.

Example log/document structure:
```json
{
    "fileId": "unique-file-id",
    "type": "image/audio/video",
    "customerId": "customer-id",
    "fileLocation": "<blob info>",
    "status": "new/...",
    "logs": [ 
        {
            "timestamp": "2024-06-01T12:00:00Z",
            "message": "File uploaded to blob storage."
        },
        {
            "timestamp": "2024-06-01T12:05:00Z",
            "message": "Processing started."
        }
    ]
}
```
