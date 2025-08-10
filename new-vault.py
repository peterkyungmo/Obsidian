from dotenv import load_dotenv
from pathlib import Path
import shutil
import argparse
import os


load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('vaultName', nargs='?', default="Notes")
args = parser.parse_args()

# Copy Vault-Template to your VaultPath
dst = Path('vaults') / args.vaultName
src = "template"
print("Creating", args.vaultName, "to", dst)
shutil.copytree(src, dst)