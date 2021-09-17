class CyclicSort(object):

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        i = 0

        while i < len(self.nums):
            correct_index = self.nums[i] - 1
            if self.nums[i] != i + 1:
                self.swap(self.nums, correct_index, i)
            else:
                i += 1

    def swap(self, arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]

    def print_result(self):
        print(self.nums)


def main():
    numbers = CyclicSort([3,2,5,1,4])
    numbers.sort()
    numbers.print_result()

main()
