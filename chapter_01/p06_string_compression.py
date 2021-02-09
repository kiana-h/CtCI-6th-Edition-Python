import time
import unittest

def compress_string(string):
    chars = list(string)
    if not chars:
        return 0
        
    prev = chars[0]
    counter = 1
    
    write = 0
    
    for i in range(1,len(chars)):
        curr = chars[i]
        
        if curr == prev:
            counter += 1
        
        else:
            chars[write] = prev
            write += 1
            if counter > 1:
                for char in list(str(counter)):
                    chars[write] = char
                    write += 1
            counter = 1
        prev = curr
        
    chars[write] = prev
    write += 1

    if counter > 1:
        for char in list(str(counter)):
            chars[write] = char
            write += 1
        
    
    return "".join(chars[:write])
        

# def compress_string(string):
#     compressed = []
#     counter = 0

#     for i in range(len(string)):  # noqa
#         if i != 0 and string[i] != string[i - 1]:
#             compressed.append(string[i - 1] + str(counter))
#             counter = 0
#         counter += 1

#     # add last repeated character
#     if counter:
#         compressed.append(string[-1] + str(counter))

#     # returns original string if compressed string isn't smaller
#     return min(string, "".join(compressed), key=len)


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
