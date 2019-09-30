# s3bucketcopy
here there are 3 files(yaml,lamdbda function,helper script) where 

helper script:

converts the python and yaml file into .zip file and uploads it into the bucket on aws and creates the stack
if the stack is already made then the scripts deletes it and creates the new one in the place

new implementations:

use of environment variables for declaring the bucket name
new policies for lambda to access s3





