
## Linear Algebra Tutorials


- [Equivalent Statement](MIS_623_HW2_MuratCabuk.pdf)

- [Linear Algebra Questions and Answers - 1](MIS_623_HW1_MuratCabuk.pdf)

- [Linear Algebra Questions and Answers - 2](MIS_623_HW2_MuratCabuk.pdf)

- [Linear Algebra Questions and Answers - 3](MIS_623_HW3_MuratCabuk.pdf)

- [Linear Algebra Questions and Answers - 4](MIS_623_HW4_MuratCabuk.pdf)

- [Linear Algebra in 4 Pages](file:///home/muratcabuk/Projects/GitHub/PythonTutorial/NumPy/matrix_linalg/linear_algebra_in_4_pages.pdf)



## Invertable Matrix Theorem or Equivalent Statements or Nonsingular Equivalences



### Invertable Matrix Theorem

[source](http://mathworld.wolfram.com/InvertibleMatrixTheorem.html)

The invertible matrix theorem is a theorem in linear algebra which gives a series of equivalent conditions for an n×n square matrix A to have an inverse. In particular, A is invertible if and only if any (and hence, all) of the following hold:

1. A is row-equivalent to the n×n identity matrix I_n.

2. A has n pivot positions.

3. The equation Ax=0 has only the trivial solution x=0.

4. The columns of A form a linearly independent set.

5. The linear transformation x->Ax is one-to-one.

6. For each column vector b in R^n, the equation  Ax=b has a unique solution.

7. The columns of A span R^n.

8. The linear transformation x|->Ax is a surjection.

9. There is an n×n matrix C such that CA=I_n.

10. There is an n×n matrix  D such that AD=I_n.

11. The transpose matrix A^(T) is invertible.

12. The columns of A form a basis for R^n.

13. The column space of A is equal to R^n.

14. The dimension of the column space of A is n.

15. The rank of A is n.

16. The null space of A is {0}.

17. The dimension of the null space of A is 0.

18. 0 fails to be an eigenvalue of A.

19. The determinant of A is not zero.

20. The orthogonal complement of the column space of A is {0}.

21. The orthogonal complement of the null space of A is R^n.

22. The row space of A is R^n.

23. The matrix A has n non-zero singular values.

#### Sources

- [Invertable Matrix Theorem](https://math.dartmouth.edu/archive/m22s07/public_html/invertmatrixthm.pdf)
- 


### Equivalent Statements

For any nxn square matrix A, these statements are all equivalent to each other; that is, if you know that one of them is true, you know that ALL of them are true; if you know that one of them is false, you know that ALL of them are false.
1. A is nonsingular.
2. A has an inverse A-1 such that A·A-1 = In.
3. A·x = 0 has only the trivial solution x = 0.
4. A is row equivalent to the identity matrix In.
5. A·x = b has a unique solution.
6. det(A) ≠ 0.
7. The row space and column space of A are n-dimensional.
8. The rank of A is n.
9. The null space of A is {0}.
10. The nullity of A is 0.
11. The rows of A are linearly independent.
12. The columns of A are linearly independent.
13. Zero is not an eigenvalue of A.

![Equivalent Statements](https://algebra.nipissingu.ca/tutorials/vector_spacegifs/equivalence.gif)


