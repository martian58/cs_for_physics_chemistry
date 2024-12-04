import re
import csv

# TASK 1

# Task 1a: Parse a Chemical Formula
def parse_chemical_formula(formula: str) -> dict:
    """
    This function parses a chemical formula and returns a dictionary with element symbols as keys 
    and their counts as values.

    Args:
        formula (str): The chemical formula to parse.

    Returns:
        dict: A dictionary with chemical elements as keys and their atom counts as values.
            - Example: {'C': 6, 'H': 12, 'O': 6}.
    """

    # Pattern for regular expressions
    """
    [A-Z]: Matches an uppercase letter, representing the first letter of an element's symbol.
    [a-z]*: Matches zero or more lowercase letters, representing the optional second letter in a two-letter element symbol.
    (\\d*): Matches zero or more digits, representing the count of atoms for the element.
    """
    pattern = r"([A-Z][a-z]*)(\d*)"
    elements = re.findall(pattern, formula)
    element_dict = {}
    for element, count in elements:
        #This retrieves the current value of the key element in the dictionary. If the key doesn't exist in the dictionary, it defaults to 0.
        element_dict[element] = element_dict.get(element, 0) + int(count) if count else 1
    return element_dict

# Task 1b: Find Molecules Mathing Criteria from formula.csv
def filter_molecules_with_criteria(file_path: str, criteria: dict) -> list:
    """
    This function filters molecules from a CSV file based on specific atom count criteria. (Task 1b)

    Args:
        file_path (str): Path to the CSV file with chemical formulas.
        criteria (dict): Dictionary specifying the required atom counts. Example: "{"C": 2, "H": 5}"

    Returns:
        list: Names of molecules mathing the criteria.
    """
    results = []  

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')  # Delimiter to match the format: "Acetic acid;CH3COOH"

        for row in reader:
            name = row[0]
            formula = row[1]

            atoms = parse_chemical_formula(formula)

            # Check if the molecule mathes the criteria
            matches_criteria = True  
            for atom, count in criteria.items():
                # If atom's count doesn't match the criteria, set matches_criteria to False
                if atoms.get(atom, 0) != count:
                    matches_criteria = False
                    break

            # If the molecule matches all criteria, add its name to the results
            if matches_criteria:
                results.append(name)

    return results  


# TASK 2

# Task 2c: Parse a Balanced Chemical Equation
def parse_balance_equation(equation: str) -> tuple:
    """
    This functionn parses a balanced chemical equation into reactants and products. (Task 2c)

    Args:
        equation (str): The chemical equation to parse. Example: "2H2+O2->2H2O".

    Returns:
        tuple: Two lists containing reactants and products as formulas.
    """
    # Split reactants and products with "->"
    reactants, products = equation.split("->")
    # Split reactants  with "+"
    reactants = reactants.split("+")
    # Split products with "+"
    products = products.split("+")
    return reactants, products


# Task 2d: Create Dictionaries for Reactants and Products
def parse_coefficient_and_formula(component: str) -> tuple:
    """
    This function splits a molecule component into its coefficient and formula. (Task 2d)

    Args:
        component (str): Molecule with coefficient (e.g., '2H2').

    Returns:
        tuple: Coefficient (int) and formula (str).
    """
    match = re.match(r"(\d+)?([A-Za-z0-9]+)", component)
    if match:
        coefficient = int(match.group(1)) if match.group(1) else 1
        formula = match.group(2)
        return coefficient, formula
    raise ValueError("Invalid component format")


# Task 2e: Check if a Chemical Equation is Balanced
def is_balanced_equation(equation: str) -> bool:
    """
    This function checks if a chemical equation is balanced. (Task 2e)

    Args:
        equation (str): The chemical equation to check.

    Returns:
        bool: True if the equation is balanced, False otherwise.
    """
    reactants, products = parse_balance_equation(equation)
    reactant_atoms = {}
    product_atoms = {}

    for reactant in reactants:
        coefficient, formula = parse_coefficient_and_formula(reactant)
        atoms = parse_chemical_formula(formula)
        for atom, count in atoms.items():
            reactant_atoms[atom] = reactant_atoms.get(atom, 0) + count * coefficient

    for product in products:
        coefficient, formula = parse_coefficient_and_formula(product)
        atoms = parse_chemical_formula(formula)
        for atom, count in atoms.items():
            product_atoms[atom] = product_atoms.get(atom, 0) + count * coefficient

    return reactant_atoms == product_atoms


# Task 2f: Find Line Numbers of Balanced Equations from balanceequation1.csv
def find_balanced_equations(file_path: str) -> list:
    """
    This function finds line numbers of balanced equations in a CSV file. (Task 2f)

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: Line numbers of balanced equations.
    """
    balanced_lines = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')  # Adjust delimiter if needed
        for i, row in enumerate(reader, start=1):
            if len(row) == 0:
                continue  # Skip empty rows
            equation = row[0]
            if is_balanced_equation(equation):
                balanced_lines.append(i)
    return balanced_lines


# Task 2g: Count Number of Balanced Equations in balanceequation2.csv
def count_balanced_equations(file_path: str) -> int:
    """
    This function counts the number of balanced equations in a CSV file. (Task 2g)

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        int: Count of balanced equations.
    """
    return len(find_balanced_equations(file_path))






# Task 1a Example
formula = "C6H12O6"
print("Parsed formula (Task 1a):", parse_chemical_formula(formula),'\n')

# Task 1b Example
filtered_molecules = filter_molecules_with_criteria("Formula.csv", {"C": 2, "H": 5})
print("Filtered molecules (Task 1b):", filtered_molecules, '\n')

# Task 2c Example
equation = "2H2+O2->2H2O"
print("Parsed equation (Task 2c):", parse_balance_equation(equation), '\n')

# Task 2d Example: Extract Coefficients and Formulas from Reactants and Products
reactants, products = parse_balance_equation(equation)
print("Reactants and Products (Task 2d):")
for reactant in reactants:
    coeff, formula = parse_coefficient_and_formula(reactant)
    print(f"Reactant: {reactant}, Coefficient: {coeff}, Formula: {formula}")

for product in products:
    coeff, formula = parse_coefficient_and_formula(product)
    print(f"Product: {product}, Coefficient: {coeff}, Formula: {formula}\n")

# Task 2e Example
print("Is equation balanced (Task 2e):", is_balanced_equation(equation), '\n')

# Task 2f Example
balanced_lines = find_balanced_equations("BalanceEquation1.csv")
print("Balanced lines (Task 2f):", balanced_lines, '\n')

# Task 2g Example
total_balanced = count_balanced_equations("BalanceEquation2.csv")
print("Total balanced equations (Task 2g):", total_balanced, '\n')




