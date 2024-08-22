import pandas as pd
import numpy as np

def create_dataframe_example(
    size:int = 20,
    seed:int = 42
) -> pd.DataFrame:
    """
    Creates a pandas DataFrame with example data.

    This function generates a DataFrame containing the names of students, their scores in two subjects, 
    and the period of the day they attend classes. The DataFrame is generated with random data to 
    simulate real-world scenarios for testing or demonstration purposes.

    Parameters:
    -----------
    size : int, optional (default=20)
        The number of rows to include in the DataFrame. If a number greater than 20 is provided, 
        the function will only use the first 20 names from the predefined list.
        
    seed : int, optional (default=42)
        The seed for the random number generator, which ensures reproducibility of the random values.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with the following columns:
            - 'Nome' : The name of the student.
            - 'Nota_1' : A random integer representing the first score (between 50 and 100).
            - 'Nota_2' : A random integer representing the second score (between 50 and 100).
            - 'Turno' : The period of the day the student attends classes ('Manhã', 'Tarde', 'Noite').

    Example:
    --------
    >>> df = create_dataframe_example(size=10, seed=123)
    >>> print(df.head())
    """

    # Gerando dados de exemplo
    np.random.seed(seed)  # Para reprodutibilidade

    nomes = ['Alice', 'Bruno', 'Carla', 'Diego', 'Eva', 'Felipe', 'Gabi', 'Hugo', 'Iara', 'Jorge', 
            'Karen', 'Luis', 'Marina', 'Nina', 'Otávio', 'Paula', 'Quico', 'Rafa', 'Silvia', 'Thiago']
    nomes = nomes[:size]


    nota1 = np.random.randint(50, 100, size=size)
    nota2 = np.random.randint(50, 100, size=size)
    turno = np.random.choice(['Manhã', 'Tarde', 'Noite'], size=size)

    # Criando DataFrame
    df = pd.DataFrame({
        'Nome': nomes,
        'Nota_1': nota1,
        'Nota_2': nota2,
        'Turno': turno
    })

    return df