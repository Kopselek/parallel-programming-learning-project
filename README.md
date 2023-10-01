
# Parallel Programming Learning Project

**parallel-programming-learning-project** is Python 3.x project for learning parallel.

This Python script benchmarks the execution time of various arithmetic operations using sequential and parallel (multithreading and multiprocessing) methods.
It also generates performance comparison graphs for different values.

## Used Libraries

- [Joblib](https://joblib.readthedocs.io/en/stable/) for parallel programming
- [Matplotlib](https://matplotlib.org/) for graphic visualisation

## Installation

### venv
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Usage
```bash
python main.py
```
The script will measure the execution time for various arithmetic operations and generate performance comparison graphs and print arithmetic operations results.

## Results

### Benchmarking Arithmetic Operations

The script benchmarks the following arithmetic operations Addition, Subtraction, Multiplication, Division, Squaring, Power for each operation, the script measures and prints the execution time for n=50000.

Example output for Addition on my setup:
```
Sequential: 0.005974 seconds
Parallel (Threads): 1.831201 seconds
Parallel (Processes): 2.980709 seconds
```

### Benchmarking more complex Operation

operation is **x^(1/3)+2*x+4**

Example output:
![](https://github.com/Kopselek/AgarioTS/blob/main/presentation.png)


## Conclusion
The additional resources required to initiate the processes significantly exceed the actual computation time.  
In practical terms, using multiprocessing in this scenario does not yield any advantages.  

However, if we change execution function, we will begin to notice improvements.  
change (line 93-95) to fibonacci function (i suggest change n_values to much lower):  
```bash
    sequential_time = measure_time_sequential(fibonacci, n)
    parallel_threads_time = measure_time_threads(fibonacci, n)
    parallel_processes_time = measure_time_threads(fibonacci, n, "threads")
```  
and now we can see different results:  
(test on ```[10, 15, 20, 25, 30]``` values)  
![](https://github.com/Kopselek/AgarioTS/blob/main/presentation2.png)
