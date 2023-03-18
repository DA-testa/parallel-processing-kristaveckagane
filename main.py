# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    pavedieni=[(0,1) for i in range(n)]
    for i, j in enumerate(data):
        sakums = pavedieni[0][0]
        sakumsIdx = pavedieni[0][1]
        for k, Idx in pavedieni[1:]:
            if k < sakums:
                sakums = k 
                sakumsIdx = Idx
        output.append((sakumsIdx, sakums))
        pavedieni.remove((sakums, sakumsIdx))
        pavedieni.append((sakums + j, sakumsIdx))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = int(input().strip())
    m = int(input().strip())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
