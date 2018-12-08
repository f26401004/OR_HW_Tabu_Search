# Practice for Tabu Search Algorithm

Please answer following single-machine total weighted tardiness problem. 
The objective function is to minimize the total weighted tardiness.



| Jobs | Process Time | Due Date | Weights | 
| -------- | -------- | -------- | -------- |
| 1 | 10 | 50 | 10 |
| 2 | 10 | 38 | 5 |
| 3 | 13 | 49 | 1 |
| 4 | 4 | 12 | 5 |
| 5 | 9 | 20 | 10 |
| 6 | 4 | 105 | 1 |
| 7 | 8 | 73 | 5 |
| 8 | 15 | 45 | 10 |
| 9 | 7 | 6 | 5 |
| 10 | 1 | 64 | 1 |
| 11 | 9 | 15 | 5 |
| 12 | 3 | 6 | 10 |
| 13 | 15 | 92 | 10 |
| 14 | 9 | 43 | 5 |
| 15 | 11 | 78 | 1 |
| 16 | 6 | 21 | 10 |
| 17 | 5 | 15 | 5 |
| 18 | 14 | 50 | 5 |
| 19 | 18 | 150 | 1 |
| 20 | 3 | 99 | 5 |

Please use Tabu Search (TS) algorithm to solve the problem and provide the total weighted tardiness. Show your parameter design (i.e. tabu list size) and the result.

---

* Tardness function: weight of current position job * (total process time in range(0, current position) - due date of current position job)

Use double layer loop to loop for tabu list size and iteration size for trail-and-error.

The result stored in process_log.txt, you can check trail-and-error process and final solution in the bottom of file

> The final solution is
> 1. Fitness function value: 1984
> 2. Tabu list size: 2
> 3. Waste time: 0.0250787734985
> 4. Search iteration: 83


