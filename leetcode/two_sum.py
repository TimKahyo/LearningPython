def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(1 + i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def main():
    twoSum([1, 6, 7, 8, 10, 34], 15)


if __name__ == "__main__":
    main()
