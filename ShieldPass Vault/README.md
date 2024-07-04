# ShieldPass Vault

Never save another password on your browser! Keep them save with this simple and effective password manager.

## Setup

1. **Clone the Repository**:
 
   1.1 **Initialize a New Git Repository**:

    ```sh
    mkdir 'ShieldPass Vault'
    cd 'ShieldPass Vault'
    git init
    ```

    1.2 **Add the Remote Repository**:

    ```sh
    git remote add origin https://github.com/rjrato/Python-Projects.git
    ```

    1.3 **Enable Sparse Checkout**:

    ```sh
    git config core.sparseCheckout true
    ```

    1.4 **Define the Subdirectory to Checkout**:

    Create a `.git/info/sparse-checkout` file and add the path to the subdirectory you want to checkout:

    ```sh
    echo "ShieldPass Vault/" >> .git/info/sparse-checkout
    ```

    1.5 **Pull from the Remote Repository**:

    ```sh
    git pull origin main
    ```

2. **Install Dependencies**:

    Make sure you have `pip` installed. Then, run:

    ```sh
    pip install -r requirements.txt
    ```

3. **Generate a Secret Key**:

   You need to generate a secret key for encryption and decryption. Run the following Python script to generate the `secret.key` file:

   ```python
   from cryptography.fernet import Fernet

   def generate_key():
       key = Fernet.generate_key()
       with open("secret.key", "wb") as key_file:
           key_file.write(key)
   
   generate_key()
   ```

   You can create a separate script called `generate_key.py` with the above code and run it:

   ```sh
    python generate_key.py
    ```

    **Note:** Make sure this file is not included in your repository by adding `secret.key` to your `.gitignore` file.

4. **Run the Application**:

    You can now run the main application:

    ```sh
    python main.py
    ```

## Usage

- **Save a Password**: Enter the website, email, and password, and click 'Save'. You can also generate a random password.
- **Search for a Password**: Enter the website name and click 'Search'.

## Important Notes

- **Do Not Share Your `secret.key` File**: The `secret.key` file is unique to you. Do not share it or upload it to GitHub.
- **Backup Your Data**: Ensure you have backups of your `data.json` and `secret.key` files. Losing your `secret.key` means you will not be able to decrypt your passwords.