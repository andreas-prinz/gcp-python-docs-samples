# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START functions_log_stackdriver]
import base64
import json

# [END functions_log_stackdriver]


# [START functions_log_helloworld]
def hello_world(data, context):
    """Background Cloud Function.
    Args:
         data (dict): The dictionary with data specific to the given event.
         context (google.cloud.functions.Context): The event metadata.
    """
    print("Hello, stdout!")


# [END functions_log_helloworld]


# [START functions_log_stackdriver]
def process_log_entry(data, context):
    data_buffer = base64.b64decode(data["data"])
    log_entry = json.loads(data_buffer)["protoPayload"]

    print(f"Method: {log_entry['methodName']}")
    print(f"Resource: {log_entry['resourceName']}")
    print(f"Initiator: {log_entry['authenticationInfo']['principalEmail']}")


# [END functions_log_stackdriver]
