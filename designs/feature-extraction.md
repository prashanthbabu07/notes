We have file formats image, audio, and video. 

We need ability to extract information from these files. 

The solutions should be 
modular i.e. function based
ability to restart from any step
reuse of functions i.e. image to text, video to images and reuse image to text function
scalable to large files
video to audio and then audio to text
The video to image will generate large number of images. 

We have different services (api) microservices that needs to utilize these functions.
We need a way to orchestrate these functions. 
The functions can be synchronous or asynchronous (needs polling).
We need ability to track the progress of each step.
We need ability to communicate the state back to the calling service. 

All of these needs to utilize Azure cloud services.

[Blob Storage] -> [Image to text function] -> [Text Output]
[Blob Storage] -> [Audio to text function] -> [Text Output]

[Blob Storage] -> 
    -> [Video to image function]
        -> [Image Storage]
    -> [Image to text function] 
        -> [Text Output]
    -> [Video to audio function] 
        -> [Audio to text function] 
            -> [Text Output]

We have many customers and they will use these services. 
We need the ability to run these process in isolation from each others. 
    Such that one custommer usage does not impact the other customer usage.
We need ability to set limits on resource usage per customer.
We need ability to set parallelism per customer.
We need ability to monitor the usage per customer.


Functions should be stateless, but since we need to perform I/O inheriently there will have some state but as long
as we use file id they can still be considered stateless. 

All of the file data will be in blob storage. The file info will be in cosmos db.

i.e. when a file is uploaded via the api the file will be stored in blob storage 
and the file metadata will be stored in cosmos db needs a separate collections.

When a file goes through functions that logs needs to be maintaning and should be append only logs.

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



