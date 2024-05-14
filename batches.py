import os
import json


def generate_test_batches():
  test_jobs_list = []
  test_folder = "tests"

  #Obtenir une liste des chemins des fichiers de test du dossier 
  test_files = [os.path.join(test_folder, f) for f in os.listdir(test_folder) if f.startswith("test")]

  if test_files:
    #Pour chaque fichiers de test generer un nom de lot de batch
    for i, test_file in enumerate(test_files):
      output_name = f"TEST_BATCH_{i+1}"
      test_jobs_list.append({"name": output_name, "path": test_file})
  
  #ouvrir le fichier GITHUB_OUTPUT en mode ajout et ecrire en format json l'output pour la matrice.
  with open(os.environ["GITHUB_OUTPUT"], 'a') as f:
    f.write(f"test_batches={json.dumps(test_jobs_list)}")

if __name__ == "__main__":
  generate_test_batches()
