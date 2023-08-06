# 1 , 2 , 3 , 4 , 5
# # 1 , 3 , 5 , 7
# # nth term = a + (n-1)*d
class apSeries:
    def apSeriesFun(self, first_element, second_element, element_that_we_have_to_find_out):
        difference = second_element - first_element
        answer = first_element + (element_that_we_have_to_find_out - 1) * difference
        return answer


object = apSeries()
result = object.apSeriesFun(1, 3, 4)
print(result)
