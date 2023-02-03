# #!/usr/bin/python3
# """Defines a matrix multiplication function."""


# def matrix_mul(m_a, m_b):
#     """Multiply two matrices.
#     Args:
#         m_a (list of lists of ints/floats): The first matrix.
#         m_b (list of lists of ints/floats): The second matrix.
#     Raises:
#         TypeError: If either m_a or m_b is not a list of lists of ints/floats.
#         TypeError: If either m_a or m_b is empty.
#         TypeError: If either m_a or m_b has different-sized rows.
#         ValueError: If m_a and m_b cannot be multiplied.
#     Returns:
#         A new matrix representing the multiplication of m_a by m_b.
#     """

#     if m_a == [] or m_a == [[]]:
#         raise ValueError("m_a can't be empty")
#     if m_b == [] or m_b == [[]]:
#         raise ValueError("m_b can't be empty")

#     if not isinstance(m_a, list):
#         raise TypeError("m_a must be a list")
#     if not isinstance(m_b, list):
#         raise TypeError("m_b must be a list")

#     if not all(isinstance(row, list) for row in m_a):
#         raise TypeError("m_a must be a list of lists")
#     if not all(isinstance(row, list) for row in m_b):
#         raise TypeError("m_b must be a list of lists")

#     if not all((isinstance(ele, int) or isinstance(ele, float))
#                for ele in [num for row in m_a for num in row]):
#         raise TypeError("m_a should contain only integers or floats")
#     if not all((isinstance(ele, int) or isinstance(ele, float))
#                for ele in [num for row in m_b for num in row]):
#         raise TypeError("m_b should contain only integers or floats")

#     if not all(len(row) == len(m_a[0]) for row in m_a):
#         raise TypeError("each row of m_a must should be of the same size")
#     if not all(len(row) == len(m_b[0]) for row in m_b):
#         raise TypeError("each row of m_b must should be of the same size")

#     if len(m_a[0]) != len(m_b):
#         raise ValueError("m_a and m_b can't be multiplied")

#     inverted_b = []
#     for r in range(len(m_b[0])):
#         new_row = []
#         for c in range(len(m_b)):
#             new_row.append(m_b[c][r])
#         inverted_b.append(new_row)

#     new_matrix = []
#     for row in m_a:
#         new_row = []
#         for col in inverted_b:
#             prod = 0
#             for i in range(len(inverted_b[0])):
#                 prod += row[i] * col[i]
#             new_row.append(prod)
#         new_matrix.append(new_row)

#     return 
#!/usr/bin/python3
"""
This is the matrix_mul module.
This module supplies one function, matrix_mul().
"""


def matrix_mul(m_a, m_b):
    """
    Return a new matrix multiplied.
    Args:
        m_a (list): list of lists of integers or floats.
        m_b (list): list of lists of integers or floats.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) > 0:
        for row_a in m_a:
            if len(row_a) is 0:
                raise ValueError("m_a can't be empty")
    else:
        raise ValueError("m_a can't be empty")
    if len(m_b) > 0:
        for row_b in m_b:
            if len(row_b) is 0:
                raise ValueError("m_b can't be empty")
    else:
        raise ValueError("m_b can't be empty")

    for row_a in m_a:
        for i in row_a:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row_b in m_b:
        for i in row_b:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    row_a_len = 0
    for row_a in m_a:
        if len(row_a) is not row_a_len and row_a_len is not 0:
            raise TypeError("each row of m_a must be of the same size")
        row_a_len = len(row_a)
    row_b_len = 0
    for row_b in m_b:
        if len(row_b) is not row_b_len and row_b_len is not 0:
            raise TypeError("each row of m_b must be of the same size")
        row_b_len = len(row_b)

    if row_a_len is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)] for row_a in m_a]