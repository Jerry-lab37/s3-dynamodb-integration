# s3-dynamodb-integration
Step-by-step guide and Lambda code for integrating Amazon S3 with DynamoDB
**Step 1: Create an S3 Bucket**

1. **Navigate to the S3 Console**:
    - Go to the [Amazon S3 Console](https://console.aws.amazon.com/s3).
2. **Create a Bucket**:
    - Click **"Create bucket"**.
    - Enter a **Bucket Name**, e.g., `my-dynamodb-s3-bucket`.
    - Choose a **Region** close to you.
    - Keep the default settings (public access blocked).
    - Click **Create bucket**.

---

### **Step 2: Create a DynamoDB Table**

1. **Navigate to the DynamoDB Console**:
    - Go to the [Amazon DynamoDB Console](https://console.aws.amazon.com/dynamodb).
2. **Create a Table**:
    - Click **"Create table"**.
    - Enter:
        - **Table Name**: `FileMetadata`
        - **Partition Key**: `FileName` (String)
    - Click **Create**.
3. **Wait for Table Activation**:
    - Ensure the table status changes to **"Active"**.

---

### **Step 3: Create a Lambda Function**

1. **Navigate to the Lambda Console**:
    - Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda).
2. **Create a Function**:
    - Click **"Create function"**.
    - Choose **"Author from scratch"**.
    - Enter:
        - **Function Name**: `ProcessS3Event`
        - **Runtime**: Python 3.x (e.g., Python 3.9)
    - Click **Create Function**.
3. **Add IAM Permissions**:
    - Go to the **"Configuration"** tab of your function.
    - Click **Permissions**.
    - Click the **Execution role** link.
    - Attach the following policies:
        - `AmazonDynamoDBFullAccess`
        - `AmazonS3ReadOnlyAccess`

---

### **Step 4: Add Code to the Lambda Function**

1. **Edit the Function Code**:
    - Scroll to the **Code source** section.
    - Replace the existing code with the following.
2. **Deploy the Function**:
    - Click **Deploy** to save and apply changes.
### **Step 5: Configure S3 to Trigger Lambda**

1. **Navigate to Your S3 Bucket**:
    - Open the S3 bucket created earlier (`my-dynamodb-s3-bucket`).
2. **Set Up an Event Notification**:
    - Go to the **Properties** tab.
    - Under **Event notifications**, click **Create event notification**.
    - Enter:
        - **Event name**: `TriggerLambdaOnUpload`
        - **Event types**: Select **All object create events**.
        - **Destination**: Choose **Lambda Function** and select `ProcessS3Event`.
    - Click **Save**.

---

### **Step 6: Test the Integration**

1. **Upload a File to S3**:
    - Open your bucket in the S3 Console.
    - Click **Upload**, select a sample file (e.g., a `.txt`, `.jpg`, or `.csv` file).
    - Click **Upload**.
2. **Verify in DynamoDB**:
    - Go to the [DynamoDB Console](https://console.aws.amazon.com/dynamodb).
    - Open the `FileMetadata` table.
    - Check if the uploaded file's metadata (file name and bucket name) is recorded.

---

### **Step 7: Monitor Logs**

1. **Navigate to the Lambda Function**:
    - Open the Lambda function `ProcessS3Event`.
2. **View Logs**:
    - Go to **Monitor > Logs**.
    - Open the log streams in CloudWatch to verify the function executed successfully.
    - Look for logs confirming the metadata was processed and stored.
      
    

---

### **Step 8: Clean Up (Optional)**

To avoid unnecessary costs:

1. Delete the files in the S3 bucket and then the bucket.
2. Delete the DynamoDB table (`FileMetadata`).
3. Delete the Lambda function (`ProcessS3Event`).
  
