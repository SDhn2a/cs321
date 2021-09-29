When running itdeep-test normally, it ran in 394 seconds. When we modified it to call DFS instead of itdeep, it ran in
200 seconds, which is a speedup of less than a factor of 2. This factor should remain fairly consistent as the size of
the tree grows, so the slowdown is relatively insignificant.

When running the A* tests, it consistently ran the num-wrong-tiles test in about 1.4 seconds, and the Manhattan test in
0.1 seconds, a speedup of some 4000 from the iterative deepening of the previous assignment. Not bad.