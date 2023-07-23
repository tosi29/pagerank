import numpy as np

def power_iteration(matrix, initial_vector, max_iterations=100, tolerance=1e-6):
    vector = initial_vector
    for i in range(max_iterations):
        new_vector = np.dot(matrix, vector)
        eigenvalue = np.linalg.norm(new_vector)  # 最大固有値の近似値として新しいベクトルのノルムを使用
        new_vector /= eigenvalue  # ベクトルの正規化
        if np.linalg.norm(new_vector - vector) < tolerance:
            break
        vector = new_vector
    return eigenvalue, vector

# 例：3x3の行列の最大固有値と対応する固有ベクトルを求める
A = np.array([
    [0, 1 / 3, 0, 1 / 3, 0, 1 / 3],
    [0, 0, 0, 1, 0, 0, ],
    [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
    [0, 0, 0, 0, 1 / 2, 1 / 2],
    [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
    [0, 0, 0, 1, 0, 0]
]).T


initial_vector = np.random.rand(6)  # 初期ベクトルをランダムに設定
eigenvalue, eigenvector = power_iteration(A, initial_vector)

print("Approximate maximum eigenvalue:", eigenvalue)
print("Approximate corresponding eigenvector:", eigenvector)

