import os
import json


def generate_test_batches():
  list_jobs_dict = []
  test_folder = "tests"
  test_files = [os.path.join(test_folder, f) for f in os.listdir(test_folder) if f.startswith("test")]
  if test_files:
    for i, test_file in enumerate(test_files):
      output_name = f"TEST_BATCH_{i+1}"
      dict_job = {}
      dict_job["name"] = output_name
      dict_job["path"] = test_file
      list_jobs_dict.append(dict_job)
      
  with open(os.environ["GITHUB_OUTPUT"], 'w') as f:
    f.write(f"test_batches = {json.dumps(list_jobs_dict)}")

if __name__ == "__main__":
  generate_test_batches()
