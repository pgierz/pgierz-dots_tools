#!/usr/bin/env python3
import gnupg
import questionary
import subprocess

def generate_subkey():
    # Initialize GPG
    gpg = gnupg.GPG()

    # Fetch keys
    keys = gpg.list_keys()
    key_choices = {key['keyid']: f"{key['keyid']} ({key['uids'][0]})" for key in keys}

    # Prompt user to select a key
    selected_key = questionary.select(
        "Select a key to add subkeys:",
        choices=key_choices.values()
    ).ask()

    if selected_key:
        selected_key_id = [k for k, v in key_choices.items() if v == selected_key][0]

        # Generate subkeys
        subkey_type = questionary.select(
            "Select the type of subkey:",
            choices=["Encryption", "Signing", "Authentication"]
        ).ask()

        if subkey_type:
            subkey_type_map = {
                "Encryption": "encrypt",
                "Signing": "sign",
                "Authentication": "auth"
            }
            subkey_command = f"gpg --expert --edit-key {selected_key_id} addkey {subkey_type_map[subkey_type]}"

            # Ask for a comment for the subkey
            subkey_comment = questionary.text("Enter a comment for the subkey (optional):").ask()

            if subkey_comment:
                subkey_command += f' comment="{subkey_comment}"'
            
            # Print the command for illustration
            print(f"Command to execute: {subkey_command}")

            # Ask for confirmation
            confirm = questionary.confirm("Confirm executing the command above?").ask()

            if confirm:
                # Execute the command using subprocess
                process = subprocess.run(subkey_command, shell=True)

                # Check the exit code
                if process.returncode == 0:
                    print("Subkey added successfully.")
                else:
                    print("Failed to add subkey.")
            else:
                print("Operation cancelled.")
        else:
            print("No subkey type selected.")
    else:
        print("No key selected.")

def main():
    generate_subkey()

if __name__ == "__main__":
    main()

