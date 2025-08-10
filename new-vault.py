from dotenv import load_dotenv
import shutil
import argparse
import os

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('vaultName', nargs='?', default="Notes")
args = parser.parse_args()

print("Copying to", os.getenv("VaultPath"), args.vaultName)
# Copy Vault-Template to your VaultPath
dst = os.path.abspath(os.getenv("VaultPath"))
src = "Vault-Template"
shutil.copytree(src, dst)
# Rename "Vault-Template" to "vaultName"
