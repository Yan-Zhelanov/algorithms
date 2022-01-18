def is_same_sums(array):
    need = sum(array)
    if need % 2 != 0:
        return False
    need //= 2
    dp = [[False] * (need+1) for _ in range(2)]
    for i in range(len(array)+1):
        for j in range(need+1):
            if j == 0:
                dp[1][j] = True
            # elif i == 0:
            #     dp[1][j] = False
            elif j - array[i-1] >= 0:
                if dp[0][j] or dp[0][j-array[i-1]]:
                    dp[1][j] = True
            elif dp[0][j]:
                dp[1][j] = True
        dp[0] = list(dp[1])
    return dp[-1][-1]


def test_is_same_sums():
    result = is_same_sums([1, 7, 5, 1])
    assert result
    result = is_same_sums([1, 1, 1])
    assert not result
    result = is_same_sums([3, 5, 10])
    assert not result
    result = is_same_sums([7, 7, 1, 1, 2])
    assert result
    result = is_same_sums([1, 2, 3, 4, 5, 1])
    assert result
    result = is_same_sums([3, 1, 1, 2, 2, 1])
    assert result
    result = is_same_sums([])
    assert result
    print('All tests passed!')


def test_speed():
    array = '21 213 68 5 139 14 93 65 254 140 256 219 73 173 172 87 152 270 109 122 211 273 161 20 185 90 285 227 158 42 270 177 155 182 249 74 159 288 11 279 11 238 72 136 3 54 129 209 6 121 48 165 107 121 205 267 227 141 264 200 188 184 16 123 17 144 168 141 86 59 112 253 300 35 41 154 108 277 17 292 5 29 239 147 295 29 296 234 279 143 250 197 186 52 263 199 149 281 29 288 231 287 69 247 219 292 199 18 71 124 285 299 281 287 89 276 1 193 255 216 203 292 220 81 89 152 54 236 240 56 148 288 51 201 284 151 35 57 250 164 234 219 118 295 116 148 176 151 59 203 168 234 186 198 241 148 22 197 238 134 53 81 132 8 201 236 300 17 203 123 174 9 22 161 241 69 116 42 251 160 158 255 213 287 125 282 216 177 79 204 200 56 290 152 180 226 56 214 187 83 144 165 93 39 212 97 109 127 19 152 287 292 169 3 1 299 10 147 30 245 151 133 249 240 198 146 242 62 269 11 246 177 184 56 162 217 296 234 150 163 260 127 158 201 202 285 165 227 164 78 262 276 137 62 280 110 196 152 42 117 238 225 36 74 26 118 211 175 68 277 109 126 83 229 64 58 150 101 116 157 284 7 104 19 295 104 27 81'
    array = list(map(int, array.split()))
    is_same_sums(array)


if __name__ == '__main__':
    test_is_same_sums()
    # test_speed()
    input()
    print(is_same_sums(list(map(int, input().split()))))
