# obsidian-vault
A repository that stores all templates, plugins, configuration settings and automation scripts to create new vaults tailored to my preferences and systems.

 Goal: To facilitate a cleaner note taking system and to avoid building a wiki, I have decided to try to archive all notes in past seasons and create new ones. This should allow me to build as I go.

Because all plugins, configurations, and settings are stored in the hidden `.obsidian` folder, all new vaults will not have their settings carried forward. 

# Archival and Renewal Process
1. Rename old vault to the relevant time period: `{start_month}-{end_month}-{year}`
2. Create a new vault that has your new seasonal theme. (If you don't have one yet, just name it "Notes")
3. Run my custom python script to install all Obsidian plugins, configurations, and templates for new vault.
4. Navigate to `Settings -> Sync (Under "Core Plugins") -> Choose (Under "Remote Vault)`. Delete the old remote vault and create a new one (local files will remain intact).