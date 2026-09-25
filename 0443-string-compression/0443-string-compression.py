class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        
        # 读写两个指针各自跑，读永远都会大于等于写指针，所以不需要担心没读到的内容被覆盖
        write = read  = 0
        
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                count += 1
                read += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write