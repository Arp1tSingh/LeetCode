class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            current_temperature = temperatures[i]

            while len(stack) > 0:

                previous_temperature = stack[-1][0]
                previous_index = stack[-1][1]

                if current_temperature <= previous_temperature:
                    break

                stack.pop()

                result[previous_index] = i - previous_index

            stack.append([current_temperature, i])

        return result