import pandas as pd
import urllib.request
import re

# ANSI color codes for colorful prints 
BLUE = "\033[1;36m"  # Blue color 
RESET = "\033[0m"    # Reset code

class AminoAcidAnalyzer:
    """
    A class to analyze amino acid datasets.
    It performs various tasks, such as fetching molecular data, calculating atomic counts, and analyzing amino acids.
    """

    def __init__(self, input_file: str):
        """
        Initialize the AminoAcidAnalyzer class with the given input file.
        
        Parameters:
        - input_file (str): Path to the CSV file containing amino acid data.
        """
        self.file = input_file  
        self.df = pd.read_csv(input_file)  # Load the data from the CSV into a Pandas DataFrame

    # Task 2b: Fetch molecular data from PubChem API and enrich the dataset
    def fetch_molecular_data(self):
        """
        This method enriches the dataset by adding molecular formula and molar mass for each amino acid.
        It fetches this information from the PubChem API.

        Updates:
        - Adds 'ChemicalFormula' column with the molecular formula.
        - Adds 'MolarMass' column with the molar mass.
        """
        # Inner function to fetch data from PubChem API
        def retrieve_info(compound):
            """
            Fetch the molecular formula and molar mass for a given compound.

            Parameters:
            - compound (str): The name of the compound. Example: 'Lysine'.

            Returns:
            - tuple: A tuple with the formula and molar mass, or None if an error occurs.
            """
            # Replace empty spaces with '%20' which is url encoded form of empty space. 
            compound_url = compound.replace(" ", "%20")
            # Build the PubChem API URL
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_url}/property/MolecularFormula,MolecularWeight/CSV"
            try:
                # Open the url and fetch the data as a CSV file
                with urllib.request.urlopen(url) as response:
                    data = pd.read_csv(response)  # Load the CSV data into a DataFrame
                    # Return the first entry for MolecularFormula and MolecularWeight
                    return data['MolecularFormula'][0], data['MolecularWeight'][0]
            except Exception:
                # Return None if an error occurs while fetching data
                return None, None

        # Add placeholders for 'ChemicalFormula' and 'MolarMass' columns
        self.df['ChemicalFormula'] = None
        self.df['MolarMass'] = None

        # Iterate through each amino acid in the dataset to fetch its molecular data
        for compound in self.df['Name']:
            formula, mass = retrieve_info(compound)  # Get the formula and mass for each compound
            # Update the DataFrame with the fetched information
            self.df.loc[self.df['Name'] == compound, 'ChemicalFormula'] = formula
            self.df.loc[self.df['Name'] == compound, 'MolarMass'] = mass

        # Save the updated dataset back to the original file
        self.df.to_csv(self.file, index=False)

    # Task 2c: Compute the atomic count of elements (H, C, N, O, S) for each compound
    def compute_atomic_counts(self):
        """
        This method calculates the count of atoms (H, C, N, O, and S) in the molecular formulas
        for each compound in the dataset.

        Updates:
        - Adds columns 'H', 'C', 'N', 'O', 'S' to the DataFrame with atom counts.
        """
        def parse_formula(formula):
            """
            This function extracts atom counts from a given chemical formula.

            Parameters:
            - formula (str): A chemical formula. Example: 'C6H14N2O2'.

            Returns:
            - dict: A dictionary with atom counts for the elements of interest (H, C, N, O, S).
            """
            # Regular expression to find elements and their counts in the formula
            pattern = r"([A-Z][a-z]*)(\d*)"
            matches = re.findall(pattern, formula)  # Find all matches (element and its count)
            # Initialize the count for each element of interest
            element_counts = {key: 0 for key in ['H', 'C', 'N', 'O', 'S']}
            for element, count in matches:
                if element in element_counts:
                    # If a count is specified, use it, otherwise default to 1
                    element_counts[element] += int(count) if count else 1
            return element_counts

        # Add new columns for each element with initial counts of 0
        for element in ['H', 'C', 'N', 'O', 'S']:
            self.df[element] = 0

        # Go through each formula in the dataset and compute atom counts
        for formula in self.df['ChemicalFormula']:
            if pd.notna(formula):  # Only process valid formulas
                counts = parse_formula(formula)  # Parse the formula for atom counts
                # Update the DataFrame with the atom counts
                for element, count in counts.items():
                    self.df.loc[self.df['ChemicalFormula'] == formula, element] = count

        # Save the enriched dataset back to the original file
        self.df.to_csv(self.file, index=False)

    # Task 3a-3g: Perform analysis on the dataset and display results
    def perform_analysis(self):
        """
        This method analyzes the dataset and displays various results based on given tasks.
        """
        # Display the dataset overview
        print(f"{BLUE}Dataset Overview:{RESET}")
        print(self.df.to_string(), "\n")  # Print the entire dataset

        # Task 3a: Display all information about lysine
        print(f"{BLUE}a. Information about Lysine (Exercise 3a):{RESET}")
        print(self.df[self.df['Name'].str.lower() == 'lysine'], "\n")

        # Task 3b: Find and display the heaviest amino acid
        print(f"{BLUE}b. The heaviest amino acid (Exercise 3b):{RESET}")
        print(self.df.loc[self.df['MolarMass'] == self.df['MolarMass'].max()], "\n")

        # Task 3c: Display amino acids with positive polarization
        print(f"{BLUE}c. Amino acids with positive polarization (Exercise 3c):{RESET}")
        print(self.df[self.df['Polarization'] == 'positive'], "\n")

        # Task 3d: Count the number of molecules by polarization type
        print(f"{BLUE}d. Number of molecules by polarization type (Exercise 3d):{RESET}")
        print(self.df['Polarization'].value_counts(), "\n")

        # Task 3e: Find the heaviest molecule for each polarization type
        print(f"{BLUE}e. The heaviest molecule for each polarization type (Exercise 3e):{RESET}")
        print(self.df.loc[self.df.groupby('Polarization')['MolarMass'].idxmax()], "\n")

        # Task 3f: Display molecules that contain at least 1 sulfur atom
        print(f"{BLUE}f. Molecules with at least 1 sulfur atom (Exercise 3f):{RESET}")
        print(self.df[self.df['ChemicalFormula'].str.contains('S', na=False)], "\n")

        # Task 3g: Find and display the molecule with the most hydrogen atoms
        print(f"{BLUE}g. The molecule with the most hydrogens (Exercise 3g):{RESET}")
        print(self.df.loc[self.df['H'] == self.df['H'].max()], "\n")

    # Task 4: Backup the enriched data and reset the original dataset
    def save_final_data(self):
        """
        Create a backup of the enriched dataset and reset the original dataset.
        """
        enriched_file = "AminoAcids_Backup.csv"  # Name of the backup file
        self.df.to_csv(enriched_file, index=False)  # Save the enriched dataset to the backup file

        # Reset the original dataset by dropping the enrichment columns
        reset_df = self.df.drop(columns=['ChemicalFormula', 'MolarMass', 'H', 'C', 'N', 'O', 'S'])
        reset_df.to_csv(self.file, index=False)  # Save the reset dataset to the original file

        print(f"{BLUE}Backup saved as {enriched_file}, original file reset.{RESET}")


if __name__ == "__main__":
    # Define the input file for the dataset
    input_file = "AminoAcids.csv"
    analyzer = AminoAcidAnalyzer(input_file) 

    analyzer.fetch_molecular_data()  
    analyzer.compute_atomic_counts()  
    analyzer.perform_analysis()  
    analyzer.save_final_data() 
