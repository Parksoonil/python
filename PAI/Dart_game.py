def solution(dartresult: str) -> int:
    nums = []
    for s in dartresult:
        if s >= "0" and s <= "9":
            if s == '0' and nums[-1] == 1:
                nums[-1] = 10
            nums.append(int(s))
        elif s == "S":
            nums[-1] = nums[-1] ** 1
        elif s == "D":
            nums[-1] = nums[-1] ** 2
        elif s == "T":
            nums[-1] = nums[-1] ** 3
        elif s == "#":
            nums[-1] = -(nums[-1])
        elif s == '*':
            nums[-1] = nums[-1] * 2
            if len(nums) > 1:
                nums[-2] = nums[-2] * 2
    return sum(nums)
print(solution("1D2S#10S"))
print(solution("1S2D*3T"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))