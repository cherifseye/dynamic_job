import os

def generate_test_batches():
  test_folder = "tests"
  test_files = [os.path.join(test_folder, f) for f in os.listdir(test_folder) if f.startswith("test")]
  if test_files:
    for i, test_file in enumerate(test_files):
      output_name = f"TEST_BATCH_{i+1}"
      print(f"{output_name}::{os.path.relpath(test_file)}")

if __name__ == "__main__":
  generate_test_batches()
