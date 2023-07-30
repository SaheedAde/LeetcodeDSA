class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         count = 0
#         while count < len(students):
#             if students[0] == sandwiches[0]:
#                 sandwiches.pop(0)
#                 count = 0
#             else:
#                 students.append(students[0])
#                 count+=1

#             students.pop(0)
#         return len(students)
        return self.countStudentsWithQ(students, sandwiches)

    def countStudentsWithQ(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        cnt = 0
        q_size = len(students)
        while cnt < q_size:
            student = students[0]
            sandwich = sandwiches[0]
            if student == sandwich:
                sandwiches.popleft()
                cnt = 0
            else:
                students.append(student)
                cnt += 1

            students.popleft()
            q_size = len(students)

        return q_size
            