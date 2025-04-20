def custom_permutations(arr):
    def backtrack(path, used, res):
        if len(path) == len(arr):
            res.append(path[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                backtrack(path, used, res)
                path.pop()
                used[i] = False

    res = []
    used = [False] * len(arr)
    backtrack([], used, res)
    return res
