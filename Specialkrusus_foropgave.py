import numpy as np
import matplotlib.pyplot as plt

def read_matrices_from_file(file_path):
    matrices = []

    # Define a custom loading function to handle empty strings
    def custom_converter(x):
        return 0 if x == '' else int(x)

    with open(file_path, 'r') as file:
        # Read all lines at once and transpose the resulting matrix
        data_matrix = np.genfromtxt(file_path, dtype=int, delimiter='\t', comments=None, converters={i: custom_converter for i in range(300)}).T

        # Iterate over each column and reshape it into a 256x256 matrix
        for column in data_matrix:
            try:
                matrix = column.reshape(256, 256)
                matrix = np.rot90(matrix)
                matrices.append(matrix)
            except ValueError:
                print("Skipping column with incorrect number of values.")

    return matrices




def plot_matrices(matrices):
    # Create a combined matrix where each matrix contributes to a different color channel
    combined_matrix = np.zeros_like(matrices[0], dtype=np.float32)
    color_step = 255 / len(matrices)

    # Plot each matrix with a different color
    for i, matrix in enumerate(matrices):
        combined_matrix += matrix * (i * color_step)

    # Normalize the combined matrix to ensure it fits within the valid color range
    combined_matrix = combined_matrix / np.max(combined_matrix) * 255

    # Display the plot
    plt.imshow(combined_matrix, cmap='viridis')  # You can choose a different colormap
    plt.colorbar()
    plt.title('Combined Matrices')
    plt.show()

# Executions
file_path = 'D:/Dokumenter/DTU/Special/Si13grader_All - Const Volume Size Sum.txt'
matrices = read_matrices_from_file(file_path)
matrices = matrices[100:300]
plot_matrices(matrices)
print('Slå_Johan')



